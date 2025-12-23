TEMPLATE_DESCRIPTION = """
Meme Post: This Girl Life Stories (GLS) template creates eye-catching meme-style images for social media posts focusing on Bollywood content, girly moments, relationships, lifestyle, and relatable experiences for women. It features a vibrant pink background with bold white text (black outline) in classic meme format, a rounded image in the center, and the GLS branding. The template is optimized for 1080x1350 dimensions and perfect for creating engaging, shareable content about Bollywood celebrities, fashion, relationships, and everyday girl life moments.
The template uses the iconic meme text style with top and bottom captions overlaying a central image - ideal for relatable, fun, and trendy posts.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Meme Post Slide:
  ### Attributes:
  - This creates a meme-style post with bold text captions and a central image, perfect for Bollywood content and girly relatable moments.
  
  - image_description: A one line description of the main image you would like to use.
    EX: "Deepika Padukone looking stunning at an event", "Alia Bhatt making a funny expression", "A girl doing makeup in mirror"
  
  - headline: The top caption text in classic meme format (bold white text with black outline).
    EX: "When you finally find the perfect outfit", "POV: Your best friend gets engaged before you", "That feeling when your crush likes your story"
  
  - bottom_text: The bottom caption text that provides the punchline or completes the meme (bold white text with black outline).
    EX: "But it's already in the laundry", "Trying to act happy but dying inside", "Screenshot at 3 AM to analyze every detail"

  ### Text Input:
    {{
      "name": "headline_slide",
      "image_description": "str",
      "text":{{
      "headline": "str",
      "bottom_text": "str"
      }}
    }}

NOTE: 
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
- Text uses the classic meme format with bold white lettering and black outline for maximum readability.
- Content should be relatable, fun, and focused on girl life moments, Bollywood celebrities, relationships, fashion, and lifestyle.
- Headline is the setup, bottom_text is the punchline or completion of the thought.
- Images work best with Bollywood actresses, relatable girl moments, fashion/beauty content, or everyday situations.
"""

HEADLINE_SLIDE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Meme Post Template</title>
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@900&display=swap"
      rel="stylesheet"
    />
    <style>
      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: "Inter", sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #333; /* Dark background for preview only */
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        /* The specific pink from the reference */
        background-color: #f9c8d4;
        padding: 60px;
        box-sizing: border-box;
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }}

      /* --- LOGO --- */
      .brand-logo {{
        position: absolute;
        top: 30px;
        right: 30px; /* Moved to top right per reference */
        width: 140px;
        height: auto;
        z-index: 20;
        object-fit: contain;
      }}

      /* --- TEXT STYLES --- */
      .meme-text {{
        font-family: "Inter", sans-serif;
        font-weight: 900; /* Extra bold */
        color: #ffffff;
        text-align: center;
        line-height: 1.2;
        /* The iconic black outline */
        -webkit-text-stroke: 5px #000000;
        paint-order: stroke fill;
        z-index: 10;
        width: 100%;
      }}

      /* Top Heading */
      .top-text {{
        font-size: 54px;
        margin-top: 80px; /* Space for logo */
        margin-bottom: 40px;
        max-width: 90%;
      }}

      /* --- IMAGE CONTAINER --- */
      .image-wrapper {{
        position: relative;
        width: 95%;
        flex-grow: 1; /* Takes up remaining space */
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
        border-radius: 60px; /* Large rounded corners */
        overflow: hidden;
        /* Optional: Limits height to prevent overflow if text is long */
        max-height: 900px;
      }}    

      .main-image {{
        width: 100%;
        height: 100%;
        object-fit: {crop_type};
        display: block;
      }}

      /* --- BOTTOM CAPTION OVERLAY --- */
      .bottom-text-container {{ 
        position: absolute;
        bottom: 40px;
        left: 0;
        width: 100%;
        padding: 0 20px;
        box-sizing: border-box;
        display: flex;
        justify-content: center;
      }}

      .bottom-text {{
        font-size: 54px;
        margin: 0;
        /* Ensure it pops over the image */
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Logo moved to top right -->
      <img src="{logo_image}" alt="Logo" class="brand-logo" />

      <!-- Top Headline -->
      {headline}

      <!-- Main Image Area -->
      <div class="image-wrapper">
        <img
          src="{background_image}"
          alt="Main Content"
          class="main-image"
        />

        <!-- Bottom Caption (Overlay) -->
        <div class="bottom-text-container">
          {bottom_text}
        </div>
      </div>
    </div>
  </body>
</html>
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
"""

thumbnail_template = {
    "page_name": "gls",
    "template_type": "thumbnail",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "h1", "class": "meme-text top-text"},
                    "bottom_text": {"type": "text_area", "tag": "h2", "class": "meme-text bottom-text"},
            },
            "assets":{
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"type":"bytes", "file_type":"png", "default": "logo.png"},
            },
            "image_edits": {
                "crop_type":{"type":"dropdown", "values":["cover", "contain"], "default":"contain"},
            },
            "video_edits":{
            }
        },
    },
}