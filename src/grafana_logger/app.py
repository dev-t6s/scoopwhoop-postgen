import json
import requests
import time
import os
from datetime import datetime
from typing import Dict, Any, Optional
import logging

class GrafanaCloudLogger:
    """
    Logger class to send logs to Grafana Cloud Loki
    Supports different environments: prod, test, stage
    Only sends to Grafana in prod environment, otherwise logs locally
    """
    
    def __init__(self, 
                 loki_url: str = None, 
                 username: str = None, 
                 password: str = None, 
                 service_name: str = "default",
                 environment: str = None):
        """
        Initialize logger with environment-aware configuration
        
        Args:
            loki_url: Grafana Cloud Loki URL
            username: Grafana Cloud username
            password: Grafana Cloud password
            service_name: Name of the service using this logger
            environment: Environment (prod/test/stage). If None, will try to get from ENV
        """
        self.service_name = service_name
        
        # Determine environment
        self.environment = environment or os.getenv('ENVIRONMENT', 'test').lower()
        
        # Only setup Grafana Cloud connection for prod environment
        if self.environment == 'prod':
            if not all([loki_url, username, password]):
                raise ValueError("loki_url, username, and password are required for prod environment")
            
            self.loki_url = loki_url.rstrip('/') + '/loki/api/v1/push'
            self.username = username
            self.password = password
            self.session = requests.Session()
            self.session.auth = (username, password)
            self.use_grafana = True
        else:
            self.use_grafana = False
            self.loki_url = None
            self.username = None
            self.password = None
            self.session = None
        
        # Setup local logging
        self.local_logger = logging.getLogger(f"{service_name}_{self.environment}")
        self.local_logger.setLevel(logging.INFO)
        
        # Add console handler if not already present
        if not self.local_logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                f'%(asctime)s - {service_name} - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.local_logger.addHandler(handler)
    
    def _send_to_loki(self, level: str, message: str, labels: Dict[str, str] = None) -> bool:
        """
        Send log entry to Grafana Cloud Loki (only in prod)
        """
        if not self.use_grafana:
            return False
            
        if labels is None:
            labels = {}
        
        # Default labels
        default_labels = {
            "service": self.service_name,
            "environment": self.environment,
            "level": level.lower(),
            "host": "localhost"  # You can make this dynamic
        }
        default_labels.update(labels)
        
        # Convert labels to Loki format
        label_string = ",".join([f'{k}="{v}"' for k, v in default_labels.items()])
        
        # Create timestamp in nanoseconds
        timestamp = str(int(time.time() * 1000000000))
        
        # Prepare log entry
        log_entry = {
            "streams": [
                {
                    "stream": default_labels,
                    "values": [
                        [timestamp, message]
                    ]
                }
            ]
        }
        
        try: 
            response = self.session.post(
                self.loki_url,
                headers={'Content-Type': 'application/json'},
                data=json.dumps(log_entry),
                timeout=10
            )
            
            if response.status_code == 204:
                return True
            else:
                self.local_logger.error(f"Failed to send log to Loki: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            self.local_logger.error(f"Exception sending log to Loki: {str(e)}")
            return False
    
    def _log_locally(self, level: str, message: str):
        """Log message locally based on level"""
        level_map = {
            'DEBUG': self.local_logger.debug,
            'INFO': self.local_logger.info,
            'WARNING': self.local_logger.warning,
            'ERROR': self.local_logger.error,
            'CRITICAL': self.local_logger.critical
        }
        
        log_func = level_map.get(level.upper(), self.local_logger.info)
        log_func(message)
    
    def info(self, message: str, labels: Dict[str, str] = None, **kwargs):
        """Log info level message"""
        if kwargs:
            message = f"{message} | Extra: {json.dumps(kwargs)}"
        
        # Always log locally
        self._log_locally("INFO", message)
        
        # Send to Loki only in prod
        if self.use_grafana:
            return self._send_to_loki("INFO", message, labels)
        return True
    
    def warning(self, message: str, labels: Dict[str, str] = None, **kwargs):
        """Log warning level message"""
        if kwargs:
            message = f"{message} | Extra: {json.dumps(kwargs)}"
        
        self._log_locally("WARNING", message)
        
        if self.use_grafana:
            return self._send_to_loki("WARNING", message, labels)
        return True
    
    def error(self, message: str, labels: Dict[str, str] = None, **kwargs):
        """Log error level message"""
        if kwargs:
            message = f"{message} | Extra: {json.dumps(kwargs)}"
        
        self._log_locally("ERROR", message)
        
        if self.use_grafana:
            return self._send_to_loki("ERROR", message, labels)
        return True
    
    def critical(self, message: str, labels: Dict[str, str] = None, **kwargs):
        """Log critical level message"""
        if kwargs:
            message = f"{message} | Extra: {json.dumps(kwargs)}"
        
        self._log_locally("CRITICAL", message)
        
        if self.use_grafana:
            return self._send_to_loki("CRITICAL", message, labels)
        return True
    
    def debug(self, message: str, labels: Dict[str, str] = None, **kwargs):
        """Log debug level message"""
        if kwargs:
            message = f"{message} | Extra: {json.dumps(kwargs)}"
        
        self._log_locally("DEBUG", message)
        
        if self.use_grafana:
            return self._send_to_loki("DEBUG", message, labels)
        return True
    
    def log_event(self, event_type: str, message: str, metadata: Dict[str, Any] = None, labels: Dict[str, str] = None):
        """
        Log a structured event with metadata
        """
        if metadata is None:
            metadata = {}
        
        if labels is None:
            labels = {}
        
        # Add event type to labels
        labels["event_type"] = event_type
        
        # Create structured message
        structured_message = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "message": message,
            "metadata": metadata
        }
        
        log_message = json.dumps(structured_message)
        self._log_locally("INFO", log_message)
        
        if self.use_grafana:
            return self._send_to_loki("INFO", log_message, labels)
        return True
    
    def log_api_request(self, method: str, endpoint: str, status_code: int, 
                       response_time: float = None, user_id: str = None):
        """
        Log API request with structured data
        """
        labels = {
            "api_method": method.upper(),
            "status_code": str(status_code)
        }
        
        metadata = {
            "endpoint": endpoint,
            "method": method,
            "status_code": status_code,
            "response_time_ms": response_time,
            "user_id": user_id
        }
        
        message = f"{method.upper()} {endpoint} - {status_code}"
        if response_time:
            message += f" - {response_time}ms"
        
        return self.log_event("api_request", message, metadata, labels)
    
    def log_database_operation(self, operation: str, table: str, success: bool, 
                              execution_time: float = None, error: str = None):
        """
        Log database operations
        """
        labels = {
            "db_operation": operation.lower(),
            "table": table,
            "status": "success" if success else "error"
        }
        
        metadata = {
            "operation": operation,
            "table": table,
            "success": success,
            "execution_time_ms": execution_time,
            "error": error
        }
        
        message = f"DB {operation.upper()} on {table} - {'SUCCESS' if success else 'FAILED'}"
        if error:
            message += f" - {error}"
        
        level = "INFO" if success else "ERROR"
        self._log_locally(level, json.dumps({
            "timestamp": datetime.now().isoformat(),
            "event_type": "database_operation",
            "message": message,
            "metadata": metadata
        }))
        
        if self.use_grafana:
            return self._send_to_loki(level, json.dumps({
                "timestamp": datetime.now().isoformat(),
                "event_type": "database_operation",
                "message": message,
                "metadata": metadata
            }), labels)
        return True


