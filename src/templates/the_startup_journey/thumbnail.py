TEMPLATE_DESCRIPTION = """
Thumbnail: This The Startup Journey template creates eye-catching thumbnail images for social media posts focusing on entrepreneurial journeys, founder stories, startup challenges, and business growth insights. It features a dynamic design with a prominent background image, a circular profile/product image overlay, bold yellow-boxed headlines, and clean white subtext to grab attention and drive engagement. The template showcases the entrepreneurial narrative while maintaining strong visual appeal.
The template is presented by The Startup Journey brand and highlights inspiring startup stories, founder experiences, and key business moments.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Thumbnail Slide:
  ### Attributes:
  - This should be the opening slide of the storyboard. Must be eye catching and engaging, featuring entrepreneurial moments.
    EX: A founder working on their laptop in a startup office, or an entrepreneur presenting at a conference, or a team brainstorming session.
  
  - image_description: A one line description of the background image you would like to use for the slide.
    EX: "A founder writing on a whiteboard", "An entrepreneur smiling at their desk"

  
  - headline: The main headline displayed in a bold yellow box - short and impactful, uppercase preferred.
    EX: "FROM FAILURE TO SUCCESS", "THE PIVOT MOMENT", "BUILDING IN PUBLIC"
  
  - subtext: Supporting text in white below the headline - provides context or story detail.
    EX: "How this founder rebuilt after losing everything", "The decision that saved the company", "A founder's transparent journey"

  ### Text Input:
    {{
      "name": "headline_slide",
      "image_description": "str",
      "text":{{
      "headline": "str",
      "subtext": "str"
      }}
    }}

NOTE: 
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
- Headlines work best when short and uppercase for maximum impact.
- Subtext should complement the headline and tell the entrepreneurial story.
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
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&display=swap"
      rel="stylesheet"
    />

    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      body {{
        font-family: "Montserrat", sans-serif;
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
        object-fit: cover;
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
        align-items: flex-start;
      }}

      /* 3. Circular Insert */
      .profile-circle {{
        width: 320px;
        height: 320px;
        border-radius: 50%;
        overflow: hidden;
        border: 3px solid #ffe605;

        /* Positioning */
        margin-left: 50px;
        margin-bottom: 30px;
        z-index: 25;
        position: relative;
        background-color: #000;
      }}

      .profile-circle img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
      }}

      /* 4. Text Box Background */
      .text-content {{
        width: 100%;
        background-color: #000000;
        padding: 0px 40px 60px 40px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px; /* Space between Headline and Subtext */
        z-index: 20;
      }}

      /* SHARED TYPOGRAPHY for consistency */
      .headline,
      .subtext {{
        font-family: "Montserrat", sans-serif;
        font-size: 58px;
        font-weight: 800; /* Extra Bold */
        text-align: center;
        text-transform: uppercase;
        line-height: 1.3;
      }}

      /* THE YELLOW BOX */
      .headline {{
        background-color: #ffe605;
        color: #000000;
        padding: 0px 10px;
        display: inline-block; /* Wraps the background tight to text */
      }}

      /* THE WHITE TEXT */
      .subtext {{       
        color: #ffffff;
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
        <!-- 3. Circle Insert -->
        <div class="profile-circle">
          <img src="{circle_image}" alt="Circle Insert" />
        </div>

        <!-- 4. Text Content -->
        <div class="text-content">
          <!-- PART A: Yellow Box -->
          {headline}

          <!-- PART B: White Text -->
          {subtext}
        </div>
      </div>
    </div>
  </body>
</html>
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
"""

thumbnail_template = {
    "page_name": "the_startup_journey",
    "template_type": "thumbnail",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "div", "class": "headline"},
                    "subtext": {"type": "text_area", "tag": "div", "class": "subtext"},
            },
            "assets":{
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"default": "logo.png"},
                "circle_image": {"type":"bytes", "file_type":"png", "default": "circle_image.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
            },
            "video_edits":{
            }
        },
    },
}
