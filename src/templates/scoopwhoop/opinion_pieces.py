TEMPLATE_DESCRIPTION = """
**Template Name:** SW Opinion Piece – Center Impact Headline

**Primary Goal:** Recreate the reference hero card (1080×1350) with a background image, SW logo at top-left, and a centered 3-line stack: a short white lead-in on top, a big yellow UPPERCASE impact line in the middle, and a brief white sub-heading below. A blue author pill appears at the bottom-center. Output a single-slide JSON with `image_description`, `first_line`, `highlight`, `sub_heading`, and `by_line`.

**General Instructions:**
*   Follow the provided HTML tags and class names exactly.
*   Keep copy concise and scannable; no line breaks inside fields.
*   `first_line`: 3–7 words; sentence/title case; can include a comma.
*   `highlight`: 2–4 words; ALL CAPS preferred; strong, punchy phrasing.
*   `sub_heading`: one simple sentence (~8–14 words); sentence case; no emojis/hashtags.
*   `by_line`: author name only (no "By"); Title Case; 2–4 words.
*   `image_description`: one clear line describing subject, mood and style (e.g., "poster-style film still on light background, clean center composition").
*   Ensure the copy remains readable over the image; avoid overly long words.
"""

JSON_DESCRIPTION = """
### Slide / Section Definitions

**1. Opinion Piece Hero**
*   **Purpose:** Center-aligned 3-line headline stack with author pill, mirroring the provided reference.

### Attributes:
*   **`image_description`:** One line describing the desired background visual and mood/style.
*   **`first_line`:** 3–7 words; sentence/title case; no special formatting.
*   **`highlight`:** 2–4 words; preferably ALL CAPS; no quotes/emojis.
*   **`sub_heading`:** One short sentence (~8–14 words); sentence case.
*   **`by_line`:** Author name only (no prefixes like "By"); Title Case; 2–4 words.

### Text Input Structure:
    {{
      "name": "opinion_pieces_slide",
      "image_description": "str",
      "text": {{
        "first_line": "str",
        "highlight": "str",
        "sub_heading": "str",
        "by_line": "str"
      }}
    }}
"""


OPINION_PIECES_TEMPLATE = """
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

      .text-content {{
        /* display: inline-block; */
        /* text-align: center; */
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
        line-height: 1.2;
        font-family: "Roboto";
        display: block;
        transform: scaleY(0.9);
        margin-bottom: 10px;
      }}

      .highlight {{
        color: #e9dc01;
        padding: 0px 0px 5px 0px;
        font-size: 110px;
        display: block;
        line-height: 0.8;
        transform: scaleY(1);
        font-family: "Roboto";
        font-weight: 600;
      }}

      .yellow {{
        color: #e9dc01;
      }}
      .sub-heading-container {{
        display: flex;
        justify-content: flex-end;
        margin-top: 25px;
      }}
      .by-line {{
        background-color: #0a4e9a;
        color: white;
        font-family: "Roboto", sans-serif;
        font-weight: 500;
        font-size: 30px;
        padding: 8px 20px;
        letter-spacing: 1px;
        line-height: 1;
        display: inline-block;
        position: absolute;
        bottom: 40px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 2;
      }}    
      .sub-heading {{
        font-size: 30px;
        font-weight: 400;
        line-height: 1.2;
        font-family: "Roboto";
        display: block;
        transform: scaleY(1.1);
        letter-spacing: 1px;
        margin-top: 15px;
      }}
    </style>
    <body>
      <div class="container">
        <div class="top-left-gradient"></div>
        <img src="{logo_image}" alt="SW Logo" class="logo" />
        <img src="{background_image}" class="background-image" />
        <div class="text-overlay">
          <div class="text-content">
            {first_line}
            {highlight}
            {sub_heading}
          </div>
        </div>  
        {by_line}
      </div>
    </body>
  </head>
</html>
"""

OPINION_PIECES_TEMPLATE_OVERLAY = """
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

      .text-content {{
        /* display: inline-block; */
        /* text-align: center; */
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
        line-height: 1.2;
        font-family: "Roboto";
        display: block;
        transform: scaleY(0.9);
        margin-bottom: 10px;
      }}    

      .highlight {{
        color: #e9dc01;
        padding: 0px 0px 5px 0px;
        font-size: 110px;
        display: block;
        line-height: 0.8;
        transform: scaleY(1);
        font-family: "Roboto";
        font-weight: 600;
      }}

      .yellow {{
        color: #e9dc01;
      }}
      .sub-heading-container {{
        display: flex;
        justify-content: flex-end;
        margin-top: 25px;
      }}
      .by-line {{
        background-color: #0a4e9a;
        color: white;
        font-family: "Roboto", sans-serif;
        font-weight: 500;
        font-size: 30px;
        padding: 8px 20px;
        letter-spacing: 1px;
        line-height: 1;
        display: inline-block;
        position: absolute;
        bottom: 40px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 2;
      }}
      .sub-heading {{
        font-size: 30px;
        font-weight: 400;
        line-height: 1.2;
        font-family: "Roboto";
        display: block;
        transform: scaleY(1.1);
        letter-spacing: 1px;
        margin-top: 15px;
      }}
    </style>
    <body>
      <div class="container">
        <img src="{logo_image}" alt="SW Logo" class="logo" />
        <div class="text-overlay">
          <div class="text-content">
            {first_line}
            {highlight}
            {sub_heading}
          </div>
        </div>  
        {by_line}
      </div>
    </body>
  </head>
</html>

"""

opinion_pieces_template = {
    "page_name": "scoopwhoop",
    "template_type": "opinion_pieces",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "opinion_pieces_slide": {
            "html_template": OPINION_PIECES_TEMPLATE,
            "overlay_template": OPINION_PIECES_TEMPLATE_OVERLAY,
            "text_only": False,
            "text": {
                    "first_line": {"type": "text", "tag": "div", "class": "first-line"},
                    "highlight": {"type": "text", "tag": "div", "class": "highlight"},
                    "sub_heading": {
                        "type": "text_area",
                        "tag": "div",
                        "class": "sub-heading",
                    },
                    "by_line": {"type": "text", "tag": "div", "class": "by-line"},
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