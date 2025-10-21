TEMPLATE_DESCRIPTION = """
**Template Name:** SW Body – One/Two-Line Card

**Primary Goal:** Create a hero card (1080×1350) with a background image and SW logo at the top-left, featuring bold body copy near the bottom. Two layout options are available: a two-line version with split placement, and a single-line version stacked near the bottom-left. Output should include `image_description` plus the text fields defined for each slide.

**General Instructions:**
*   Follow the provided HTML tags and class names exactly.
*   Keep copy short and scannable; avoid manual line breaks.
*   Use `**<str>**` to emphasize words in yellow when needed.
*   `source` is used only when crediting non‑ScoopWhoop content; keep it short (site or author name).
*   Ensure text stays readable over the image; avoid very long words.
"""
JSON_DESCRIPTION = """
This template has the following slides/sections:

**1. Body Two-Line Slide (`body_two_line_slide`)**
*   **Purpose:** Split body copy layout – a bold right-aligned line near the upper-right and a lighter line near the bottom-left. Optional source credit sits at the very bottom-left.

### Attributes:
*   **`image_description`:** One line describing the background visual and mood/style.
*   **`first_line`:** 3–8 words; headline-style; may use `**<str>**` for emphasis.
*   **`second_line`:** 6–16 words; sentence case; may use `**<str>**` sparingly.
*   **`source`:** Optional short credit (site/author); plain text.

### Text Input:
    {{
      "name": "body_two_line_slide",
      "image_description": "str",
      "text":{{
        "first_line": "str",
        "second_line": "str",
        "source": "str"
      }}
    }}

---

**2. Body One-Line Slide (`body_one_line_slide`)**
*   **Purpose:** Single, punchy body copy line near the bottom-left with optional source credit underneath.

### Attributes:
*   **`image_description`:** One line describing the background visual and mood/style.
*   **`first_line`:** 6–16 words; sentence case; may use `**<str>** ` for emphasis.
*   **`source`:** Optional short credit; plain text.

### Text Input:
    {{
      "name": "body_one_line_slide",
      "image_description": "str",
      "text":{{
        "first_line": "str",
        "source": "str"
      }}
    }}

---

**Notes:**
- Use `**<str>**` to highlight important words; avoid overuse.
- Keep image descriptions concise and visual (e.g., “soft-lit portrait, shallow depth of field”).
"""

