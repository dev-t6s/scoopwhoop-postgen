TEMPLATE_DESCRIPTION = """This dope indian template creates fun, viral, and engaging social media content with bold text on a vibrant yellow background. Perfect for interactive posts like quizzes, fun facts, relatable content, and trending topics that drive engagement.
NOTE: You can either have one slide or create multiple slides with the same slide template."""

JSON_DESCRIPTION = """
This template has the following slides/sections:
1. Writeup Slide:
  - This should be the opening slide of the storyboard. Must be eye catching and engaging.

  ### Attributes:
  - headline: A catchy, viral-worthy headline that grabs attention. Should be bold and engaging, max 2-3 lines. 
    EX: Your birth month reveals your cartoon character.
  ### Text Input:
    {{
      "name": "writeup_slide",
      "text": {{
      "headline": "str",
      }}
    }}

NOTE: 
- Use \\n for new line.
"""

WRITEUP_SLIDE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>The Dope Indian</title>
    <style>
      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: "Arial MT Pro", Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #f0f0f0;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        background-image: url("background.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        color: black;
        box-sizing: border-box;
      }}

      .headline {{
        font-size: 56px;
        font-weight: 700;
        line-height: 1.2;
        text-align: center;
        width: 100%;
        margin: 0;
      }}

      .swipe {{
        position: absolute;
        bottom: 50px;
        right: 60px;
        font-size: 45px;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 65px;
        height: 65px;
        border-radius: 50%;
        background-color: rgba(255, 255, 255, 0.3);
      }}

      .handle {{
        position: absolute;
        bottom: 50px;
        left: 60px;
        font-size: 32px;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 8px;
      }}
    </style>
  </head>
  <body>
    <div class="container">
        {headline}
    </div>
  </body>
</html>
"""

writeup_template = {
    "page_name": "the_dope_indian",
    "template_type": "writeup",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "writeup_slide": {
            "html_template": WRITEUP_SLIDE_HTML_TEMPLATE,
            "overlay_template": "",
            "text_only": True,
            "text": {
                "headline": {"type": "text_area", "tag": "h1", "class": "headline"},
            },
            "assets":{
                "background_image": {"type": "dropdown", "values": ["background.png"], "default": "background.png"},
            },
            ## No edits because background image not there
            "image_edits": {},
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
            }
        }
    },
}