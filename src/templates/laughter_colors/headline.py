TEMPLATE_DESCRIPTION = """
Thumbnail: This Laughter Colors template creates eye-catching thumbnail images for social media posts. It combines a striking background image with bold, highlighted text overlays to grab attention and drive engagement. The thumbnail should capture the essence of the story while remaining visually appealing and readable at smaller sizes.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Thumbnail Slide:
  ### Attributes:
  - image_description: A one line description of the image you would like to use for the slide.
    EX: A photo of a temple and a gurdwara created inside a game.
  
  - headline: The main headline of the story with no new lines. Max 4-5 words
  
  - subtext: A short subtext for the post, one-two sentence max.

  ### Text Input:
    {{
      "name": "headline_slide",
      "image_description": "str",
      "text":{{
      "headline": "str",
      "subtext": "str",
      }}
    }}

NOTE: 
- \\n for new line.
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
"""

HEADLINE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Instagram Post Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "Poppins", sans-serif;
        background: #f0f0f0;
        display: flex;
        justify-content: center;
        /* align-items: center; */
        min-height: 100vh;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        background: #000;
        display: flex;
        flex-direction: column;
      }}

      /* Top Banner */
      .top-banner {{
        width: 100%;
        background: #ffd600;
        padding: 50px 20px;
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        color: black;
      }}

      /* Middle image area */
      .image-container {{
        flex: 1;
        width: 100%;
        overflow: hidden;
      }}

      .image-container img {{
        width: 100%;
        height: 100%;
        object-fit: {crop_type};
        display: block;
      }}

      /* Bottom Banner */
      .bottom-banner {{
        width: 100%;
        background: #000;
        padding: 80px 30px;
        text-align: center;
      }}

      .bottom-banner .subtext {{
        font-size: 50px;
        font-weight: 600;
        color: white;
        line-height: 1.4;
        margin-left: auto;
        margin-right: auto;
      }}

      /* Export button */
      .export-button {{
        position: fixed;
        top: 20px;
        right: 20px;
        background: #007bff;
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
        transition: all 0.3s ease;
        z-index: 1000;
      }}

      .export-button:hover {{
        background: #0056b3;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 123, 255, 0.4);
      }}

      .export-button:active {{
        transform: translateY(0);
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Top Banner -->
      {headline}

      <!-- Image -->
      <div class="image-container">
        <img src="{background_image}" alt="Post Image" />
      </div>

      <!-- Bottom Banner -->
      <div class="bottom-banner">
        {subtext}
      </div>
    </div>
  </body>
</html>
"""

HEADLINE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Instagram Post Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "Poppins", sans-serif;
        background: rgba(128,128,128,1);
        display: flex;
        justify-content: center;
        /* align-items: center; */
        min-height: 100vh;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        background: rgba(128,128,128,1);
        display: flex;
        flex-direction: column;
      }}

      /* Top Banner */
      .top-banner {{
        width: 100%;
        background: #ffd600;
        padding: 50px 20px;
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        color: black;
      }}

      /* Middle image area */
      .image-container {{
        flex: 1;
        width: 100%;
        overflow: hidden;
      }}

      .image-container video {{
        width: 100%;
        height: 100%;
        object-fit: contain;
        display: block;
      }}

      /* Bottom Banner */
      .bottom-banner {{
        width: 100%;
        background: #000;
        padding: 80px 30px;
        text-align: center;
      }}

      .bottom-banner .subtext {{
        font-size: 50px;
        font-weight: 600;
        color: white;
        line-height: 1.4;
        margin-left: auto;
        margin-right: auto;
      }}

      /* Export button */
      .export-button {{
        position: fixed;
        top: 20px;
        right: 20px;
        background: #007bff;
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
        transition: all 0.3s ease;
        z-index: 1000;
      }}

      .export-button:hover {{
        background: #0056b3;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 123, 255, 0.4);
      }}

      .export-button:active {{
        transform: translateY(0);
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Top Banner -->
      {headline}

      <!-- Image -->
      <div class="image-container">
        <video src="{background_video}" alt="Post Image" />
      </div>

      <!-- Bottom Banner -->
      <div class="bottom-banner">
        {subtext}
      </div>
    </div>
  </body>
</html>
"""

laughter_colors_headline_template = {
    "page_name": "laughter_colors",
    "template_type": "headline",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "div", "class": "top-banner"},
                    "subtext": {"type": "text_area", "tag": "div", "class": "subtext"},
                    
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            },
            "video_edits":{
                "type": {"type":"default", "values": "video_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
                "green_screen": {"type":"defauly","values": (128,128,128,1)},
                "class_name": {"type":"default","values": "image-container"},
                "padding": {"type":"default","values": 256},
            }
        },
    },
}