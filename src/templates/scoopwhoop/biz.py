TEMPLATE_DESCRIPTION = """
**Template Name:** Biz/Showbiz – Blue Pill Headline

**Primary Goal:** Build a single hero card (1080×1350) like the reference: SW Showbiz logo at the top-left; bottom-left text stack with a small white lead-in, a bold WHITE UPPERCASE headline inside a BLUE pill with a YELLOW offset block behind it, and a short YELLOW kicker line underneath. Output a single-slide JSON with `image_description`, `first_line`, `highlight`, and `sub_heading`.

**General Instructions:**
*   Follow the provided HTML tags and class names exactly.
*   Keep copy tight and skimmable; no manual line breaks.
*   `first_line`: 3–6 words; sentence/title case.
*   `highlight`: 2–4 words; ALL CAPS preferred; punchy news-style phrase.
*   `sub_heading`: short kicker (~6–12 words); sentence case; no emojis/hashtags.
*   `image_description`: one line describing background subject, mood and style.
*   Ensure readability over the image; avoid overly long words.
"""

JSON_DESCRIPTION = """
### Slide / Section Definitions

**1. Biz/Showbiz Hero**
*   **Purpose:** Bottom-left aligned stack with blue-pill headline and yellow kicker.

### Attributes:
*   **`image_description`:** One line describing the desired background visual and mood/style.
*   **`first_line`:** 3–6 words; sentence/title case; plain text only.
*   **`highlight`:** 2–4 words; ALL CAPS preferred; plain text only.
*   **`sub_heading`:** Short kicker (~6–12 words); sentence case; plain text only.

### Text Input Structure:
    {{
      "name": "biz_slide",
      "image_description": "str",
      "text": {{
        "first_line": "str",
        "highlight": "str",
        "sub_heading": "str"
      }}
    }}
"""


BIZ_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap");

      @font-face {{
        font-family: "Cook Conthic";
        src: url("cookconthic.otf") format("opentype");
      }}

      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        background-color: black;
        font-family: "Cook Conthic", sans-serif;
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
        inset: 0;
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

      .text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        padding: 220px 0px 40px 40px;
        background: radial-gradient(
          90% 100% at 50% 100%,
          rgba(0, 0, 0, 1) 0%,
          rgba(0, 0, 0, 0.95) 40%,
          rgba(0, 0, 0, 0.9) 60%,
          rgba(0, 0, 0, 0) 100%
        );
        color: white;
        z-index: 1;
        width: 100%;
      }}

      .first-line {{
        font-size: 54px;
        font-weight: 500;
        font-family: "Roboto", sans-serif;
        line-height: 1;
        letter-spacing: 1.5px;
        transform: scaleY(1);
        margin-bottom: 5px;
        padding-left: 5px;
        width: 90%;
      }}

      .highlight-container {{
        position: relative;
        display: inline-block;
        margin-bottom: 25px;
        width: inherit;
        height: 75px;
      }}

      .highlight-background,
      .highlight-text {{
        font-size: 100px;
        font-weight: 600;
        font-family: "Roboto";
        line-height: 0.8;
        letter-spacing: 0px;
        padding: 10px 25px 10px 10px;
        display: inline-block;
      }}

      .highlight-background {{
        position: absolute;
        top: 8px;
        left: -4px;
        background-color: #e9dc01;
        color: transparent;
        z-index: 0;
      }}    

      .highlight-text {{
        position: absolute; /* ✅ relative instead of absolute */
        background-color: #0a4e9a;
        color: white;
        display: inline-block;
        z-index: 1;
      }}

      .sub-heading {{
        font-family: "Roboto", sans-serif;
        font-weight: 500;
        font-size: 28px;
        letter-spacing: 1px;
        color: #e9dc01;
        width: inherit;
        margin-top: 15px;
      }}
    </style>
  </head>

  <body>
    <div class="container">
      <div class="top-left-gradient"></div>
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <img src="{background_image}" class="background-image" />

      <div class="text-overlay">
        {first_line}
        <div class="highlight-container">
            <div class="highlight-background"></div>
            {highlight}
        </div>
          {sub_heading}
      </div>
    </div>
  </body>
  <script>
      document.addEventListener("DOMContentLoaded", function () {{
        const highlightContainers = document.querySelectorAll(".highlight-container");

        highlightContainers.forEach((container) => {{
          const text = container.querySelector(".highlight-text");
          const bg = container.querySelector(".highlight-background");
          if (text && bg) {{
            bg.textContent = text.textContent;
          }}
        }});
      }});
    </script>
