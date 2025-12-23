TEMPLATE_DESCRIPTION = """
Headline/Quote Post: This Girl Life Stories (GLS) template creates eye-catching quote and headline images for social media posts focusing on Bollywood content, girly moments, relationships, lifestyle, and relatable experiences for women. It features a full-screen background image with a pink/magenta gradient overlay, bold white text (black outline) in classic meme style, and the GLS logo at the bottom with decorative lines. The template is optimized for 1080x1350 dimensions and perfect for creating engaging, shareable content about Bollywood celebrities, empowering quotes, relatable statements, and everyday girl life moments.
The template features a centered text overlay with the GLS branding prominently displayed at the bottom - ideal for impactful quotes, bold statements, and relatable one-liners.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Headline/Quote Post Slide:
  ### Attributes:
  - This creates a bold statement or quote post with a full-screen background image and centered text overlay, perfect for Bollywood content and girly relatable moments.
  
  - image_description: A one line description of the background image you would like to use.
    EX: "Deepika Padukone looking confident", "Alia Bhatt in a glamorous outfit", "A girl posing fashionably", "Kareena Kapoor smiling"
  
  - quote_text: The main quote, statement, or headline text (bold white text with black outline, centered).
    EX: "Queens don't compete with peasants", "She believed she could so she did", "Bollywood but make it relatable", "Living my best life unapologetically"

  ### Text Input:
    {{
      "name": "headline_slide",
      "image_description": "str",
      "text":{{
      "quote_text": "str"
      }}
    }}

NOTE: 
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
- Text uses the classic meme format with bold white lettering and black outline for maximum readability.
- Content should be empowering, relatable, fun, and focused on girl life moments, Bollywood celebrities, relationships, fashion, and lifestyle.
- Quote text works best when it's a bold statement, empowering quote, or relatable one-liner.
- Images work best with Bollywood actresses, confident girl moments, fashion/beauty content, or glamorous situations.
- The GLS logo appears at the bottom with decorative lines for strong brand presence.
"""

HEADLINE_SLIDE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Instagram Post Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@900&display=swap"
      rel="stylesheet"
    />
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{   
        font-family: "Inter", "Arial", sans-serif;
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
        object-position: top center;
      }}

      /* Updated gradient to match the pink/magenta tone of the reference */
      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 60%;
        background: linear-gradient(
          to top,
          rgba(255, 48, 104, 0.5) 0%,
          rgba(255, 48, 104, 0.3) 30%,
          rgba(255, 48, 104, 0.1) 50%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      .text-overlay {{
        position: absolute;
        bottom: 50px;
        left: 0;
        right: 0;
        padding: 0 40px;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
      }}

      .logo-container {{
        display: flex;
        align-items: center;
        justify-content: center;
        width: 120%;
        margin-bottom: 0px;
      }}

      .logo-line {{ 
        flex: 1;
        height: 3px;
        background: white;
      }}

      .logo-image {{
        /* Adjust width based on your actual logo file aspect ratio */
        width: auto;
        height: 180px;
        object-fit: contain;
        margin: 0 20px 0px 15px;
        filter: drop-shadow(3px 3px 0px #000);
      }}

      /* Updated Text Styling to match the meme style */
      .quote-text {{
        font-family: "Inter", sans-serif;
        font-weight: 900; /* Extra bold */
        font-size: 64px;
        color: white;
        text-align: center;
        line-height: 1.1;

        /* The specific stroke and shadow effect */
        -webkit-text-stroke: 6px black;
        letter-spacing: 1px;
        paint-order: stroke fill;
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

      <!-- Gradient Overlay -->
      <div class="gradient-overlay"></div>

      <!-- Text Overlay Section -->
      <div class="text-overlay">
        <!-- Logo Section with lines -->
        <div class="logo-container">
          <div class="logo-line"></div>
          <!-- Ensure you use a transparent PNG logo here for best results -->
          <img src="{logo_image}" alt="Logo" class="logo-image" />
          <div class="logo-line"></div>
        </div>

        <!-- Main Text -->
        {quote_text}
      </div>
    </div>
  </body>
</html>
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
"""

headline_template = {
    "page_name": "gls",
    "template_type": "headline",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "quote_text": {"type": "text_area", "tag": "div", "class": "quote-text"},
            },
            "assets":{
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"default": "logo.png"},
            },
            "image_edits": {
                "crop_type":{"default":"cover"},
            },
            "video_edits":{
            }
        },
    },
}