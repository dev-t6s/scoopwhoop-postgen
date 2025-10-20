TEMPLATE_DESCRIPTION = """
**Template Name:** SW Ranking – Number Badge Hero

**Primary Goal:** Create a single hero card (1080×1350) with a background image, SW logo at top-left, and an angled number badge at the top-right. The lower area shows a bottom-left text stack: a large yellow Header and a short white body line beneath it. Output a single-slide JSON with `image_description` and the text fields: `number`, `highlight`, and `sub_heading`.

**General Instructions:**
*   Use the exact HTML tags and class names provided.
*   Keep copy concise; do not insert manual line breaks.
*   `number`: 1–2 digits (1–99); numeric string only; no suffixes.
*   `highlight`: 1–4 words; Title Case or ALL CAPS; punchy and short.
*   `sub_heading`: brief kicker (~4–12 words); sentence case; no emojis/hashtags.
*   `image_description`: one clear line describing subject, mood, and style.
*   Ensure text remains readable over the image and fits the layout.
"""

JSON_DESCRIPTION = """
### Slide / Section Definitions

**1. Ranking Hero**
*   **Purpose:** Ranking card with angled number badge (top-right) and bottom-left headline + body text.

### Attributes:
*   **`image_description`:** One line describing the desired background visual and mood/style.
*   **`number`:** 1–2 digits (1–99); numeric string; no symbols.
*   **`highlight`:** 1–4 words; Title Case or ALL CAPS; no quotes/emojis.
*   **`sub_heading`:** Short sentence (~4–12 words); sentence case.

### Text Input Structure:
    {{
      "name": "ranking_slide",
      "image_description": "str",
      "text": {{
        "number": "str",
        "highlight": "str",
        "sub_heading": "str"
      }}
    }}
"""


RANKING_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap");
      @font-face {{
        font-family: "Cook Conthic";
        src: url("cookconthic.otf") format("opentype");
        font-weight: normal;
        font-style: normal;
      }}

      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Cook Conthic", sans-serif;
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
        display: block;
        object-fit: {crop_type};
        object-position: center 25%;
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

      /* === ANGLED NUMBER CONTAINER === */
      .number-container {{          
        position: absolute;
        top: 45px;
        right: 40px;
        width: 100px;
        height: 110px;
        z-index: 3;
        transform: skewY(-15deg); /* creates the angled effect */
      }}

      .number-box {{
        position: relative;
        width: 100%;
        height: 100%;
        background: #0046b3; /* blue front face */
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: "Cook Conthic", sans-serif;
        font-weight: 500;
        font-size: 90px;
        color: white;
      }}

      /* yellow background "shadow" layer */
      .number-container::after {{
        content: "1";
        position: absolute;
        bottom: -10px;
        right: -7px;
        width: 100px;
        height: 110px;
        background: #e9dc01; /* yellow accent */
        z-index: -1;
        transform: skewY(-2deg);
      }}

      .text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 220px 40px 150px 40px;
        color: white;
        text-align: center;

        background: radial-gradient(
          90% 100% at 50% 100%,
          rgba(0, 0, 0, 1) 0%,
          rgba(0, 0, 0, 0.95) 40%,
          rgba(0, 0, 0, 0.9) 60%,
          rgba(0, 0, 0, 0) 100%
        );
      }}        

      .sub-heading {{
        font-size: 35px;
        font-weight: 500;
        line-height: 1.2;
        font-family: "Roboto";
        display: block;
        transform: scaleY(1);
        margin-top: 15px;
      }}

      .highlight {{
        color: #e9dc01;
        padding: 0px 0px 5px 0px;
        font-size: 110px;
        display: block;
        line-height: 0.8;
        transform: scaleY(1);
        font-family: "Roboto";
        font-weight: 500;
      }}

      .yellow {{
        color: #e9dc01;
      }}    
    </style>
  </head>

  <body>
    <div class="container">
      <div class="top-left-gradient"></div>
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <!-- angled number box -->
      <div class="number-container">
        {number}
      </div>
      <img src="{background_image}" class="background-image" />
      <div class="text-overlay">
        <div class="text-content">
          {highlight}
          {sub_heading}
        </div>
      </div>
    </div>
  </body>
</html>
"""

RANKING_TEMPLATE_OVERLAY = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap");
      @font-face {{
        font-family: "Cook Conthic";
        src: url("cookconthic.otf") format("opentype");
        font-weight: normal;
        font-style: normal;
      }}

      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Cook Conthic", sans-serif;
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

      /* === ANGLED NUMBER CONTAINER === */
      .number-container {{          
        position: absolute;
        top: 45px;
        right: 40px;
        width: 100px;
        height: 110px;
        z-index: 3;
        transform: skewY(-15deg); /* creates the angled effect */
      }}

      .number-box {{
        position: relative;
        width: 100%;
        height: 100%;
        background: #0046b3; /* blue front face */
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: "Cook Conthic", sans-serif;
        font-weight: 500;
        font-size: 90px;
        color: white;
      }}

      /* yellow background "shadow" layer */
      .number-container::after {{
        content: "1";
        position: absolute;
        bottom: -10px;
        right: -7px;
        width: 100px;
        height: 110px;
        background: #e9dc01; /* yellow accent */
        z-index: -1;
        transform: skewY(-2deg);
      }}

      .text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 220px 40px 150px 40px;
        color: white;
        text-align: center;

        background: radial-gradient(
          90% 100% at 50% 100%,
          rgba(0, 0, 0, 1) 0%,
          rgba(0, 0, 0, 0.95) 40%,
          rgba(0, 0, 0, 0.9) 60%,
          rgba(0, 0, 0, 0) 100%
        );
      }}        

      .sub-heading {{
        font-size: 35px;
        font-weight: 500;
        line-height: 1.2;
        font-family: "Roboto";
        display: block;
        transform: scaleY(1);
        margin-top: 15px;
      }}

      .highlight {{
        color: #e9dc01;
        padding: 0px 0px 5px 0px;
        font-size: 110px;
        display: block;
        line-height: 0.8;
        transform: scaleY(1);
        font-family: "Roboto";
        font-weight: 500;
      }}

      .yellow {{
        color: #e9dc01;
      }}    
    </style>
  </head>

  <body>
    <div class="container">
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <!-- angled number box -->
      <div class="number-container">
        {number}
      </div>
      <div class="text-overlay">
        <div class="text-content">
          {highlight}
          {sub_heading}
        </div>
      </div>
    </div>
  </body>
</html>
"""

ranking_template = {
    "page_name": "scoopwhoop",
    "template_type": "ranking",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "ranking_slide": {
            "html_template": RANKING_TEMPLATE,
            "overlay_template": RANKING_TEMPLATE_OVERLAY,
            "text_only": False,
            "text": {
                    "number": {"type": "text", "tag": "div", "class": "number-box"},
                    "highlight": {"type": "text", "tag": "div", "class": "highlight"},
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