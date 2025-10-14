import logging
from pathlib import Path
from PIL import Image

from src.utils import (
    capture_html_screenshot,
    cleanup_files,
    convert_text_to_html,
    process_overlay_for_transparency,
)
from src.workflows.editor_utils import create_overlay_image, create_image_over_video, create_video_over_image

logger = logging.getLogger(__name__)


def image_editor(text: dict,page_name:str, assets: dict, image_edits: dict, html_template: str, session_id: str) -> bytes:
    try:
        if html_template is None:
            raise ValueError("HTML template is None")
        if text is None:
            raise ValueError("Text template is None")
        
        temp_dir = Path(f"./data/{page_name}/temp")
        temp_dir.mkdir(exist_ok=True)

        for key, value in assets.items():
            assets[key] = value.split("/")[-1]
        # Check if this is a text-based template 
        html_content = html_template.format(**assets, **image_edits, **text)

        html_path = f"./data/{page_name}/temp/temp_overlay_{session_id}.html"
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        overlay_image_path = f"./data/{page_name}/temp/overlay_{session_id}.png"
        capture_html_screenshot(
            file_path=html_path,
            element_selector=".container",
            output=overlay_image_path,
        )

        with open(overlay_image_path, "rb") as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error in workflow: {e}")
        return None
    finally:
        cleanup_files(temp_dir,session_id)


def video_editor(text: dict,page_name:str,assets:dict ,video_edits: dict, html_template: str, session_id: str, target_width: int = None, target_height: int = None) -> bytes:
    """
    Complete workflow to create edited video with text overlay

    Args:
        video_bytes: Raw video file bytes
        headline: Main headline text
        subtext: Subtitle text

    Returns:
        str: Path to the final video file, or None if failed
    """

    try:
        # Create temp directory
        temp_dir = Path(f"./data/{page_name}/temp")
        temp_dir.mkdir(exist_ok=True)

        video_src = assets.get("background_video")
        # del assets['background_video']
        for key, value in assets.items():
            assets[key] = value.split("/")[-1]

        # Step 2: Create the overlay image with text
        if video_edits.get("type") == "image_overlay":
            type = "bottom_to_top"
            green_screen = (0,0,0,0)
            gradient_color = (0,0,0,0)
            if video_edits.get("gradient") == "top_to_bottom":
                type = "top_to_bottom"
            if video_edits.get("green_screen"):
                green_screen = video_edits.get("green_screen")
            if video_edits.get("gradient_color"):
                gradient_color = video_edits.get("gradient_color")
            
            overlay_image_path, html_path, video_rect = create_overlay_image(
                text=text,
                assets=assets,
                html_template=html_template,
                session_id=session_id,  
                page_name=page_name,
            )

            if target_height is None or target_width is None:
                with open(overlay_image_path, "rb") as f:
                    overlay_image = Image.open(f)
                    target_height = overlay_image.height
                    target_width = overlay_image.width
            
            processed_overlay_path = process_overlay_for_transparency(
                image_path=overlay_image_path,
                session_id=session_id,
                target_width=target_width,
                target_height=target_height,
                page_name=page_name,
                green_screen=green_screen,
            )
            
            final_video_path, video_temp_files = create_image_over_video(
                video_path=video_src,
                overlay_image_path=processed_overlay_path,
                page_name=page_name,
                session_id=session_id,
                add_gradient=video_edits.get("add_gradient", True),
                target_width=target_width,
                target_height=target_height,
                crop_type=video_edits.get("crop_type", "cover"),
                offset=video_edits.get("offset", 0),
                type=type,
                gradient_color=gradient_color,
            )
        else:
            overlay_image_path, html_path, video_rect = create_overlay_image(
                text=text,
                assets=assets,
                html_template=html_template,
                session_id=session_id,  
                page_name=page_name,
                get_video=True,
                class_name = video_edits.get("class_name", ""),
            )

            if target_height is None or target_width is None:
                with open(overlay_image_path, "rb") as f:
                    overlay_image = Image.open(f)
                    target_height = overlay_image.height
                    target_width = overlay_image.width
            
            processed_overlay_path = process_overlay_for_transparency(
                image_path=overlay_image_path,
                session_id=session_id,
                target_width=target_width,
                target_height=target_height,
                page_name=page_name,
                green_screen=video_edits.get("green_screen", (0,0,0,0)),
            )
            
            final_video_path, video_temp_files = create_video_over_image(
                image_path=processed_overlay_path,
                page_name=page_name,
                video_path=video_src,
                session_id=session_id,
                width=video_rect.get("width"),
                height=video_rect.get("height"),
                x=video_rect.get("x"),
                y=video_rect.get("y"),
                padding = video_edits.get("padding", 0),
                add_gradient=video_edits.get("add_gradient", True),
                type=video_edits.get("type", "bottom_to_top"),
                gradient_color=video_edits.get("gradient_color", (0,0,0,0)),
            )

        if not final_video_path:
            logger.error("Failed to create final video")
            raise Exception("Failed to create final video")

        logger.info(f"Workflow completed successfully: {final_video_path}")
        with open(final_video_path, "rb") as f:
            return f.read()

    except Exception as e:
        logger.error(f"Error in workflow: {e}")
        raise Exception(f"Error in workflow: {e}")

    finally:
        # Step 5: Clean up temp files
        cleanup_files(temp_dir,session_id)


