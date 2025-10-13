TEMPLATE_DESCRIPTION = """
Carousel: This template creates engaging startup/business carousel posts with one impactful headline slide followed by 4-5 content slides. The headline slide features a background image with bold yellow-highlighted text, while content slides present key information with yellow question tags and white text on black background.

Example Headline Slide: Background image with "**STARTUP FUNDING TRENDS** \\n WHAT'S CHANGING IN 2025"
Example Content Slides: Yellow question tag "WHAT?" with detailed explanation below in white text

The source should only be used if the post or the news is not from ScoopWhoop.
NOTE: This template requires 1 headline slide + 4-5 content slides (total 5-6 slides).
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:

1. Headline Slide (REQUIRED - Only 1):
  ### Attributes:
  - This is the opening slide with an impactful background image and headline text.
    EX: Startup scene, business concept, relevant visual metaphor, etc.
  
  - image_description: A one line description of the background image.
  
  - headline: Contains both the highlighted text and subtext. Text wrapped in ** ** appears with yellow highlight, text without ** ** appears in white below.
    EX: "**STARTUP FUNDING TRENDS** \\n WHAT'S CHANGING IN 2025"
    EX: "**THE RISE OF AI STARTUPS** \\n HOW FOUNDERS ARE BUILDING THE FUTURE"

  - subtext: A short subtext for the post, one sentence max.
  
  ### Text Input:
    {{
      "name": "headline_slide",
      "image_description": "str",
      "text":{{
        "headline": "str",
        "subtext": "str"
      }}
    }}

2. Content Slides (REQUIRED - 4 to 5 slides):
  ### Attributes:
  - These slides present key information/insights with a background image, yellow question tag, and detailed content text.
  
  - image_description: A one line description of the background image that relates to the content.
  
  - question: Short question/tag text that appears in yellow box (e.g., "WHAT IS IT?", "WHY IS IT IMPORTANT?", "HOW DOES IT WORK?", "KEY POINT").
  
  - content: Main text content that appears in white below the question tag.
  
  ### Text Input (repeat 4-5 times):
    {{
      "name": "content_slide",
      "image_description": "str",
      "text":{{
        "question": "str",
        "content": "str"
      }}
    }}

NOTE: 
- Use **str** to highlight parts of the text in headline (this creates the yellow highlight effect).
- Use \\n for new line
- Keep question tags short and impactful (1-3 words)
- Content should be concise but informative
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
- Total slides should be 5-6 (1 headline + 4-5 content)
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
          rgba(0, 0, 0, 0.9) 30%,
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
        margin-bottom: 0px;
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
        margin-top: 10px;
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
          rgba(0, 0, 0, 0.9) 30%,
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
        margin-bottom: 0px;
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
        margin-top: 10px;
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
        {subtext}
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

      /* Black bottom section */
      .black-section {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 40%;
        background: #000;
        z-index: 5;
        padding: 00px 0px 80px 0px;
        display: flex;
        flex-direction: column;
        gap: 20px;
      }}
      .question {{
        font-size: 52px;
        font-weight: 700;
        background: #ffde59;
        color: #000;
        padding: 0px 16px;
        width: fit-content;
        letter-spacing: 0.5px;
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

      .logo-text {{
        font-size: 48px;
        font-weight: 800;
        color: white;
        font-family: "Montserrat", sans-serif;
      }}

      .arrow {{
        font-size: 32px;
        color: white;
      }}

      .text-box {{
        flex: 1;
        display: flex;
        align-items: flex-start;
      }}

      .text {{
        width: 100%;
        padding: 0px 20px 0px 40px;
        font-size: 54px;
        font-weight: 600;
        color: #fff;
        line-height: 1.4;
        margin-top: 0px;
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

      <!-- Black Bottom Section -->
      <div class="black-section">
        {question}
        <div class="text-box">
          {content}
        </div>
      </div>
    </div>

    <script>
      function adjustTextSize() {{
        const blackSection = document.querySelector(".black-section");
        const text = document.querySelector(".text");

        // Get the black section height
        const blackSectionHeight = blackSection.offsetHeight;

        let fontSize = 100; // Start with max size
        text.style.fontSize = fontSize + "px";

        // Reduce font size until text fits
        while (text.scrollHeight > blackSectionHeight - 130 && fontSize > 20) {{
          fontSize -= 1;
          text.style.fontSize = fontSize + "px";
        }}
      }}

      // Run on page load
      window.addEventListener("load", adjustTextSize);

      // Re-run if window is resized
      window.addEventListener("resize", adjustTextSize);
    </script>
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
        display: flex;
        justify-content: center;
        /* align-items: center; */
        min-height: 100vh;
      }}

      .container {{
        background: #000000;
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
      }}

      .video-container {{
        height: 60%;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1;
      }}

      .background-image-cover {{
        height: 100%;
        object-fit: cover;
      }}

      .background-image-contain {{
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
      }}

      /* Black bottom section */
      .black-section {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 40%;
        background: #000;
        z-index: 5;
        padding: 00px 0px 80px 0px;
        display: flex;
        flex-direction: column;
        gap: 20px;
      }}
      .question {{
        font-size: 52px;
        font-weight: 700;
        background: #ffde59;
        color: #000;
        padding: 0px 16px;
        width: fit-content;
        letter-spacing: 0.5px;
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

      .logo-text {{
        font-size: 48px;
        font-weight: 800;
        color: white;
        font-family: "Montserrat", sans-serif;
      }}

      .arrow {{
        font-size: 32px;
        color: white;
      }}

      .text-box {{
        flex: 1;
        display: flex;
        align-items: flex-start;
      }}

      .text {{
        width: 100%;
        padding: 0px 20px 0px 40px;
        font-size: 54px;
        font-weight: 600;
        color: #fff;
        line-height: 1.4;
        margin-top: 0px;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      
      <!-- Logo -->
      <div class="logo-container">
        <div class="logo">
          <img src="logo.png" alt="The Tatva" />
        </div>
      </div>

      <!-- Background -->
      <div class="video-container">
        <video src="{background_video}" autoplay muted loop class="background-image-{crop_type}" />
      </div>

      <!-- Black Bottom Section -->
      <div class="black-section">
        {question}
        <div class="text-box">
          {content}
        </div>
      </div>
    </div>

    <script>
      function adjustTextSize() {{
        const blackSection = document.querySelector(".black-section");
        const text = document.querySelector(".text");

        // Get the black section height
        const blackSectionHeight = blackSection.offsetHeight;

        let fontSize = 100; // Start with max size
        text.style.fontSize = fontSize + "px";

        // Reduce font size until text fits
        while (text.scrollHeight > blackSectionHeight - 130 && fontSize > 20) {{
          fontSize -= 1;
          text.style.fontSize = fontSize + "px";
        }}
      }}

      // Run on page load
      window.addEventListener("load", adjustTextSize);

      // Re-run if window is resized
      window.addEventListener("resize", adjustTextSize);
    </script>
  </body>
</html>
"""

scheme_template = {
    "page_name": "the_startup_journey",
    "template_type": "scheme",
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
                "question": {"type": "text_area", "tag": "div", "class": "question"},
                "content": {"type": "text_area", "tag": "div", "class": "text"},
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
            },
            "video_edits":{
                "type": {"type":"default", "values": "video_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
                "class_name":{"type":"default","values":"background-image"},
                "green_screen": {"type":"default", "values": (128,128,128,1),
                "padding":{"type":"default","values":256}},
            }
        },
    },
}
