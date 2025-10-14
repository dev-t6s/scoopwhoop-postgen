from src.grafana_logger.app import GrafanaCloudLogger
import os 

from dotenv import load_dotenv

load_dotenv()

logger = GrafanaCloudLogger(
    service_name=os.getenv('SERVICE_NAME') or "postgen",
    environment=os.getenv('ENVIRONMENT') or "test",
    loki_url=os.getenv('LOKI_URL'),
    username=os.getenv('LOKI_USERNAME'),
    password=os.getenv('LOKI_PASSWORD')
)