</html>
"""

BIZ_TEMPLATE_OVERLAY = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap");

      @font-face {{
        font-family: "Cook Conthic";
        src: url("cookconthic.otf") format("opentype");
      }}

      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        background-color: black;
        font-family: "Cook Conthic", sans-serif;
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

      .text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        padding: 220px 0px 40px 40px;
        background: radial-gradient(
          90% 100% at 50% 100%,
          rgba(0, 0, 0, 1) 0%,
          rgba(0, 0, 0, 0.95) 40%,
          rgba(0, 0, 0, 0.9) 60%,
          rgba(0, 0, 0, 0) 100%
        );
        color: white;
        z-index: 1;
        width: 100%;
      }}

      .first-line {{
        font-size: 54px;
        font-weight: 500;
        font-family: "Roboto", sans-serif;
        line-height: 1;
        letter-spacing: 1.5px;
        transform: scaleY(1);
        margin-bottom: 5px;
        padding-left: 5px;
        width: 90%;
      }}

      .highlight-container {{
        position: relative;
        display: inline-block;
        margin-bottom: 25px;
        width: inherit;
        height: 75px;
      }}

      .highlight-background,
      .highlight-text {{
        font-size: 100px;
        font-weight: 600;
        font-family: "Roboto";
        line-height: 0.8;
        letter-spacing: 0px;
        padding: 10px 25px 10px 10px;
        display: inline-block;
      }}

      .highlight-background {{
        position: absolute;
        top: 8px;
        left: -4px;
        background-color: #e9dc01;
        color: transparent;
        z-index: 0;
      }}    

      .highlight-text {{
        position: absolute; /* ✅ relative instead of absolute */
        background-color: #0a4e9a;
        color: white;
        display: inline-block;
        z-index: 1;
      }}

      .sub-heading {{
        font-family: "Roboto", sans-serif;
        font-weight: 500;
        font-size: 28px;
        letter-spacing: 1px;
        color: #e9dc01;
        width: inherit;
        margin-top: 15px;
      }}
    </style>
  </head>

  <body>
    <div class="container">
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <div class="text-overlay">
        {first_line}
        <div class="highlight-container">
            <div class="highlight-background"></div>
            {highlight}
        </div>
          {sub_heading}
      </div>
    </div>
  </body>
  <script>
      document.addEventListener("DOMContentLoaded", function () {{
        const highlightContainers = document.querySelectorAll(".highlight-container");

        highlightContainers.forEach((container) => {{
          const text = container.querySelector(".highlight-text");
          const bg = container.querySelector(".highlight-background");
          if (text && bg) {{
            bg.textContent = text.textContent;
          }}
        }});
      }});
    </script>
</html>
"""

biz_template = {
    "page_name": "scoopwhoop",
    "template_type": "biz",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "biz_slide": {
            "html_template": BIZ_TEMPLATE,
            "overlay_template": BIZ_TEMPLATE_OVERLAY,
            "text_only": False,
            "text": {
                    "first_line": {"type": "text_area", "tag": "div", "class": "first-line"},
                    "highlight": {"type": "text", "tag": "div", "class": "highlight-text"},
                    "sub_heading": {
                        "type": "text_area",
                        "tag": "div",
                        "class": "sub-heading",
                    },
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"type": "dropdown", "values": ["logo.png"], "default": "logo.png"},
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