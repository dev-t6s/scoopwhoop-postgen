import re
from pathlib import Path
import time
import logging
import os
from typing import List
import io

from PIL import Image, ImageDraw
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

## General Utils
def extract_x(response: str, code_type: str) -> str:
    pattern = rf"```{code_type}\s*(.*?)```"
    match = re.search(pattern, response, re.DOTALL)
    return match.group(1).strip() if match else None

def cleanup_files(dir_path: str, session_id: str) -> None:
    """Delete all temporary files generated during the workflow that contain the session_id"""
    for file_path in os.listdir(dir_path):
        try:
            if not file_path:
                continue
            full_path = os.path.join(dir_path, file_path)
            if os.path.exists(full_path):
                if session_id in file_path:
                    os.remove(full_path)
                    logger.info(f"Deleted temporary file: {full_path}")
        except Exception as e:
            logger.warning(f"Failed to delete file {full_path}: {e}")


## Image Utils
def capture_html_screenshot(
    file_path: str,
    element_selector: str,
    output: str = "./data/scoopwhoop/element_screenshot.png",
    zoom: float = 1.0,
    delay: float = 0.6,
    headless: bool = True,
    get_video: bool = False,
    class_name:str = ''
):
    file_url = Path(file_path).resolve().as_uri()
    video_rect = None

    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--window-size=1920,2300")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")    
    options.add_argument("--disable-dev-shm-usage")
    
    # Suppress Chrome DevTools messages
    options.add_argument("--log-level=2")  # Show warnings and errors only
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--silent")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(file_url)

        # Apply zoom if needed
        if zoom != 1.0:
            driver.execute_script(f"document.body.style.zoom='{zoom}';")

        time.sleep(delay)

        # Find the element (e.g., an <img> tag)
        element = driver.find_element("css selector", element_selector)
        if get_video:
            video_element = driver.find_element("css selector", f".{class_name}")
            video_rect = video_element.rect  # Returns {'x': int, 'y': int, 'width': int, 'height': int}

        # Capture screenshot of the element
        element.screenshot(output)
        logger.info(f"Image element captured and saved to {output}")

        return video_rect
    except Exception as e:
        logger.error(f"Error capturing image element: {e}")
        raise e
    finally:
        driver.quit()
        return video_rect


def pil_image_to_bytes(image, format="PNG"):
    buffer = io.BytesIO()
    image.save(buffer, format=format)
    return buffer.getvalue()


def compress_image(
    image_data: bytes, max_size: tuple = (1200, 1800), quality: int = 80
) -> bytes:
    """
    Compress an image while maintaining aspect ratio and quality.

    Args:
        image_data: Raw image bytes
        max_size: Maximum dimensions (width, height) for the image
        quality: JPEG quality (1-100, higher is better quality)

    Returns:
        Compressed image bytes

    Example:
        ```python
        with open("image.jpg", "rb") as f:
            image_bytes = f.read()
        compressed_bytes = compress_image(image_bytes)
        ```
    """
    try:
        # Validate image data is not empty
        if not image_data:
            raise ValueError("Image data is empty")
        
        # Open image from bytes
        img = Image.open(io.BytesIO(image_data))

        # Convert to RGB if necessary (for PNG with transparency)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Calculate new dimensions while maintaining aspect ratio
        ratio = min(max_size[0] / img.width, max_size[1] / img.height)
        if ratio < 1:  # Only resize if image is larger than max_size
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)

        # Save compressed image to bytes
        output = io.BytesIO()
        img.save(output, format="JPEG", quality=quality, optimize=True)
        return output.getvalue()

    except Exception as e:
        print(f"Error compressing image: {e}")
        return image_data  # Return original if compression fails


