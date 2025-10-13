TEMPLATE_DESCRIPTION = """
News Carousel: This template creates engaging news carousel posts with one headline slide ("WHAT HAPPENED IN THE LAST 24 HOURS") followed by 4-5 individual news story slides. Each news slide features a relevant background image with bold yellow-highlighted headline text at the bottom.

Example Headline Slide: "WHAT HAPPENED IN THE LAST 24 HOURS" with swipe indicator
Example Content Slides: Background images with news headlines using yellow highlights like "**STARTUP RAISES $50M** in Series B funding"

The source should only be used if the post or the news is not from ScoopWhoop.
NOTE: This template requires 1 headline slide + 4-5 news content slides (total 5-6 slides).
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:

1. Headline Slide (REQUIRED - Only 1):
  ### Attributes:
  - This is the opening slide with FIXED text "WHAT HAPPENED IN THE LAST 24 HOURS" and a swipe indicator.
  - The text is always the same and cannot be changed - it's hardcoded in the template.
  - Only requires a background image description.
  
  - image_description: A one line description of the background image (e.g., "news background", "city skyline", "abstract pattern").
  
  ### Text Input:
    {{
      "name": "headline_slide",
      "image_description": "str"
    }}

2. News Content Slides (REQUIRED - 4 to 5 slides):
  ### Attributes:
  - Each slide presents an individual news story with a relevant background image and headline text.
  
  - image_description: A one line description of the background image that relates to the news story.
  
  - headline: The news headline text. Text wrapped in ** ** appears with yellow highlight, text without ** ** appears in white.
    EX: "**STARTUP RAISES $50M** in Series B funding"
    EX: "**NEW AI TOOL LAUNCHED** by Google for businesses"
    EX: "Indian unicorn **EXPANDS TO 10 NEW CITIES**"
  
  ### Text Input (repeat 4-5 times):
    {{
      "name": "content_slide",
      "image_description": "str",
      "text":{{
        "headline": "str"
      }}
    }}

NOTE: 
- Use **str** to highlight parts of the text in news headlines (this creates the yellow highlight effect).
- Headlines should be concise and attention-grabbing
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
- Total slides should be 5-6 (1 headline + 4-5 news content)
"""

