TEMPLATE_DESCRIPTION = """
Thumbnail: This the thatva template creates eye-catching thumbnail images for social media posts. It combines a striking background image with bold, highlighted text overlays to grab attention and drive engagement. The thumbnail should capture the essence of the story while remaining visually appealing and readable at smaller sizes.
This is a single slide template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Thumbnail Slide:
  ### Attributes:
  - image_description: A one line description of the image you would like to use for the slide.
    EX: A photo of a temple and a gurdwara created inside a game.
  
  - headline: The main headline of the story with no new lines.
  
  - subtext: A short subtext for the post, one sentence max.

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
        /* align-items: center; */
        min-height: 100vh;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        object-fit: {crop_type};
        position: absolute;
        top: 0;
        left: 0;
      }}

      /* Gradient overlay */
      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 55%;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.95) 0%,
          rgba(0, 0, 0, 0.7) 40%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      /* Text area */
      .text-overlay {{
        position: absolute;
        bottom: 130px;
        left: 35px;
        right: 35px;
        text-align: center;
        z-index: 10;
      }}

      .headline {{
        font-size: 50px;
        font-weight: 600;
        color: #fff;
        line-height: 1.4;
        /* margin-bottom: 20px; */
      }}

      .headline .yellow {{
        background: #ffbe80; /* Orange-beige highlight */
        color: #000;
        padding: 2px 4px;
        border-radius: 3px;
      }}

      .subtext {{
        font-size: 24px;
        font-weight: 500;
        color: #ddd;
        line-height: 1.4;
      }}

      /* Logo section */
      .footer {{
        position: absolute;
        bottom: 30px;
        left: 40px;
        right: 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 15;
      }}

      .logo img {{
        height: 60px;
        width: auto;
      }}

      .arrow {{
        font-size: 32px;
        color: white;
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
      <!-- Background -->
      <img
        src={background_image}
        alt="Background"
        class="background-image"
      />

      <!-- Gradient Overlay -->
      <div class="gradient-overlay"></div>

      <!-- Text -->
      <div class="text-overlay">
        {headline}
        {subtext}
      </div>

      <!-- Footer -->
      <div class="footer">
        <div class="logo">
          <img src="./tatvalight.png" alt="The Tatva" />
        </div>
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
        background: #000000;
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
      }}

      /* Gradient overlay */
      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 55%;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.95) 0%,
          rgba(0, 0, 0, 0.7) 40%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      /* Text area */
      .text-overlay {{
        position: absolute;
        bottom: 130px;
        left: 35px;
        right: 35px;
        text-align: center;
        z-index: 10;
      }}

      .headline {{
        font-size: 50px;
        font-weight: 600;
        color: #fff;
        line-height: 1.4;
        /* margin-bottom: 20px; */
      }}

      .headline .yellow {{
        background: #ffbe80; /* Orange-beige highlight */
        color: #000;
        padding: 2px 4px;
        border-radius: 3px;
      }}

      .subtext {{
        font-size: 24px;
        font-weight: 500;
        color: #ddd;
        line-height: 1.4;
      }}

      /* Logo section */
      .footer {{
        position: absolute;
        bottom: 30px;
        left: 40px;
        right: 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 15;
      }}

      .logo img {{
        height: 60px;
        width: auto;
      }}

      .arrow {{
        font-size: 32px;
        color: white;
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
      <!-- Text -->
      <div class="text-overlay">
        {headline}
        {subtext}
      </div>

      <!-- Footer -->
      <div class="footer">
        <div class="logo">
          <img src="./tatvalight.png" alt="The Tatva" />
        </div>
      </div>
    </div>
  </body>
</html>
"""

the_thatva_headline_template = {
    "page_name": "the_tatva",
    "template_type": "headline",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "div", "class": "headline"},
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
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            }
        },
    },
}