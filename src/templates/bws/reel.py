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

REEL_TEMPLATE_HTML = """
"""

REEL_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Meme Template</title>
    <style>
      /* Importing Playfair Display to match the editorial Serif look */
      @import url("https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&display=swap");
      /* Importing Poppins for the watermark */
      @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap");

      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: sans-serif;
        background-color: rgba(0,247,34,1);
      }}

      .container {{
        position: relative;
        /* Dimensions */
        width: 1350px;
        height: 1950px;
        margin: auto;
        overflow: hidden;
        background-color: rgba(0,247,34,1);
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        display: block;
        object-fit: cover;
        object-position: center top;
      }}

      .text-overlay {{
        position: absolute;
        /* Positioned in the lower third */
        top: 65%;
        left: 0;
        right: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 20;
      }}

      .text-content {{
        width: 90%;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
      }}

      .text-content h1 {{
        margin: 0;
        font-family: "Playfair Display", serif;
        font-size: 72px;
        font-weight: 700;
        color: white;
        text-transform: capitalize;

        /* Sharp black stroke */
        -webkit-text-stroke: 7px black;
        paint-order: stroke fill;

        /* Soft shadow */
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);

        line-height: 1.3;
      }}

      .text-content h1 .yellow {{       
        color: #ffcc00; /* Gold/Yellow */
        -webkit-text-stroke: 7px black;
      }}

      /* Watermark Styling - Positioned relative to text */
      .watermark {{
        margin-top: 60px; /* Spacing below the main text */
        font-family: "Poppins", sans-serif;
        font-size: 30px;
        font-weight: 500;
        color: #b7b7b7; /* Solid Gray */
        letter-spacing: 1px;
        text-shadow: none;
      }}
    </style>
  </head>
  <body>
    <div class="container">

      <!-- Caption Text & Watermark Container -->
      <div class="text-overlay">
        <div class="text-content">
          {headline}
          <!-- Watermark is now here, directly below the text -->
          <div class="watermark">bharatiyawebseries</div>
        </div>
      </div>
    </div>
  </body>
</html>
"""

reel_template = {
    "page_name": "bws",
    "template_type": "reel",
    "text_template": {
        "template_description": TEMPLATE_DESCRIPTION,
        "json_description": JSON_DESCRIPTION
    },
    "slides": {
        "reel_slide": {
            "html_template": REEL_TEMPLATE_HTML,
            "overlay_template": REEL_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "h1", "class": ""}
                },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
            },
            "image_edits": {
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
                "add_gradient": {"type":"default", "values": False},
                "offset": {"type":"default", "values": 0},
                "green_screen": {"type":"default", "values": (0,247,34,1)},
            }
        }
    }
}
