TEMPLATE_DESCRIPTION = """
Announcement: This template creates impactful startup/business announcement posts featuring a relevant background image with bold yellow-highlighted headline text and supporting white subtext at the bottom. The design emphasizes key achievements, milestones, or announcements with high visual impact.

Example: Background image of a crowd/event, with yellow highlighted text "FROM YOUTUBE TEACHER TO IPO" and white subtext "ALAKH PANDEY IS REWRITING INDIA'S ED-TECH STORY"

The source should only be used if the post or the news is not from ScoopWhoop.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Announcement Slide:
  ### Attributes:
  - This should be an impactful announcement slide featuring a relevant background image.
    EX: A crowd photo at a startup event, founders celebrating, product launch scene, etc.
  
  - image_description: A one line description of the background image that relates to the announcement/achievement.
  
  - headline: Contains both the highlighted text and subtext. Text wrapped in ** ** appears with yellow highlight, text without ** ** appears in white below.
    EX: "**FROM YOUTUBE TEACHER TO IPO** \\n ALAKH PANDEY IS REWRITING INDIA'S ED-TECH STORY"
    EX: "**BOOTSTRAPPED TO UNICORN IN 3 YEARS** \\n THIS FOUNDER BUILT WITHOUT ANY VC FUNDING"
  
  ### Text Input:
    {{
      "name": "announcement_slide",
      "image_description": "str",
      "text":{{
      "headline": "str"
      }}
    }}

NOTE: 
- Use **str** to highlight parts of the text (this creates the yellow highlight effect).
- Use \\n for new line
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
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
        object-fit: cover;
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
          rgba(0, 0, 0, 1) 0%,
          rgba(0, 0, 0, 1) 15%,
          rgba(0, 0, 0, 0.5) 55%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      /* Text area */
      .text-overlay {{
        position: absolute;
        bottom: 110px;
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
          <img src="logo.png" alt="" />
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
        background: #000000;
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
        object-fit: cover;
        position: absolute;
        top: 0;
        left: 0;
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
        font-size: 50px;
        font-weight: 600;
        color: #fff;
        line-height: 1.4;
        /* margin-bottom: 20px; */
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
          <img src="logo.png" alt="" />
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

announcement_template = {
    "page_name": "the_startup_journey",
    "template_type": "announcement_slide",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "announcement_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
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
            }
        },
    },
}