BODY_TWO_LINE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap");

      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Roboto", sans-serif;
        background-color: black;
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
        object-fit: {crop_type};
        object-position: center 25%;
        display: block;
      }}

      /* Keep gradient and logo as is */
      .top-left-gradient {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(
          circle at 0% 0%,
          rgba(0, 0, 0, 0.7) 0%,
          rgba(0, 0, 0, 0) 30%
        );
        z-index: 0;
        pointer-events: none;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 110px;
        filter: brightness(0) invert(1);
        z-index: 2;
      }}

      /* --- Text Layout --- */

      .body-copy-1 {{
        position: absolute;
        top: 25%;
        left: 43%;
        color: white;
        font-size: 60px;
        font-weight: 600;
        line-height: 1.3;
        text-align: right;
        z-index: 2;
        width: 50%;
      }}

      .body-copy-2 {{       
        position: absolute;
        bottom: 350px;
        left: 120px;
        color: white;
        font-size: 45px;
        width: 50%;
        font-weight: 400;
        line-height: 1;
        text-align: left;
        z-index: 2;
      }}

      .yellow {{
        color: #e9dc01;
      }}

      .source {{
        position: absolute;
        bottom: 60px;
        left: 70px;
        color: white;
        font-size: 35px;
        font-weight: 400;
        opacity: 0.8;
        z-index: 2;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <div class="top-left-gradient"></div>
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <img
        src="{background_image}"
        alt="Background"
        class="background-image"
      />

      {first_line}

      {second_line}

      {source}
    </div>
  </body>
</html>
"""

BODY_TWO_LINE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap");

      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Roboto", sans-serif;
        background-color: black;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 110px;
        filter: brightness(0) invert(1);
        z-index: 2;
      }}

      /* --- Text Layout --- */

      .body-copy-1 {{
        position: absolute;
        top: 25%;
        left: 43%;
        color: white;
        font-size: 60px;
        font-weight: 600;
        line-height: 1.3;
        text-align: right;
        z-index: 2;
        width: 50%;
      }}

      .body-copy-2 {{       
        position: absolute;
        bottom: 350px;
        left: 120px;
        color: white;
        font-size: 45px;
        width: 50%;
        font-weight: 400;
        line-height: 1;
        text-align: left;
        z-index: 2;
      }}

      .yellow {{
        color: #e9dc01;
      }}

      .source {{
        position: absolute;
        bottom: 60px;
        left: 70px;
        color: white;
        font-size: 35px;
        font-weight: 400;
        opacity: 0.8;
        z-index: 2;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      {first_line}

      {second_line}

      {source}
    </div>
  </body>
</html>
"""

BODY_ONE_LINE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap");

      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Roboto", sans-serif;
        background-color: black;
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
        object-fit: {crop_type};
        object-position: center 25%;
        display: block;
      }}

      .top-left-gradient {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(
          circle at 0% 0%,
          rgba(0, 0, 0, 0.7) 0%,
          rgba(0, 0, 0, 0) 30%
        );
        z-index: 0;
        pointer-events: none;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 110px;
        filter: brightness(0) invert(1);
        z-index: 2;
      }}

      /* --- Text Styling to Match Reference --- */
      .body-copy {{
        position: absolute;
        bottom: 130px;
        left: 70px;
        color: white;
        font-size: 55px;
        font-weight: 500;
        line-height: 1.3;
        width: 80%;
        text-align: left;
        z-index: 2;
      }}

      .yellow {{        
        color: #e9dc01;
        font-weight: 600;
      }}

      .source {{
        position: absolute;
        bottom: 55px;
        left: 70px;
        color: white;
        font-size: 37px;
        font-weight: 400;
        opacity: 0.7;
        z-index: 2;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <div class="top-left-gradient"></div>
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <img
        src="{background_image}"
        alt="Background"
        class="background-image"
      />

      {first_line}
      {source}
    </div>
  </body>
</html>
"""

BODY_ONE_LINE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap");

      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Roboto", sans-serif;
        background-color: black;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 110px;
        filter: brightness(0) invert(1);
        z-index: 2;
      }}

      /* --- Text Styling to Match Reference --- */
      .body-copy {{
        position: absolute;
        bottom: 130px;
        left: 70px;
        color: white;
        font-size: 55px;
        font-weight: 500;
        line-height: 1.3;
        width: 80%;
        text-align: left;
        z-index: 2;
      }}

      .yellow {{        
        color: #e9dc01;
        font-weight: 600;
      }}

      .source {{
        position: absolute;
        bottom: 55px;
        left: 70px;
        color: white;
        font-size: 37px;
        font-weight: 400;
        opacity: 0.7;
        z-index: 2;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <img src="{logo_image}" alt="SW Logo" class="logo" />

      {first_line}
      {source}
    </div>
  </body>
</html>
"""



body_template = {
    "page_name": "scoopwhoop",
    "template_type": "body_template",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "body_two_line_slide": {
            "html_template": BODY_TWO_LINE_TEMPLATE,
            "overlay_template": BODY_TWO_LINE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                "first_line": {"type": "text_area", "tag": "div", "class": "body-copy-1"},
                "second_line": {"type": "text_area", "tag": "div", "class": "body-copy-2"},
                "source": {"type": "text", "tag": "div", "class": "source"},
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"type": "dropdown", "values": ["logo.png"], "default": "logo.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
                "offset": {"type":"default", "values": 75},
                "add_gradient": {"type":"default", "values": False}
            }
        },
        "body_one_line_slide": {
            "html_template": BODY_ONE_LINE_TEMPLATE,
            "overlay_template": BODY_ONE_LINE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                "first_line": {"type": "text_area", "tag": "div", "class": "body-copy"},
                "source": {"type": "text", "tag": "div", "class": "source"},
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"type": "dropdown", "values": ["logo.png"], "default": "logo.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
                "offset": {"type":"default", "values": -50},
                "add_gradient": {"type":"default", "values": False}
            }
        },
    },
}
