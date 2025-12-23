TEMPLATE_DESCRIPTION = """
Post: This BWS (Bharatiya Web Series) template creates engaging post slides for social media posts about Indian web series, OTT content, streaming shows, and digital entertainment. It features a full-screen background image with bold centered text overlay using yellow highlighting capabilities. The design includes the "bharatiyawebseries" watermark at the top and uses heavy typography with strong stroke and shadow effects for maximum impact. Perfect for promoting web series content, character introductions, show highlights, and OTT entertainment news.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Post Slide:
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
      "name": "post_slide",
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

POST_TEMPLATE_HTML = """
<!DOCTYPE html>
<html>
  <head>
    <title>Infomance - Meme Style</title>
    <style>
      /* Load Anton Font for the classic thick meme look */
      @import url("https://fonts.googleapis.com/css2?family=Anton&display=swap");
      /* Load Roboto for the watermark */
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap");

      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: "Anton", sans-serif;
        display: flex;
        justify-content: center;
        min-height: 100vh;
        background-color: white;
      }}

      .container {{
        width: 1080px;
        height: 1350px; /* 4:5 Aspect Ratio */
        background-color: #000000;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: flex-end; /* Align content to bottom */
        align-items: center;
      }}

      /* Video Layer - Full Background */
      .main-image {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: {crop_type};
        z-index: 1; /* Sits behind text */
      }}

      /* Text Wrapper - Positioned at bottom */
      .content-wrapper {{
        position: relative;
        z-index: 10; /* Sits above video */
        width: 100%;
        padding-bottom: 80px; /* Space from bottom edge */
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
      }}

      /* Meme Text Styling */
      .meme-text {{
        font-family: "Anton", sans-serif;
        font-size: 75px;
        color: #ffffff;
        text-transform: uppercase; /* Ensures that punchy look */
        line-height: 1.1;
        letter-spacing: 1px;
        margin: 0;
        padding: 0 40px;

        /* Strong Black Outline Effect */
        -webkit-text-stroke: 3px black;
        text-shadow: 3px 3px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000,
          -1px 1px 0 #000, 1px 1px 0 #000;
      }}

      /* Highlight Color */
      .yellow {{
        color: #ffd700; /* Gold/Yellow */
      }}

      /* Watermark Styling */
      .watermark {{ 
        font-family: "Roboto", sans-serif;
        font-weight: 500;
        font-size: 30px;
        color: #c0bfbf; /* Solid Gray */
        margin-top: 15px;
        text-transform: none;

        /* No outline for watermark, just clean gray text */
        text-shadow: none;
        -webkit-text-stroke: 0;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Video Background -->
      <img src="{background_image}" class="main-image"></img>

      <!-- Overlay Content -->
      <div class="content-wrapper">
        {headline}

        <div class="watermark">@bhartiyawebseries</div>
      </div>
    </div>
  </body>
</html>
"""

POST_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <title>Infomance - Meme Style</title>
    <style>
      /* Load Anton Font for the classic thick meme look */
      @import url("https://fonts.googleapis.com/css2?family=Anton&display=swap");
      /* Load Roboto for the watermark */
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap");

      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: "Anton", sans-serif;
        display: flex;
        justify-content: center;
        min-height: 100vh;
        background-color: #000000;
      }}

      .container {{
        width: 1080px;
        height: 1350px; /* 4:5 Aspect Ratio */
        background-color: #000000;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: flex-end; /* Align content to bottom */
        align-items: center;
      }}

      /* Text Wrapper - Positioned at bottom */
      .content-wrapper {{
        position: relative;
        z-index: 10; /* Sits above video */
        width: 100%;
        padding-bottom: 80px; /* Space from bottom edge */
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
      }}

      /* Meme Text Styling */
      .meme-text {{
        font-family: "Anton", sans-serif;
        font-size: 75px;
        color: #ffffff;
        text-transform: uppercase; /* Ensures that punchy look */
        line-height: 1.1;
        letter-spacing: 1px;
        margin: 0;
        padding: 0 40px;

        /* Strong Black Outline Effect */
        -webkit-text-stroke: 3px black;
        text-shadow: 3px 3px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000,
          -1px 1px 0 #000, 1px 1px 0 #000;
      }}

      /* Highlight Color */
      .yellow {{
        color: #ffd700; /* Gold/Yellow */
      }}

      /* Watermark Styling */
      .watermark {{ 
        font-family: "Roboto", sans-serif;
        font-weight: 500;
        font-size: 30px;
        color: #c0bfbf; /* Solid Gray */
        margin-top: 15px;
        text-transform: none;

        /* No outline for watermark, just clean gray text */
        text-shadow: none;
        -webkit-text-stroke: 0;
      }}
    </style>
  </head>
  <body>
    <div class="container">

      <!-- Overlay Content -->
      <div class="content-wrapper">
        {headline}

        <div class="watermark">@bhartiyawebseries</div>
      </div>
    </div>
  </body>
</html>
"""

post_template = {
    "page_name": "bws",
    "template_type": "post",
    "text_template": {
        "template_description": TEMPLATE_DESCRIPTION,
        "json_description": JSON_DESCRIPTION
    },
    "slides": {
        "post_slide": {
            "html_template": POST_TEMPLATE_HTML,
            "overlay_template": POST_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "div", "class": "meme-text"}
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
