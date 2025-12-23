TEMPLATE_DESCRIPTION = """
Thumbnail: This StartupTalksIndia template creates eye-catching thumbnail images for social media posts focusing on startup news, business updates, entrepreneurship, and industry insights. It combines a striking background image with bold, highlighted text overlays to grab attention and drive engagement. The thumbnail should capture the essence of the startup story while remaining visually appealing and readable at smaller sizes.
The source should only be used if the post or the news is not from StartupTalksIndia.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Thumbnail Slide:
  ### Attributes:
  - This should be the opening slide of the storyboard. Must be eye catching and engaging.
    EX: A photo of a startup founder in their office, or a product launch event, or a business meeting.
  
  - image_description: A one line description of the image you would like to use for the slide.
  - headline: The main headline of the story with no new lines.

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
- Use Source tag to only cite external sources NOT STARTUPTALKSINDIA.
"""

HEADLINE_SLIDE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Trillionaire Culture Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,700;0,800;0,900;1,600&display=swap"
      rel="stylesheet"
    />

    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "Montserrat", sans-serif;
        background: #f0f0f0;
        display: flex;
        justify-content: center;
        min-height: 100vh;
      }}  

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        background-color: #000;
      }}

      /* --- LAYERS --- */

      /* 1. Background Image */
      .background-image {{
        width: 100%;
        height: 100%;
        object-fit: {crop_type};
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1;
      }}

      /* 2. Gradients */
      .top-gradient {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 300px;
        background: linear-gradient(
          to bottom,
          rgba(0, 0, 0, 0.6) 0%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 2;
        pointer-events: none;
      }}

      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 60%;
        background: linear-gradient(
          to top,
          rgba(15, 0, 5, 1) 0%,
          rgba(20, 0, 10, 0.9) 30%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 2;
        pointer-events: none;
      }}

      /* 3. Top Elements */
      .top-logo {{
        position: absolute;
        top: 20px;
        right: 20px;
        z-index: 10;
      }}

      .top-logo img {{
        height: 120px;
        width: auto;
      }}  

      /* --- DYNAMIC BOTTOM SECTION --- */

      /* This wrapper sits at the bottom and grows upwards based on content */
      .content-layout {{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        z-index: 20;
        display: flex;
        flex-direction: column;
        /* Aligns items to the right so the circle stays right */
        align-items: flex-end;
      }}

      /* 4. Circular Profile Image */
      /* No longer absolute positioning */
      .profile-circle {{
        width: 380px;
        height: 380px;
        border-radius: 50%;
        overflow: hidden;
        border: 4px solid #530328;

        /* Positioning logic */
        margin-right: 40px; /* Distance from right edge */
        margin-bottom: 20px; /* Pulls the circle DOWN into the text box slightly */
        z-index: 25; /* Ensures circle sits ON TOP of the text background */
        position: relative;
      }}

      .profile-circle img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
      }}

      /* 5. Text Box Background */
      .text-content {{
        width: 100%;
        background-color: #170418;
        padding: 0px 40px 20px 40px; /* Top padding creates space for the overlapping circle */
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        z-index: 20;
      }}

      .headline {{
        color: #ffffff;
        font-family: "Montserrat", sans-serif;
        font-size: 62px;
        font-weight: 700;
        text-align: center;
        text-transform: uppercase;
        line-height: 1.2;
      }}

      .yellow {{
        background-color: #530328;
        padding: 0px 10px;
      }}

      .footer-text {{
        color: #ffffff;
        font-family: "Montserrat", sans-serif;
        font-size: 22px;
        font-weight: 600;
        font-style: italic;
        margin-top: 10px;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- 1. Background Image -->
      <img src="{background_image}" alt="Background" class="background-image" />

      <!-- 2. Gradients -->
      <div class="top-gradient"></div>
      <div class="gradient-overlay"></div>

      <!-- 3. Top Logo -->
      <div class="top-logo">
        <img src="logo.png" alt="Logo" />
      </div>

      <!-- DYNAMIC CONTENT WRAPPER -->
      <!-- Holds both the circle and the text box -->
      <div class="content-layout">
        <!-- 4. Circle Insert (Stacked on top of text) -->
        <div class="profile-circle">
          <img src="{circle_image}" alt="Circle Insert" />
        </div>

        <!-- 5. Text Content (Stacked below circle) -->
        <div class="text-content">
          {headline}

          <div class="footer-text">Trillionaire Culture</div>
        </div>
      </div>
    </div>
  </body>
</html>
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
"""

headline_template = {
    "page_name": "trillionaire_culture",
    "template_type": "headline",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "div", "class": "headline"},
            },
            "assets":{
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"default": "logo.png"},
                "circle_image": {"type":"bytes", "file_type":"png", "default": "circle_image.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
            },
            "video_edits":{
            }
        },
    },
}
