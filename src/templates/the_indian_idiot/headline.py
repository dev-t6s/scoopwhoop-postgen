TEMPLATE_DESCRIPTION = """
Thumbnail: This The Indian Idiot template creates eye-catching thumbnail images for social media posts. It combines a striking background image with bold, highlighted text overlays to grab attention and drive engagement. The thumbnail should capture the essence of the story while remaining visually appealing and readable at smaller sizes.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Thumbnail Slide:
  ### Attributes:
  - image_description: A one line description of the image you would like to use for the slide.
    EX: A photo of a temple and a gurdwara created inside a game.
  
  - headline: The main headline of the story max 2 sentences.

  ### Text Input:
    {{
      "name": "headline_slide",
      "image_description": "str",
      "text":{{
      "headline": "str",
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
    <link
      href="https://fonts.googleapis.com/css2?family=GravitiCa+Rounded:wght@300;400;500;600;700;800&display=swap"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <title>Instagram Post - Trending News Style</title>
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "GravitiCa Rounded", "SF Pro Display", "SF Pro Text",
          -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial,
          sans-serif;
        /* font-family: "Poppins", sans-serif; */
        background-color: #f0f0f0;
        display: flex;
        justify-content: center;
        min-height: 100vh;
        gap: 40px;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        background: #000;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        object-fit: {crop_type};
        object-position: center;
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1;
      }}

      /* Logo top-left */
      .logo-container {{
        position: absolute;
        top: 40px;
        left: 40px;
        z-index: 3;
      }}

      .logo-image {{
        max-width: 220px;
        max-height: 80px;
        object-fit: contain;
        filter: drop-shadow(2px 2px 4px rgba(0, 0, 0, 0.6));
      }}

      /* Gradient overlay */
      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 810px;
        background: linear-gradient(
          to top,
          rgba(70, 0, 20, 0.78) 0%,
          rgba(70, 0, 20, 0.61) 20%,
          rgba(70, 0, 20, 0.48) 40%,
          rgba(70, 0, 20, 0.19) 60%,
          rgba(70, 0, 20, 0.01) 80%,
          transparent 100%
        );
        z-index: 2;
      }}

      /* Caption text */
      .caption-text {{
        position: absolute;
        bottom: 220px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 54px;
        font-weight: 700;
        color: #fff;
        /* line-height: 1.35; */
        text-align: center;
        z-index: 3;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
      }}

      .highlight {{
        color: #ff0000;
        font-weight: 800;
      }}

      /* Yellow line below text */
      .yellow-line {{
        position: absolute;
        bottom: 150px;
        left: 50%;
        transform: translateX(-50%);
        width: 110px;
        height: 10px;
        background: #d3c58a;
        z-index: 3;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Background Image -->
      <img
        src="{background_image}"
        alt="Background"
        class="background-image"
      />

      <!-- Logo -->
      <div class="logo-container">
        <img
          src="./theindianidiotlogo.png"
          alt="The Indian Idiot Logo"
          class="logo-image"
        />
      </div>

      <!-- Gradient Overlay -->
      <div class="gradient-overlay"></div>

      <!-- Caption Text -->
      {headline}
      <!-- Yellow Line -->
      <div class="yellow-line"></div>
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
    <link
      href="https://fonts.googleapis.com/css2?family=GravitiCa+Rounded:wght@300;400;500;600;700;800&display=swap"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <title>Instagram Post - Trending News Style</title>
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "GravitiCa Rounded", "SF Pro Display", "SF Pro Text",
          -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial,
          sans-serif;
        /* font-family: "Poppins", sans-serif; */
        background-color: #000000;
        display: flex;
        justify-content: center;
        min-height: 100vh;
        gap: 40px;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        background: #000000;
      }}

      /* Logo top-left */
      .logo-container {{
        position: absolute;
        top: 40px;
        left: 40px;
        z-index: 3;
      }}

      .logo-image {{
        max-width: 220px;
        max-height: 80px;
        object-fit: contain;
        filter: drop-shadow(2px 2px 4px rgba(0, 0, 0, 0.6));
      }}

      /* Caption text */
      .caption-text {{
        position: absolute;
        bottom: 220px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 54px;
        font-weight: 700;
        color: #fff;
        /* line-height: 1.35; */
        text-align: center;
        z-index: 3;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
      }}

      .highlight {{
        color: #ff0000;
        font-weight: 800;
      }}

      /* Yellow line below text */
      .yellow-line {{
        position: absolute;
        bottom: 150px;
        left: 50%;
        transform: translateX(-50%);
        width: 110px;
        height: 10px;
        background: #d3c58a;
        z-index: 3;
      }}
    </style>
  </head>
  <body>
    <div class="container">

      <!-- Logo -->
      <div class="logo-container">
        <img
          src="./theindianidiotlogo.png"
          alt="The Indian Idiot Logo"
          class="logo-image"
        />
      </div>


      <!-- Caption Text -->
      {headline}
      <!-- Yellow Line -->
      <div class="yellow-line"></div>
    </div>
  </body>
</html>
"""

the_indian_idiot_headline_template = {
    "page_name": "the_indian_idiot",
    "template_type": "headline",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "div", "class": "caption-text"},
                    
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
            },
            "image_edits": {"crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},},
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            }
        },
    },
}