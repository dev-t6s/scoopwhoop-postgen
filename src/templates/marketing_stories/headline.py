TEMPLATE_DESCRIPTION = """
Thumbnail: This Marketing Stories template creates eye-catching thumbnail images for social media posts. It combines a striking background image with bold, highlighted text overlays to grab attention and drive engagement. The thumbnail should capture the essence of the story while remaining visually appealing and readable at smaller sizes.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Thumbnail Slide:
  ### Attributes:
  - This should be the opening slide of the storyboard. Must be eye catching and engaging.
    EX: A photo of a temple and a gurdwara created inside a game.
  
  - image_description: A one line description of the image you would like to use for the slide.
  - headline: The main headline of the story with no new lines. Use **str** for highlighting important words.

  ### Text Input:
    {{
      "name": "headline_slide",
      "image_description": "str",
      "text":{{
      "headline": "str",
      }}
    }}

NOTE: 
- Use **str** to highlight parts of the text and \\n for new line.
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
"""

HEADLINE_SLIDE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Marketing Stories Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&display=swap"
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
        align-items: center;
        min-height: 100vh;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
      }}

      /* Background image */
      .background-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        position: absolute;
        top: 0;
        left: 0;
      }}

      /* White gradient from top */
      .gradient-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 50%;
        background: linear-gradient(
          to bottom,
          rgba(255, 255, 255, 0.99) 0%,
          rgba(255, 255, 255, 0.8) 40%,
          rgba(255, 255, 255, 0.6) 60%,
          rgba(255, 255, 255, 0) 100%
        );
        z-index: 5;
      }}

      /* Text block */
      .text-overlay {{
        position: absolute;
        top: 40px;
        left: 60px;
        right: 60px;
        text-align: center;
        z-index: 10;
      }}

      .headline {{
        font-size: 50px;
        font-weight: 700;
        color: #000;
        line-height: 1.4;
      }}

      .headline .yellow {{
        background: #feff03; /* Bright yellow highlight */
        color: #000;
        padding: 2px 6px;
        border-radius: 2px;
      }}

      /* Logo placement */
      .logo {{
        position: absolute;
        bottom: 5%;
        right: -1px;
        display: flex;
        align-items: center;
        gap: 8px;
        z-index: 10;
        background-color: white;
        height: 50px;
        width: 140px;
        border-top-left-radius: 100%;
        border-bottom-left-radius: 100%;
      }}

      .logo img {{
        position: absolute;
        right: -1px;
        top: -13px;
        height: 70px;
        width: auto;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Background -->
      <img src="{background_image}" alt="Background" class="background-image" />

      <!-- White Gradient -->
      <div class="gradient-overlay"></div>

      <!-- Text -->
      <div class="text-overlay">
        {headline}
      </div>

      <!-- Logo -->
      <div class="logo">
        <img src="{logo_image}" alt="Marketing Stories" />
      </div>
    </div>
  </body>
</html>
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Instagram Post Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&display=swap"
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
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background-color: rgba(128, 128, 128, 1);
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
      }}

      /* Background image */
      .background-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        position: absolute;
        top: 0;
        left: 0;
      }}

      /* White gradient from top */
      .gradient-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 50%;
        background: linear-gradient(
          to bottom,
          rgba(255, 255, 255, 0.99) 0%,
          rgba(255, 255, 255, 0.8) 40%,
          rgba(255, 255, 255, 0.6) 60%,
          rgba(255, 255, 255, 0) 100%
        );
        z-index: 5;
      }}

      /* Text block */
      .text-overlay {{
        position: absolute;
        top: 40px;
        left: 60px;
        right: 60px;
        text-align: center;
        z-index: 10;
      }}

      .headline {{
        font-size: 50px;
        font-weight: 700;
        color: #000;
        line-height: 1.4;
      }}

      .headline .yellow {{
        background: #feff03; /* Bright yellow highlight */
        color: #000;
        padding: 2px 6px;
        border-radius: 2px;
      }}

      /* Logo placement */
      .logo {{
        position: absolute;
        bottom: 5%;
        right: -1px;
        display: flex;
        align-items: center;
        gap: 8px;
        z-index: 10;
        background-color: white;
        height: 50px;
        width: 140px;
        border-top-left-radius: 100%;
        border-bottom-left-radius: 100%;
      }}

      .logo img {{
        position: absolute;
        right: -1px;
        top: -13px;
        height: 70px;
        width: auto;
      }}
    </style>
  </head>
  <body>
    <div class="container">

      <!-- Text -->
      <div class="text-overlay">
        {headline}
      </div>

      <!-- Logo -->
      <div class="logo">
        <img src="{logo_image}" alt="Marketing Stories" />
      </div>
    </div>
  </body>
</html>
"""

thumbnail_template = {
    "page_name": "marketing_stories",
    "template_type": "thumbnail",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "div", "class": "headline"}
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": { "default": "logo.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
                "gradient": {"type":"default", "values": "top_to_bottom"},
                "green_screen": {"type":"default", "values": (128,128,128,1)},
                "gradient_color": {"type":"default", "values": (255,255,255,1)},
            }
        },
    },
}
