TEXT_DESCRIPTION = """Create bold, viral text-only posts for ScoopWhoop. Lead with a punchy headline (use **bold** for emphasis) and follow with a short, witty subtext. The design uses a high-contrast card with brand colors, making it perfect for hot takes, quick opinions, or one-liners that are instantly shareable."""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Text Based Slide:
  - Single-slide template focused on a catchy, engaging, and viral message.
  - Note: Only one slide is required for this template.

  ### Attributes:
  - headline: The main headline of the post. Supports emphasis.
    EX: IPL just doesn't seem that **exciting** anymore.
  - subtext: A short follow-up or punchline (one sentence max).
    EX: And then I realized mummy hamesha last mai kyun khaati thi.
  ### Text Input:
    {{
      "name": "text_based_slide",
      "text":{{
      "headline": "str",
      "subtext": "str"
      }}
    }}

NOTE: 
- Use **str** to bold parts of the text and \\n for a new line.
"""

TEXT_BASED_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Text Highlight Template</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap");

      /* Base styles */
      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: "Roboto", sans-serif;
        display: flex;
        justify-content: center;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
      }}
      .background-image {{
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        /* 'cover' scales the image to fill the container, cropping sides or top/bottom as needed */
        object-fit: cover;
        /* Aligns the image. 'center' horizontally, and 25% from the top vertically to shift it up. */
        object-position: center 25%;
        z-index: 0;
      }}

      .top-left-gradient {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(
          800% 110% at 0% 0%,
          rgba(0, 0, 0, 0.35) 0%,
          rgba(0, 0, 0, 0.05) 20%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 1;
        pointer-events: none;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 90px;
        height: auto;
        z-index: 2;
      }}

      .card {{
        position: relative;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: inline-block;
        max-width: 720px;
        box-sizing: border-box;
        background-color: None;
        border-radius: 40px;
        padding: 60px 70px;
        text-align: left;
        z-index: 2;
      }}

      .headline {{  
        margin: 0;
        font-size: 80px;
        font-weight: 1000;
        color: white;
        text-shadow: 6px 8px 0px black;
      }}

      .yellow {{
        background-color: #0072ce;
        color: #e9dc01;
      }}

      .subtext {{
        margin-top: 16px;
        font-size: 34px;
        color: white;
        font-weight: 500;
      }}
    </style>
  </head>
  <body>
    <!-- Add class="dark" here for dark mode -->
    <div class="container">
      <div class="top-left-gradient"></div>
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <img src="{background_image}" class="background-image" />
      <div class="card">
        {headline}
        {subtext}
      </div>
    </div>
  </body>
</html>
"""

TEXT_BASED_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Text Highlight Template</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap");

      /* Base styles */
      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: "Roboto", sans-serif;
        display: flex;
        justify-content: center;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
        background-color: rgba(0, 247, 34, 1);
      }}

      .top-left-gradient {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(
          800% 110% at 0% 0%,
          rgba(0, 0, 0, 0.35) 0%,
          rgba(0, 0, 0, 0.05) 20%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 1;
        pointer-events: none;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 90px;
        height: auto;
        z-index: 2;
      }}

      .card {{
        position: relative;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: inline-block;
        max-width: 720px;
        box-sizing: border-box;
        background-color: None;
        border-radius: 40px;
        padding: 60px 70px;
        text-align: left;
        z-index: 2;
      }}

      .headline {{  
        margin: 0;
        font-size: 80px;
        font-weight: 1000;
        color: white;
        text-shadow: 6px 8px 0px black;
      }}

      .yellow {{
        background-color: #0072ce;
        color: #e9dc01;
      }}

      .subtext {{
        margin-top: 16px;
        font-size: 34px;
        color: white;
        font-weight: 500;
      }}
    </style>
  </head>
  <body>
    <!-- Add class="dark" here for dark mode -->
    <div class="container">
      <div class="top-left-gradient"></div>
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <div class="card">
        {headline}
        {subtext}
      </div>
    </div>
  </body>
</html>
"""

text_based_4_template = {
    "page_name": "scoopwhoop",
    "template_type": "text_based_4",
    "text_template": {"template_description":TEXT_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "text_based_slide": {
            "html_template": TEXT_BASED_HTML_TEMPLATE,
            "overlay_template": TEXT_BASED_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                "headline": {"type": "text_area", "tag": "div", "class": "headline"},
                "subtext": {"type": "text_area", "tag": "div", "class": "subtext"},
            },
            "assets":{
                "logo_image": {"type": "dropdown", "values": ["logo.png"], "default": "logo.png"},
                "background_image": {"type": "dropdown", "values": ["background.png"], "default": "background.png"},
            },
            ## No edits because background image not there
            "image_edits": {},
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "add_gradient": {"type":"default", "values": False},
                "green_screen": {"type":"default", "values": (0, 247, 34, 1)},
            }
        },
    },
}