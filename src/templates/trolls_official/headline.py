TEMPLATE_DESCRIPTION = """
Thumbnail: This trolls_official template creates eye-catching thumbnail images for social media posts. It combines a striking background image with bold, highlighted text overlays to grab attention and drive engagement. The thumbnail should capture the essence of the story while remaining visually appealing and readable at smaller sizes.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Thumbnail Slide:
  ### Attributes:
  - image_description: A one line description of the image you would like to use for the slide.
    EX: A photo of a temple and a gurdwara created inside a game.
  
  - headline: The main headline of the story. Max one - two sentences

  ### Text Input:
    {{
      "name": "headline_slide",
      "image_description": "str",
      "text":{{
      "headline": "str",
      }}
    }}

NOTE: 
- To emphasize specific words or phrases in your text, wrap them with double asterisks (**like this**) for bold highlighting.
- Use '\\n' to indicate line breaks within the text.
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
      href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "Montserrat", "Arial", sans-serif;
        background-color: #f0f0f0;
        display: flex;
        justify-content: center;
        min-height: 100vh;
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
      }}

      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 70%;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.9) 0%,
          rgba(0, 0, 0, 0.7) 25%,
          rgba(0, 0, 0, 0.5) 50%,
          rgba(0, 0, 0, 0.2) 75%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      .logo-container {{
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 0px;
        gap: 1px;
      }}

      .logo-line {{
        flex: 1;
        height: 2px;
        background: white;
      }}

      .logo-main {{
        font-size: 48px;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        line-height: 1;
        margin-bottom: 5px;
      }}

      .logo-sub {{
        font-size: 18px;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        font-weight: 300;
      }}

      .logo-image {{
        max-width: 200px;
        max-height: 80px;
        object-fit: contain;
        filter: drop-shadow(2px 2px 4px rgba(0, 0, 0, 0.8));
        margin-left: 15px;
      }}

      .text-overlay {{
        position: absolute;
        bottom: 80px;
        left: 0;
        right: 0;
        padding: 40px 60px 40px 60px;
        z-index: 10;
      }}

      .quote-text {{
        font-size: 48px;
        color: white;
        line-height: 1.25;
        margin-bottom: 25px;
        font-weight: 700;
      }}

      .yellow {{
        background: #00ffff;
        color: #000;
        padding: 2px 8px;
        border-radius: 2px;
        font-weight: bold;
      }}

    </style>
  </head>
  <body>
    <div class="container">
      <!-- Background Image - Replace with your image URL -->
      <img
        src="{background_image}"
        alt="Background"
        class="background-image"
      />

      <!-- Gradient Overlay -->
      <div class="gradient-overlay"></div>

      <!-- Text Overlay Section -->
      <div class="text-overlay">
        <!-- Logo Section with lines -->
        <div class="logo-container">
          <div class="logo-line"></div>
          <img
            src="./trollsofficiallogo.png"
            alt="Logo"
            class="logo-image"
          />
          <div class="logo-line"></div>
        </div>

        <!-- Main Text - Replace with your content -->
        {headline}
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
      href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "Montserrat", "Arial", sans-serif;
        background-color: #f0f0f0;
        display: flex;
        justify-content: center;
        min-height: 100vh;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        background: #000;
      }}

      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 70%;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.9) 0%,
          rgba(0, 0, 0, 0.7) 25%,
          rgba(0, 0, 0, 0.5) 50%,
          rgba(0, 0, 0, 0.2) 75%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      .logo-container {{
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 0px;
        gap: 1px;
      }}

      .logo-line {{
        flex: 1;
        height: 2px;
        background: white;
      }}

      .logo-main {{
        font-size: 48px;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        line-height: 1;
        margin-bottom: 5px;
      }}

      .logo-sub {{
        font-size: 18px;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        font-weight: 300;
      }}

      .logo-image {{
        max-width: 200px;
        max-height: 80px;
        object-fit: contain;
        filter: drop-shadow(2px 2px 4px rgba(0, 0, 0, 0.8));
        margin-left: 15px;
      }}

      .text-overlay {{
        position: absolute;
        bottom: 80px;
        left: 0;
        right: 0;
        padding: 40px 60px 40px 60px;
        z-index: 10;
      }}

      .quote-text {{
        font-size: 48px;
        color: white;
        line-height: 1.25;
        margin-bottom: 25px;
        font-weight: 700;
      }}

      .yellow {{
        background: #00ffff;
        color: #000;
        padding: 2px 8px;
        border-radius: 2px;
        font-weight: bold;
      }}

    </style>
  </head>
  <body>
    <div class="container">
      <!-- Text Overlay Section -->
      <div class="text-overlay">
        <!-- Logo Section with lines -->
        <div class="logo-container">
          <div class="logo-line"></div>
          <img
            src="./trollsofficiallogo.png"
            alt="Logo"
            class="logo-image"
          />
          <div class="logo-line"></div>
        </div>

        <!-- Main Text - Replace with your content -->
        {headline}
      </div>
    </div>
  </body>
</html>
"""

trolls_official_headline_template = {
    "page_name": "trolls_official",
    "template_type": "headline",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "div", "class": "quote-text"},
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