def crop_image(
    image_bytes: bytes,
    output_width: int = 1080,
    output_height: int = 1350,
    bias: float = 0.35,
) -> bytes:
    """
    Crops an image to the specified size with subject-biased centering.

    Args:
        image_path: Path to the input image.
        output_path: Path to save the cropped image.
        output_width: Target width (default 1080).
        output_height: Target height (default 1350).
        bias: Bias from center to keep subject in view (0 = left-aligned, 0.5 = center, 1 = right-aligned).

    Returns:
        Path to the cropped image.
    """
    # Validate image bytes is not empty
    if not image_bytes:
        raise ValueError("Image bytes is empty")
    
    img = Image.open(io.BytesIO(image_bytes))
    scale_factor = output_height / img.height
    resized_width = int(img.width * scale_factor)
    resized_img = img.resize((resized_width, output_height), Image.Resampling.LANCZOS)

    left = int((resized_width - output_width) * bias)
    top = 0
    right = left + output_width
    bottom = output_height

    cropped = resized_img.crop((left, top, right, bottom))
    buffer = io.BytesIO()
    cropped.save(buffer, format="PNG")

    return buffer.getvalue()


def create_gradient_overlay(
    width: int, height: int, gradient_height_ratio: float = 0.35
) -> Image:
    """
    Create a gradient overlay image that's transparent at top and black at bottom
    """
    gradient_height = int(height * gradient_height_ratio)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    for y in range(gradient_height):
        alpha = int(y * 1.2)
        draw = ImageDraw.Draw(img)
        y_pos = height - gradient_height + y
        draw.line([(0, y_pos), (width, y_pos)], fill=(0, 0, 0, alpha))

    return img


def process_overlay_for_transparency(
    image_path: str, session_id: str, target_width: int = 576, target_height: int = 720, page_name: str = "scoopwhoop"
) -> str:
    """
    Process overlay image to make black areas transparent
    """
    try:
        img = Image.open(image_path).convert("RGBA")
        pixels = img.getdata()
        new_pixels = []

        for pixel in pixels:
            r, g, b, a = pixel
            if r == 0 and g == 0 and b == 0:
                new_pixels.append((255, 255, 255, 0))  # Make black transparent
            else:
                new_pixels.append(pixel)

        img.putdata(new_pixels)
        resized_img = img.resize(
            (target_width, target_height), Image.Resampling.LANCZOS
        )
        output_path = f"./data/{page_name}/temp/processed_overlay_{session_id}.png"
        resized_img.save(output_path, format="PNG")
        return output_path

    except Exception as e:
        logger.error(f"Error processing overlay image Error: {e}")
        return None


## Text-Html Utils
def extract_text_from_html(html_content):
    """Extract clean text from HTML content, converting spans to **text** syntax"""
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        # Convert yellow spans to **text** syntax
        for span in soup.find_all("span", class_="yellow"):
            span.replace_with(f"**{span.get_text()}**")

        # Get text content, replace <br/> with newlines
        text = soup.get_text(separator=" ").strip()
        text = re.sub(r"<br\s*/?>", "\n", text)
        return text if text else ""
    except Exception as e:
        logger.error(f"Error extracting text from HTML: {e}")
        return ""


def convert_text_to_html(tag: str, class_name: str, text: str) -> str:
    """
    Build HTML for a text element
    """
    text_lines = text.strip().split("\n")
    html_parts = []
    if not text:
        return ""
    for line in text_lines:
        line = line.strip()
        if line:
            processed_line = re.sub(
                r"\*\*([^*]+?)\*\*", r'<span class="yellow">\1</span>', line
            )
            html_parts.append(processed_line)

    return f"<{tag} class='{class_name}'>{('<br />').join(html_parts)}</{tag}>"

def get_file_type(filename: str) -> str:
    """Determine if file is image or video based on extension"""
    image_extensions = [".png", ".jpg", ".jpeg", ".gif"]
    video_extensions = [".mp4", ".mov", ".avi"]

    ext = os.path.splitext(filename.lower())[1]

    if ext in image_extensions:
        return "image"
    elif ext in video_extensions:
        return "video"
    else:
        return "unknown"


if __name__ == "__main__":
    pass
    # with open("./data_/test_cropped.png","wb") as f:
    #     f.write(crop_image(image_bytes=open("./data_/test.png","rb").read(),bias=0.5))
    video = capture_html_screenshot(file_path="./data_/bleh_22.html",element_selector=".container",output="./data_/test_out.png",delay=2,headless=True, get_video=True)
    print(video)
