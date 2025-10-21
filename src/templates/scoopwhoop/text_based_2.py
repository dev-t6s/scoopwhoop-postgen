TEXT_DESCRIPTION = """Create bold, viral text-only posts for ScoopWhoop. Lead with a punchy headline (use **bold** for emphasis) and follow with a short, witty subtext. The design uses a high-contrast card with brand colors and supports light/dark modes, making it perfect for hot takes, quick opinions, or one-liners that are instantly shareable."""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Text Based Slide:
  - Single-slide template focused on a catchy, engaging, and viral message.
  - Note: Only one slide is required for this template.

  ### Attributes:
  - mode: Theme of the card.
    EX: dark or light
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
      "mode": "dark/light"
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
        height: 100%;
        font-family: "Roboto", sans-serif;
        background-color: black;
        display: flex;
        justify-content: center;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        background-color: white;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center;
        transition: background-color 0.4s ease;
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
          rgba(0, 0, 0, 0) 20%
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

      .headline {{
        position: relative;
        z-index: 2;
        font-size: 60px;
        font-weight: 1000;
        color: #1a1a1a;
        text-shadow: 8px 10px 0px #ffdd00; /* yellow shadow for light mode */
        line-height: 1.2;
        transition: color 0.4s ease, text-shadow 0.4s ease;
        text-align: left;
      }}

      .yellow {{
        color: #0072ce;
      }}

      .subtext {{       
        position: absolute;
        bottom: 60px;
        z-index: 2;
        font-size: 34px;
        font-weight: 600;
        color: #0072ce;
        transition: color 0.4s ease;
      }}

      /* 🌙 Dark Mode */
      body.dark {{
        background-color: #000000;
      }}

      body.dark .container {{
        background-color: #000000;
      }}

      body.dark .headline {{
        color: #ffffff;
        text-shadow: none;
      }}    

      body.dark .yellow {{
        color: #e9dc01;
      }}

      body.dark .subtext {{
        color: #e9dc01;
      }}
    </style>
  </head>
  <body class="{mode}">
    <!-- Add class="dark" here for dark mode -->
    <div class="container">
      <div class="top-left-gradient"></div>
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      {headline}
      {subtext}
    </div>
  </body>
</html>

"""

text_based_2_template = {
    "page_name": "scoopwhoop",
    "template_type": "text_based_2",
    "text_template": {"template_description":TEXT_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "text_based_slide": {
            "html_template": TEXT_BASED_HTML_TEMPLATE,
            "overlay_template": "",
            "text_only": True,
            "text": {
                "headline": {"type": "text_area", "tag": "div", "class": "headline"},
                "subtext": {"type": "text_area", "tag": "div", "class": "subtext"},
                "mode": {"type": "dropdown", "values": ["dark", "light"], "default": "light"},
            },
            "assets":{
                "logo_image": {"type": "dropdown", "values": ["logo.png"], "default": "logo.png"},
            },
            ## No edits because background image not there
            "image_edits": {},
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
            }
        },
    },
}