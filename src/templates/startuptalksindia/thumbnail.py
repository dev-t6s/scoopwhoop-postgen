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
    <title>Startups Talk India Template</title>
    <!-- Importing Droid Serif -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Droid+Serif:wght@400;700&family=Merriweather:wght@400;700&display=swap"
      rel="stylesheet"
    />

    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "Droid Serif", "Merriweather", serif;
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

      /* Main Background Image */
      .background-image {{
        width: 100%;
        height: 100%;
        object-fit: {crop_type};
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1;
      }}

      /* 
         --- NEW: Top Gradient for Logo Visibility --- 
         This adds a subtle shadow behind the top-left logo 
      */
      .top-gradient {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 350px; /* Covers the area behind the logo */
        background: linear-gradient(
          to bottom,
          rgba(0, 0, 0, 0.4) 0%,
          /* Start with light black opacity */ rgba(0, 0, 0, 0) 100%
            /* Fade to transparent */
        );
        z-index: 2;
        pointer-events: none; /* Allows clicks to pass through if needed */
      }}

      /* Bottom Gradient Overlay - Darker at bottom for text readability */
      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 60%;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 1) 0%,
          rgba(0, 0, 0, 0.8) 40%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 2;
      }}

      /* Top Branding / Logo */
      .top-logo {{
        position: absolute;
        top: -30px;
        left: 25px;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
      }}

      .top-logo img {{
        height: 250px;
        width: auto;
      }}

      /* Circular CEO Profile Image */
      .profile-circle {{
        position: absolute;
        left: 60px;
        bottom: 380px;
        width: 320px;
        height: 320px;
        border-radius: 50%;
        overflow: hidden;
        border: 6px solid #fff;
        z-index: 5;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
      }}

      .profile-circle img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
      }}

      /* Text Content */
      .text-overlay {{
        position: absolute;
        bottom: 120px;
        left: 40px;
        right: 40px;
        text-align: center;
        z-index: 10;
        color: #ffffff;
      }}

      .headline {{
        font-family: "Droid Serif", "Merriweather", serif;
        font-size: 58px;
        font-weight: 400;
        line-height: 1.3;
        letter-spacing: -0.5px;
      }}

      /* The Green Highlight Color */
      .yellow {{
        color: #86ff00;
        font-weight: 700;
      }}

      /* Footer Elements */
      .footer {{
        position: absolute;
        bottom: 40px;
        left: 50px;
        right: 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 15;
      }}

      /* Bottom Left Decorative Dashes */
      .decorative-dashes {{
        display: flex;
        gap: 10px;
        align-items: center;
      }}

      .dash {{
        height: 12px;
        background-color: #86ff00;
        border-radius: 10px;
      }}

      .dash.long {{
        width: 60px;
      }}
      .dash.short {{
        width: 12px;
      }}

      /* Swipe Button */
      .swipe-btn img {{
        height: 60px;
        width: auto;
        cursor: pointer;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- 1. Background Image -->
      <img src="{background_image}" alt="Background" class="background-image" />

      <!-- 2. NEW: Top Gradient (Added here) -->
      <div class="top-gradient"></div>

      <!-- 3. Bottom Gradient Overlay -->
      <div class="gradient-overlay"></div>

      <!-- 4. Top Logo -->
      <div class="top-logo">
        <img src="logo.png" alt="Startups Talk India" />
      </div>

      <!-- 5. Circular Profile Image -->
      <div class="profile-circle">
        <img src="{circle_image}" alt="CEO Profile" />
      </div>

      <!-- 6. Main Text -->
      <div class="text-overlay">
        {headline}
      </div>

      <!-- 7. Footer -->
      <div class="footer">
        <div class="decorative-dashes">
          <div class="dash long"></div>
          <div class="dash short"></div>
        </div>

        <div class="swipe-btn">
          <img src="swipe.png" alt="Swipe" />
        </div>
      </div>
    </div>
  </body>
</html>
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
"""

thumbnail_template = {
    "page_name": "startuptalksindia",
    "template_type": "thumbnail",
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
