TEMPLATE_DESCRIPTION = """
Carousel/Thumbnail: This The Startup Journey template creates eye-catching carousel and thumbnail images for social media posts focusing on entrepreneurial journeys, founder stories, startup challenges, and business growth insights. It features a dynamic design with a prominent background image, bold yellow-boxed headlines, and clean white subtext to grab attention and drive engagement. The template showcases the entrepreneurial narrative while maintaining strong visual appeal.
The template is presented by The Startup Journey brand and highlights inspiring startup stories and founder experiences.
NOTE: This template includes headline, subtext, and optional footer text fields.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Carousel/Thumbnail Slide:
  ### Attributes:
  - This should be the opening slide of the storyboard. Must be eye catching and engaging, featuring entrepreneurial moments.
    EX: A founder working late at night in their startup office, or an entrepreneur pitching to investors, or a team celebrating a milestone.
  
  - image_description: A one line description of the image you would like to use for the slide.
  - headline: The main headline displayed in a bold yellow box - short and impactful, uppercase preferred.
    EX: "FROM GARAGE TO UNICORN", "THE PIVOT THAT CHANGED EVERYTHING"
  
  - subtext: Supporting text in white below the headline - can span multiple lines for storytelling.
    EX: "How this founder turned rejection into a billion-dollar idea", "The journey from 0 to 100 employees"
  
  - footer_text: "Swipe to read"
    EX: "Swipe to read"

  ### Text Input:
    {{
      "name": "headline_slide",
      "image_description": "str",
      "text":{{
      "headline": "str",
      "subtext": "str",
      "footer_text": "str"
      }}
    }}

NOTE: 
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
- Headlines work best when short and uppercase for maximum impact.
- Subtext can be longer to tell the entrepreneurial story.
"""

HEADLINE_SLIDE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>TSJ Style Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <!-- UPDATED FONT LINK: Now includes Italic 800 and 900 -->
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,600;1,800;1,900&display=swap"
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
        min-height: 100vh;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        background-color: #000;
      }}

      /* --- LAYERS --- */

      /* 1. Background Image */
      .background-image {{
        width: 100%;
        height: 80%;
        object-fit: {crop_type};
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1;
      }}

      /* 2. Top Logo */
      .top-logo {{
        position: absolute;
        top: 40px;
        right: 40px;
        z-index: 10;
      }}

      .top-logo img {{  
        height: 120px;
        width: auto;
      }}

      /* --- DYNAMIC BOTTOM SECTION --- */

      .content-layout {{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        z-index: 20;
        display: flex;
        flex-direction: column;
        align-items: flex-end;
      }}

      /* 3. Presented By Section */
      .presented-box {{
        margin-right: 30px;
        margin-bottom: 50px;
        padding: 12px 0px 10px 0px;
        border-left: 8px solid #ffe605;
        padding-left: 8px;
        text-align: left;
        color: #ffffff;
        line-height: 1.4;
      }}

      .presented-label {{
        font-size: 28px;
        /* Updated to 900 (Black Italic) for maximum thickness */
        font-weight: 700;
        font-style: italic;
        color: #000;
        line-height: 1.2;
      }}

      .presented-brand {{
        font-size: 29px;
        font-weight: 700;
        text-transform: capitalize;
        color: #ffffff;
      }}

      /* 4. Text Box Background */
      .text-content {{
        width: 100%;
        background-color: #000000;
        padding: 0px 40px 35px 40px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        z-index: 20;
      }}

      /* SHARED TYPOGRAPHY */
      .headline,
      .subtext {{       
        font-family: "Poppins", sans-serif;
        font-size: 62px;
        font-weight: 800;
        text-align: center;
        text-transform: uppercase;
        line-height: 1.3;
        margin-bottom: 10px;
      }}

      /* PART A: The Yellow Box Headline */
      .headline {{
        background-color: #ffe605;
        color: #000000;
        /* Increased side padding to make the line longer */
        padding: 0px 35px;
        display: inline-block;
        margin-bottom: 5px;
      }}

      /* PART B: White Subtext */
      .subtext {{
        color: #ffffff;
      }}

      .footer-text {{
        color: #ffffff;
        font-family: "Poppins", sans-serif;
        font-size: 28px;
        font-weight: 800;
        font-style: italic;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- 1. Background Image -->
      <img src="{background_image}" alt="Background" class="background-image" />

      <!-- 2. Top Logo -->
      <div class="top-logo">
        <img src="{logo_image}" alt="TSJ Logo" />
      </div>

      <!-- DYNAMIC CONTENT WRAPPER -->
      <div class="content-layout">
        <!-- 3. Presented By (Sits above text box) -->
        <div class="presented-box">
          <div class="presented-label">Presented by</div>
          <div class="presented-brand">The Startup Journey</div>
        </div>

        <!-- 4. Text Content (Black Bottom Box) -->
        <div class="text-content">
          <!-- Headline (Yellow) -->
          {headline}

          <!-- Subtext (White) -->
          {subtext}

          {footer_text}
        </div>
      </div>
    </div>
  </body>
</html>
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
"""

carousel_template = {
    "page_name": "the_startup_journey",
    "template_type": "carousel",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "carousel_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "div", "class": "headline"},
                    "subtext": {"type": "text_area", "tag": "div", "class": "subtext"},
                    "footer_text": {"type": "text_area", "tag": "div", "class": "footer-text"},
            },
            "assets":{
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"default": "logo.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
            },
            "video_edits":{
            }
        },
    },
}
