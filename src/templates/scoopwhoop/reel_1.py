TEMPLATE_DESCRIPTION = """
ScoopWhoop Reel: Create short, high-impact video reels with bold headline and supporting subtitle over a full-frame background video. Optimized for viral stories and quick attention on social feeds. The overlay supports emphasis (use **bold** in the headline) and uses a green-screen background for easy compositing in post.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Reel Slide:
  ### Attributes:
  - Full-screen background video with bold headline (top) and subtitle (bottom).
  - Headline supports emphasis using **bold** (renders with brand accent color).
  - Subtitle is clean, readable, and kept short (1 line recommended).
  - Optimized for fast, viral social content.
    EX: "The powerful speech of this **Nepali student** is breaking the internet"
        (with a relevant background video)

  - background_video: MP4 video that fills the frame.
  - headline: Short, punchy line to grab attention. Supports **bold** and \\n.
  - subtitle: Brief supporting line shown near the bottom.

  ### Text Input:
    {{
      "name": "reel_slide",
      "text":{{
        "headline": "str",
        "subtitle": "str"
      }}
    }}

NOTE: 
- Keep copy concise and direct.
- Use \\n to break lines in the headline if needed.
- This template uses a green-screen background in the overlay for easy compositing in post.
"""

HEADLINE_SLIDE_HTML_TEMPLATE = """
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Marketing Stories Template</title>

    <!-- Fonts -->
    <style>
      @font-face {{
        font-family: "Cook Conthic";
        src: url("cookconthic.otf") format("opentype");
      }}

      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap");

      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "Roboto", sans-serif;
        display: flex;
        justify-content: center;
        height: 1920px;
        background: #fff;
      }}

      .container {{
        width: 1080px;
        height: auto;
        position: relative;
        overflow: hidden;
        background: #000;
      }}

      /* Headline with box */
      .headline {{
        position: absolute;
        top: 350px;
        left: 0;
        right: 0;
        text-align: center;
        font-family: "Cook Conthic", sans-serif;
        font-size: 200px;
        font-weight: 800;
        color: #ffeb00;
        line-height: 1.2;
        z-index: 10;
      }}

      /* Subtitle (bottom) */
      .subtitle {{
        position: absolute;
        bottom: 470px;
        left: 50%;
        transform: translateX(-50%);
        display: inline-block;
        background: #0072ce;
        color: #fff;
        padding: 12px 40px;
        border-radius: 40px;
        font-family: "Roboto", sans-serif;
        font-size: 50px;
        font-weight: 700;
        text-align: center;
        box-shadow: -6px 6px 0 #ffeb00; /* Yellow shadow */
        z-index: 10;
      }}

      /* Logo container */
      .logo-container {{        
        position: absolute;
        top: 80px;
        left: 40px;
        z-index: 15;
      }}

      .logo-container img {{
        height: 110px;
        width: auto;
      }}

      .yellow {{
        color: #0072ce;
      }}
    </style>
  </head>

  <body>
    <div class="container">
      <!-- Logo -->
      <div class="logo-container">
        <img src="{logo_image}" alt="Logo" />
      </div>

      <!-- Headline -->
      {headline}

      <!-- Subtitle (bottom) -->
      {subtitle}
    </div>
  </body>
</html>
"""

reel_1_template = {
    "page_name": "scoopwhoop",
    "template_type": "reel_1",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "reel_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "video_only": True,
            "text": {
                    "headline": {"type": "text_area", "tag": "div", "class": "headline"},
                    "subtitle": {"type": "text_area", "tag": "div", "class": "subtitle"},
            },
            "assets":{
                "logo_image": { "default": "logo.png"},
                "background_video": {"type":"bytes", "file_type":"mp4"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"], "default": "contain"},
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
                "add_gradient": {"type":"default", "values": False},
                "add_full_gradient": {"type":"checkbox", "html_snippet": True},
                "add_top_left_gradient": {"type":"checkbox", "html_snippet": True},
            }
        },
    },
}
