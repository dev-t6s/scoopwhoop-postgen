TEMPLATE_DESCRIPTION = """
Founders Quote: This template creates impactful founder quote posts featuring a photo of the founder with an inspiring quote displayed in a bold yellow-highlighted box at the bottom. The design showcases wisdom and insights from successful founders and entrepreneurs.

Example: Photo of Nithin Kamath with yellow quote box "DON'T START WITH THE GOAL OF 'DOING A STARTUP.' THE RISK IS THAT YOU MIGHT GET MARRIED TO THE WRONG IDEA TOO EARLY" and attribution "-Nithin Kamath, Co-founder of Zerodha"

NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Founders Quote Slide:
  ### Attributes:
  - This should be an impactful quote slide featuring a photo of the founder/entrepreneur.
    EX: Photo of a founder speaking, portrait of entrepreneur, founder at an event, etc.
  
  - image_description: A one line description of the founder's photo.
    EX: "Photo of Nithin Kamath smiling during an interview"
    EX: "Kunal Shah speaking at a startup event"
  
  - headline: The inspirational or insightful quote from the founder. Text wrapped in ** ** appears with yellow highlight.
    EX: "**DON'T START WITH THE GOAL OF** \\n 'DOING A STARTUP.' THE RISK IS THAT \\n YOU MIGHT GET MARRIED \\n TO THE WRONG IDEA TOO EARLY"
  
  - subtext: The name and title/company of the person being quoted.
    EX: "-Nithin Kamath, Co-founder of Zerodha"
    EX: "-Kunal Shah, Founder of CRED"
  
  ### Text Input:
    {{
      "name": "founders_slide",
      "image_description": "str",
      "text":{{
      "headline": "str",
      "subtext": "str"
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
        bottom: 50px;
        left: 35px;
        right: 35px;
        text-align: center;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
      }}

      .headline {{
        font-size: 50px;
        font-weight: 600;
        color: #fff;
        line-height: 1.4;
        order: -1;
        margin-bottom: 15px;
      }}

      .headline .yellow {{
        background: #fce059; /* Yellow highlight */
        color: #000;
        padding: 0px 6px;
        border-radius: 3px;
        font-weight: 700;
      }}

      .subtext {{
        font-size: 28px;
        font-weight: 600;
        font-style: italic;
        color: white;
        line-height: 1.4;
        margin-top: 15px;
      }}

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

      .arrow {{
        font-size: 32px;
        color: white;
      }}

      /* Export button */
      .export-button {{
        position: fixed;
        top: 20px;
        right: 20px;
        background: #007bff;
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
        transition: all 0.3s ease;
        z-index: 1000;
      }}

      .export-button:hover {{
        background: #0056b3;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 123, 255, 0.4);
      }}

      .export-button:active {{
        transform: translateY(0);
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
        {subtext}
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
        background-color: rgba(128,128,128,1);
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
        bottom: 50px;
        left: 35px;
        right: 35px;
        text-align: center;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
      }}

      .headline {{
        font-size: 50px;
        font-weight: 600;
        color: #fff;
        line-height: 1.4;
        order: -1;
        margin-bottom: 15px;
      }}

      .headline .yellow {{
        background: #fce059; /* Yellow highlight */
        color: #000;
        padding: 0px 6px;
        border-radius: 3px;
        font-weight: 700;
      }}

      .subtext {{
        font-size: 28px;
        font-weight: 600;
        font-style: italic;
        color: white;
        line-height: 1.4;
        margin-top: 15px;
      }}

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
      <div class="logo-container">
        <div class="logo">
          <img src="logo.png" alt="" />
        </div>
      </div>

      <!-- Text -->
      <div class="text-overlay">
        {headline}
        {subtext}
      </div>
    </div>
  </body>
</html>
"""

founders_template = {
    "page_name": "the_startup_journey",
    "template_type": "founders_slide",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "founders_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "div", "class": "headline"},
                    "subtext": {"type": "text_area", "tag": "div", "class": "subtext"},
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
                "green_screen": {"type":"default", "values": (128,128,128,1)}
            }
        },
    },
}