def text_editor(
    template: dict,
    page_name: str,
    image_edits: dict,
    video_edits: dict,
    text: dict,
    assets: dict,
    session_id: str,
    is_video: bool = False,
) -> bytes:
    """
    Editor for text-based templates
    """
    html_template = template["overlay_template"] if is_video else template["html_template"]

    # Process text inputs
    text_input = {}
    text_template = template["text"]
    
    # Add defaults for missing keys
    for key, value in text_template.items():
        if key not in text and "default" in value:
            text_input[key] = value["default"]
    # Process provided text values
    for key, value in text.items():
        if key not in text_template:
            continue
        
        template_config = text_template[key]
        if template_config["type"] in ["text", "text_area"]:
            text_input[key] = convert_text_to_html(
                tag=template_config["tag"],
                class_name=template_config["class"],
                text=value,
            )
        elif template_config["type"] == "checkbox":
            text_input[key] = template_config["html_snippet"] if value else ""
        elif template_config["type"] == "dropdown":
            text_input[key] = value

    # Process assets
    assets_input = assets
    assets_template = template["assets"]
    
    # Add defaults for missing assets
    for key, value in assets_template.items():
        if key not in assets and "default" in value:
            assets_input[key] = value["default"]

    # Process edits based on video/image mode
    if is_video:
        edits_template = template["video_edits"]
        edits_input = video_edits
    else:
        edits_template = template["image_edits"]
        edits_input = image_edits

    # Process edits
    processed_edits = {}
    for key, value in edits_template.items():
        if key not in edits_input and "default" in value:
            processed_edits[key] = value["default"]
    
    for key, value in edits_input.items():
        if key in edits_template and edits_template[key]["type"] in ["default", "dropdown"]:
            processed_edits[key] = value

    # Call appropriate editor
    if is_video:
        return video_editor(
            text=text_input,
            page_name=page_name,
            assets=assets_input,
            video_edits=processed_edits,
            html_template=html_template,
            session_id=session_id,
        )
    else:
        return image_editor(
            text=text_input,
            page_name=page_name,
            assets=assets_input,
            image_edits=processed_edits,
            html_template=html_template,
            session_id=session_id,
        )


# Test function for development
if __name__ == "__main__":
    from src.templates.marketing_stories.carousel import carousel_template
    ## Test Image Workflow
    final_image = text_editor(
        template=carousel_template['slides']['content_slide'],
        page_name="marketing_stories",
        image_edits={"crop_type": "cover" },
        video_edits={},
        text={"headline": "**DON'T START WITH THE GOAL OF**\n'DOING A STARTUP.' THE RISK IS THAT\nYOU MIGHT GET MARRIED TO THE\nWRONG IDEA TOO EARLY"},
        assets={"background_image":"test.png"},
        is_video=False,
        session_id="test",
    )
    # final_video = text_editor(
    #     template=carousel_template['slides']['content_slide'],
    #     page_name="marketing_stories",
    #     image_edits={},
    #     video_edits={"crop_type": "contain","green_screen": (128,128,128,1), "type": "image_overlay", "gradient": "top_to_bottom", "gradient_color": (255,255,255,1)},
    #     text={"headline": "**The powerful speech of this Nepali!**\n student is braking the internet"},
    #     assets={"background_image": "./data_/test.png"},
    #     is_video=True,
    #     session_id="test",
    # )

    # with open("./data_/test_out.png", "wb") as f:
    #     f.write(final_image)