# Factory function to create logger instance
def create_logger(service_name: str, 
                  environment: str = None,
                  loki_url: str = None,
                  username: str = None,
                  password: str = None) -> GrafanaCloudLogger:
    """
    Create a logger instance for a specific service
    
    Args:
        service_name: Name of the service
        environment: Environment (prod/test/stage). If None, will try to get from ENV
        loki_url: Grafana Cloud Loki URL (required for prod)
        username: Grafana Cloud username (required for prod)
        password: Grafana Cloud password (required for prod)
    
    Returns:
        GrafanaCloudLogger instance
    """
    return GrafanaCloudLogger(
        loki_url=loki_url,
        username=username,
        password=password,
        service_name=service_name,
        environment=environment
    )


# Default logger instance (for backward compatibility)
# This will use environment variables for configuration
default_logger = GrafanaCloudLogger(
    loki_url="http://65.2.130.253:3100",
    username="loki-user",
    password="4O3vSL2(WOrL%nN/%R`:)gFG",
    service_name='WLDD_DMS',
    environment='test'
)

# Convenience functions for easy import (using default logger)
def log_info(message: str, **kwargs):
    return default_logger.info(message, **kwargs)

def log_warning(message: str, **kwargs):
    return default_logger.warning(message, **kwargs)

def log_error(message: str, **kwargs):
    return default_logger.error(message, **kwargs)

def log_critical(message: str, **kwargs):
    return default_logger.critical(message, **kwargs)

def log_debug(message: str, **kwargs):
    return default_logger.debug(message, **kwargs)

def log_api_request(method: str, endpoint: str, status_code: int, **kwargs):
    return default_logger.log_api_request(method, endpoint, status_code, **kwargs)

def log_database_operation(operation: str, table: str, success: bool, **kwargs):
    return default_logger.log_database_operation(operation, table, success, **kwargs)

def log_event(event_type: str, message: str, **kwargs):
    return default_logger.log_event(event_type, message, **kwargs)