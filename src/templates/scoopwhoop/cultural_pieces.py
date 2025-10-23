TEMPLATE_DESCRIPTION = """
**Template Name:** Impact Word Headline

**Primary Goal:** Create a single hero card (1080×1350) featuring a strong background image and a bold impact word as the focal point. The output must be a single-slide JSON with `image_description` and three text fields: `first_line`, `highlight`, and `sub_heading`.

**General Instructions:**
*   Adhere strictly to the provided HTML tags and class names.
*   Keep text extremely concise and skimmable.
*   `first_line`: short lead-in of 3–4 words max; sentence/title case.
*   `highlight`: the big impact word/phrase, 3–4 words max; prefer UPPERCASE wording.
*   `sub_heading`: optional one-line subtitle in sentence case (about 8–10 words max).
*   `image_description`: one clear line describing background subject, mood and style for an image generator.
*   Ensure copy fits the layout and remains readable over the image.
"""

JSON_DESCRIPTION = """
### Slide / Section Definitions

**1. Impact Word Headline**
*   **Purpose:** A single-slide hero card with a bold impact word, a short lead-in, and an optional one-line subtitle.

### Attributes:
*   **`image_description`:** One line describing the desired background visual and mood/style (e.g., "cinematic portrait with dramatic rim light", "stadium crowd under spotlights").
*   **`first_line`:** Lead-in text of no more than 3–4 words; sentence/title case; plain text only.
*   **`highlight`:** Emphasized word/phrase; no more than 3–4 words; prefer strong UPPERCASE wording.
*   **`sub_heading`:** Optional single line in sentence case; keep within ~8–10 words; plain text only.

### Text Input Structure:
    {{
      "name": "cultural_pieces_slide",
      "image_description": "str",
      "text": {{
        "first_line": "str",
        "highlight": "str",
        "sub_heading": "str"
      }}
    }}
"""


CULTURAL_PIECES_TEMPLATE = """
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
        /* 'cover' scales the image to fill the container, cropping sides or top/bottom as needed */
        object-fit: {crop_type};
        /* Aligns the image. 'center' horizontally, and 25% from the top vertically to shift it up. */
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
        width: 110px; /* Increased logo size */
        filter: brightness(0) invert(1);
      }}

      .text-overlay {{      
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 220px 40px 70px 40px;
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

      .text-content {{
        display: inline-block;
        text-align: center;
      }}
      .first-line-container {{
        display: flex;
        justify-content: flex-start;
        padding: 0px 5px;
        letter-spacing: 1px;
      }}

      .first-line {{
        font-size: 55px;
        font-weight: 400;
        line-height: 0.9;
        font-family: "Roboto";
        display: block;
        text-align: left;
      }}

      .highlight {{
        color: #e9dc01;
        padding: 0px 0px 5px 0px;
        font-size: 160px;
        display: inline-block;
        font-weight: 500;
        line-height: 0.9;
        font-family: "Cook Conthic";
      }}

      .yellow {{
        color: #e9dc01;
      }}
      .sub-heading-container {{
        display: flex;
        justify-content: flex-end;
        margin-top: 25px;
      }}
      .sub-heading {{
        background-color: #0a4e9a;
        color: white;
        font-family: "Roboto", sans-serif;
        font-weight: 400;
        font-size: 30px;
        padding: 8px 15px;
        letter-spacing: 1px;
        margin-top: 0px;
        display: inline-block;
      }}
    </style>
    <body>
      <div class="container">
        <div class="top-left-gradient"></div>
        <img src="{logo_image}" alt="SW Logo" class="logo" />
        <img src="{background_image}" class="background-image" />
        <div class="text-overlay">
          <div class="text-content">
            <div class="first-line-container">
              {first_line}
            </div>
            {highlight}
            <div class="sub-heading-container">
              {sub_heading}
            </div>
          </div>
        </div>
      </div>
    </body>
  </head>
</html>
"""

CULTURAL_PIECES_TEMPLATE_OVERLAY = """
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
        width: 110px; /* Increased logo size */
        filter: brightness(0) invert(1);
      }}

      .text-overlay {{      
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 220px 40px 70px 40px;
        color: white;
        text-align: center;
      }}

      .text-content {{
        display: inline-block;
        text-align: center;
      }}
      .first-line-container {{
        display: flex;
        justify-content: flex-start;
        padding: 0px 5px;
        letter-spacing: 1px;
      }}

      .first-line {{
        font-size: 55px;
        font-weight: 400;
        line-height: 0.9;
        font-family: "Roboto";
        display: block;
        text-align: left;
      }}

      .highlight {{
        color: #e9dc01;
        padding: 0px 0px 5px 0px;
        font-size: 160px;
        display: inline-block;
        font-weight: 500;
        line-height: 0.9;
        font-family: "Cook Conthic";
      }}

      .yellow {{
        color: #e9dc01;
      }}
      .sub-heading-container {{
        display: flex;
        justify-content: flex-end;
        margin-top: 25px;
      }}
      .sub-heading {{
        background-color: #0a4e9a;
        color: white;
        font-family: "Roboto", sans-serif;
        font-weight: 400;
        font-size: 30px;
        padding: 8px 15px;
        letter-spacing: 1px;
        margin-top: 0px;
        display: inline-block;
      }}
    </style>
    <body>
      <div class="container">
        <img src="{logo_image}" alt="SW Logo" class="logo" />
        <div class="text-overlay">
          <div class="text-content">
            <div class="first-line-container">
              {first_line}
            </div>
            {highlight}
            <div class="sub-heading-container">
              {sub_heading}
            </div>
          </div>
        </div>
      </div>
    </body>
  </head>
</html>
"""

cultural_pieces_template = {
    "page_name": "scoopwhoop",
    "template_type": "cultural_pieces",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "cultural_pieces_slide": {
            "html_template": CULTURAL_PIECES_TEMPLATE,
            "overlay_template": CULTURAL_PIECES_TEMPLATE_OVERLAY,
            "text_only": False,
            "text": {
                    "first_line": {"type": "text", "tag": "div", "class": "first-line"},
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
                "logo_image": {"type": "dropdown", "values": ["logo.png","logo_original.png", "logo_hottake.png"], "default": "logo.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
                "add_top_left_gradient": {"type":"checkbox", "html_snippet": '<div class="top-left-gradient"></div>'},
            }
        },
    },
}