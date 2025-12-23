TEMPLATE_DESCRIPTION = """
Static Carousel: This BWS (Bharatiya Web Series) template creates engaging carousel slides for social media posts about Indian web series, OTT content, streaming shows, and digital entertainment. It features a full-screen background image with bold centered text overlay using yellow highlighting capabilities. The design includes the "bharatiyawebseries" watermark at the top and uses heavy typography with strong stroke and shadow effects for maximum impact. Perfect for promoting web series content, character introductions, show highlights, and OTT entertainment news.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Static Carousel Slide:
  ### Attributes:
  - This should be an engaging content slide for web series and OTT content. Must have compelling visual and text.
    EX: A still from a popular web series, a character poster, an actor from an OTT show, a dramatic scene from a series.
  
  - image_description: A one line description of the image you would like to use for the slide.
    EX: "A dramatic scene from Sacred Games", "Actor Pankaj Tripathi in Mirzapur", "A poster of The Family Man"
  
  - headline: The main headline content. Use **str** for yellow highlighting on important words and \\n for line breaks.
    EX: "When **Kaleen Bhaiya** enters the scene", "**Mirzapur Season 3** is finally here!", "This **web series** deserves more hype"
    Note: Use plain text with **str** for yellow highlighting.

  ### Text Input:
    {{
      "name": "static_carousel_slide",
      "image_description": "str",
      "text": {{
      "headline": "str"
      }}
    }}

NOTE: 
- Use **str** to highlight words in yellow and make the headline more engaging. Use \\n for line breaks.
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
- Focus on creating engaging, shareable content about Indian web series, OTT platforms, and streaming entertainment.
- Content works best with web series references, character moments, show recommendations, and OTT content discussions.
"""

STATIC_CAROUSEL_SLIDE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title></title>
    <style>
      /* Antonio is a naturally condensed (upright) font, perfect for this style */
      @import url("https://fonts.googleapis.com/css2?family=Antonio:wght@700&display=swap");

      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: sans-serif;
        background-color: #333;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
        background-color: #000;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        display: block;
        object-fit: {crop_type};
        object-position: center 20%;
      }}

      .watermark {{
        position: absolute;
        top: 60px;
        width: 100%;
        text-align: center;
        font-family: "Poppins", sans-serif;
        font-size: 32px;
        font-weight: 600;
        color: rgba(255, 255, 255, 0.6);
        z-index: 10;
        letter-spacing: 1px;
      }}

      .text-overlay {{
        position: absolute;
        /* Aligned with the bike tank area */
        top: 72%;
        left: 0;
        right: 0;
        display: flex;
        flex-direction: column;
        z-index: 20;
      }}

      .text-content {{
        width: 95%;
        align-self: center;
        text-align: center;
      }}

      .text-content h1 {{
        margin: 0;
        /* Using Antonio for the naturally tall/upright look */
        font-family: "Antonio", sans-serif;
        font-size: 60px; /* Increased size since the font is narrow */
        font-weight: 700; /* Bold */
        color: white;

        /* Removed the transform:scaleY since this font is naturally upright */

        /* Heavy Stroke and Shadow */
        -webkit-text-stroke: 6px black;
        paint-order: stroke fill;
        text-shadow: 4px 4px 0px #000000;

        line-height: 1.1;
        letter-spacing: 0.2px;
      }}

      .text-content h1 .yellow {{
        color: #fff200;
        -webkit-text-stroke: 3px black;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <div class="watermark">bharatiyawebseries</div>

      <img src="{background_image}" class="background-image" alt="Background" />

      <div class="text-overlay">
        <div class="text-content">
          {headline}
        </div>
      </div>
    </div>
  </body>
</html>
"""

STATIC_CAROUSEL_SLIDE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title></title>
    <style>
      /* Antonio is a naturally condensed (upright) font, perfect for this style */
      @import url("https://fonts.googleapis.com/css2?family=Antonio:wght@700&display=swap");

      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: sans-serif;
        background-color: #000000;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
        background-color: #000;
      }}

      .watermark {{
        position: absolute;
        top: 60px;
        width: 100%;
        text-align: center;
        font-family: "Poppins", sans-serif;
        font-size: 32px;
        font-weight: 600;
        color: rgb(135, 130, 130);
        z-index: 10;
        letter-spacing: 1px;
      }}

      .text-overlay {{
        position: absolute;
        /* Aligned with the bike tank area */
        top: 72%;
        left: 0;
        right: 0;
        display: flex;
        flex-direction: column;
        z-index: 20;
      }}

      .text-content {{
        width: 95%;
        align-self: center;
        text-align: center;
      }}

      .text-content h1 {{
        margin: 0;
        /* Using Antonio for the naturally tall/upright look */
        font-family: "Antonio", sans-serif;
        font-size: 60px; /* Increased size since the font is narrow */
        font-weight: 700; /* Bold */
        color: white;

        /* Removed the transform:scaleY since this font is naturally upright */

        /* Heavy Stroke and Shadow */
        -webkit-text-stroke: 6px black;
        paint-order: stroke fill;
        text-shadow: 4px 4px 0px #000000;

        line-height: 1.1;
        letter-spacing: 0.2px;
      }}

      .text-content h1 .yellow {{
        color: #fff200;
        -webkit-text-stroke: 3px black;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <div class="watermark">bharatiyawebseries</div>

      <div class="text-overlay">
        <div class="text-content">
          {headline}
        </div>
      </div>
    </div>
  </body>
</html>
"""

static_carousel_template = {
    "page_name": "bws",
    "template_type": "carousel",
    "text_template": {
        "template_description": TEMPLATE_DESCRIPTION,
        "json_description": JSON_DESCRIPTION
    },
    "slides": {
        "static_carousel_slide": {
            "html_template": STATIC_CAROUSEL_SLIDE_HTML_TEMPLATE,
            "overlay_template": STATIC_CAROUSEL_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "h1", "class": ""}
                },
            "assets":{
                "background_image": {"type":"bytes", "file_type":"png"},
                "background_video": {"type":"bytes", "file_type":"mp4"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
                "add_gradient": {"type":"default", "values": False},
                "offset": {"type":"default", "values": 0},
            }
        }
    }
}