HEADLINE_SLIDE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Instagram Post Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&display=swap"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "Poppins", sans-serif;
        background: #f0f0f0;
        display: flex;
        justify-content: center;
        /* align-items: center; */
        min-height: 100vh;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        object-fit: {crop_type};
        position: absolute;
        top: 0;
        left: 0;
      }}

      /* Gradient overlay */
      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 55%;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.95) 0%,
          rgba(0, 0, 0, 0.85) 15%,
          rgba(0, 0, 0, 0.9) 25%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      /* Text area */
      .text-overlay {{
        position: absolute;
        bottom: 130px;
        left: 35px;
        right: 35px;
        text-align: center;
        z-index: 10;
      }}

      .headline {{
        font-size: 90px;
        font-weight: 600;
        color: #fff;
        line-height: 1.3;
        /* margin-bottom: 20px; */
      }}

      .headline .yellow {{
        display: inline-block;
        height: 75px;
        line-height: 75px;
        background: #fce059; /* Yellow highlight */
        color: #000;
        padding: 0px 40px;
        font-weight: 700;
      }}    

      .subtext {{
        font-size: 24px;
        font-weight: 500;
        color: #ddd;
        line-height: 1.4;
      }}

      /* Logo section */
      .logo-container {{
        position: absolute;
        top: 10px;
        right: 10px;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        z-index: 15;
      }}

      .logo img {{
        height: 110px;
        width: auto;
      }}

      /* Swipe indicator */
      .swipe-indicator {{
        position: absolute;
        bottom: 15px;
        right: 0px;
        z-index: 15;
      }}

      .swipe-indicator img {{
        height: 110px;
        width: auto;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Background -->
      <!-- Logo -->
      <div class="logo-container">
        <div class="logo">
          <img src="logo.png" alt="The Tatva" />
        </div>
      </div>
      <img src="{background_image}" alt="Background" class="background-image" />

      <!-- Gradient Overlay -->
      <div class="gradient-overlay"></div>

      <!-- Text -->
      <div class="text-overlay">
        <div class="headline">
          <div class="box"><span class="yellow">WHAT HAPPENED IN</span></div>
          <div class="box">THE LAST 24 HOURS</div>
        </div>
      </div>

      <!-- Swipe Indicator -->
      <div class="swipe-indicator">
        <img src="swipe.png" alt="Swipe Left" />
      </div>
    </div>
  </body>
</html>
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Instagram Post Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&display=swap"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "Poppins", sans-serif;
        background: rgba(128,128,128,1);
        display: flex;
        justify-content: center;
        /* align-items: center; */
        min-height: 100vh;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
      }}

      /* Gradient overlay */
      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 55%;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.95) 0%,
          rgba(0, 0, 0, 0.85) 15%,
          rgba(0, 0, 0, 0.9) 25%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      /* Text area */
      .text-overlay {{
        position: absolute;
        bottom: 130px;
        left: 35px;
        right: 35px;
        text-align: center;
        z-index: 10;
      }}

      .headline {{
        font-size: 90px;
        font-weight: 600;
        color: #fff;
        line-height: 1.3;
        /* margin-bottom: 20px; */
      }}

      .headline .yellow {{
        display: inline-block;
        height: 75px;
        line-height: 75px;
        background: #fce059; /* Yellow highlight */
        color: #000;
        padding: 0px 40px;
        font-weight: 700;
      }}    

      .subtext {{
        font-size: 24px;
        font-weight: 500;
        color: #ddd;
        line-height: 1.4;
      }}

      /* Logo section */
      .logo-container {{
        position: absolute;
        top: 10px;
        right: 10px;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        z-index: 15;
      }}

      .logo img {{
        height: 110px;
        width: auto;
      }}

      /* Swipe indicator */
      .swipe-indicator {{
        position: absolute;
        bottom: 15px;
        right: 0px;
        z-index: 15;
      }}

      .swipe-indicator img {{
        height: 110px;
        width: auto;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Background -->
      <!-- Logo -->
      <div class="logo-container">
        <div class="logo">
          <img src="logo.png" alt="The Tatva" />
        </div>
      </div>

      <!-- Text -->
      <div class="text-overlay">
        <div class="headline">
          <div class="box"><span class="yellow">WHAT HAPPENED IN</span></div>
          <div class="box">THE LAST 24 HOURS</div>
        </div>
      </div>

      <!-- Swipe Indicator -->
      <div class="swipe-indicator">
        <img src="swipe.png" alt="Swipe Left" />
      </div>
    </div>
  </body>
</html>
"""

CONTENT_SLIDE_HTML_TEMPLATE = """

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Instagram Post Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&display=swap"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "Poppins", sans-serif;
        background: #f0f0f0;
        display: flex;
        justify-content: center;
        /* align-items: center; */
        min-height: 100vh;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        object-fit: {crop_type};
        position: absolute;
        top: 0;
        left: 0;
      }}

      /* Gradient overlay */
      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 55%;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.95) 0%,
          rgba(0, 0, 0, 0.85) 15%,
          rgba(0, 0, 0, 0.9) 25%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      /* Text area */
      .text-overlay {{
        position: absolute;
        top: 1060px;
        left: 35px;
        right: 35px;
        text-align: center;
        z-index: 10;
      }}

      .headline {{
        font-size: 50px;
        font-weight: 600;
        color: #fff;
        line-height: 1.4;
        /* margin-bottom: 20px; */
        /* display: flex;
        flex-direction: column;
        align-items: center; */
      }}

      .headline .yellow {{
        background: #fce059; /* Yellow highlight */
        color: #000;
        padding: 0px 6px;
        border-radius: 3px;
        font-weight: 700;
      }}

      .subtext {{
        font-size: 24px;
        font-weight: 500;
        color: #ddd;
        line-height: 1.4;
      }}

      /* Logo section */
      .logo-container {{
        position: absolute;
        top: 10px;
        right: 10px;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        z-index: 15;
      }}

      .logo img {{
        height: 110px;
        width: auto;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Background -->
      <!-- Logo -->
      <div class="logo-container">
        <div class="logo">
          <img src="logo.png" alt="The Tatva" />
        </div>
      </div>
      <img src="{background_image}" alt="Background" class="background-image" />

      <!-- Gradient Overlay -->
      <div class="gradient-overlay"></div>

      <!-- Text -->
      <div class="text-overlay">
        {headline}
      </div>
    </div>
  </body>
</html>
"""

CONTENT_SLIDE_OVERLAY_TEMPLATE = """

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Instagram Post Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&display=swap"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "Poppins", sans-serif;
        background: rgba(128,128,128,1);
        display: flex;
        justify-content: center;
        /* align-items: center; */
        min-height: 100vh;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
      }}

      /* Gradient overlay */
      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 55%;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.95) 0%,
          rgba(0, 0, 0, 0.85) 15%,
          rgba(0, 0, 0, 0.9) 25%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      /* Text area */
      .text-overlay {{
        position: absolute;
        top: 1060px;
        left: 35px;
        right: 35px;
        text-align: center;
        z-index: 10;
      }}

      .headline {{
        font-size: 50px;
        font-weight: 600;
        color: #fff;
        line-height: 1.4;
        /* margin-bottom: 20px; */
        /* display: flex;
        flex-direction: column;
        align-items: center; */
      }}

      .headline .yellow {{
        background: #fce059; /* Yellow highlight */
        color: #000;
        padding: 0px 6px;
        border-radius: 3px;
        font-weight: 700;
      }}

      .subtext {{
        font-size: 24px;
        font-weight: 500;
        color: #ddd;
        line-height: 1.4;
      }}

      /* Logo section */
      .logo-container {{
        position: absolute;
        top: 10px;
        right: 10px;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        z-index: 15;
      }}

      .logo img {{
        height: 110px;
        width: auto;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Background -->
      <!-- Logo -->
      <div class="logo-container">
        <div class="logo">
          <img src="logo.png" alt="The Tatva" />
        </div>
      </div>

      <!-- Text -->
      <div class="text-overlay">
        {headline}
      </div>
    </div>
  </body>
</html>
"""

news_template = {
    "page_name": "the_startup_journey",
    "template_type": "news_slide",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {},
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
                "green_screen": {"type":"default", "values": (128,128,128,1)},
            }
        },
        "content_slide": {
            "html_template": CONTENT_SLIDE_HTML_TEMPLATE,
            "overlay_template": CONTENT_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                "headline": {"type": "text_area", "tag": "div", "class": "headline"},
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
                "green_screen": {"type":"default", "values": (128,128,128,1)},
            }
        },
    },
}
