TEMPLATE_DESCRIPTION = """
Thumbnail: This Smart India News template creates eye-catching thumbnail images for social media posts focusing on pan-India news, current affairs, national updates, politics, social issues, and important developments across the country. It features a full-screen background image with a dark gradient overlay, a bold headline in a distinctive lime-green box, white supporting text, and the Smart India News branding at the bottom with decorative lines.
The template combines professional news presentation with eye-catching design - ideal for breaking news, important updates, and trending national stories.
"""

JSON_DESCRIPTION = """
This template has the following slide:
Thumbnail Slide:
  ### Attributes:
  - image_description: A one line description of the background image you would like to use for the slide.
    EX: "Indian parliament building", "A crowd of people protesting", "Prime Minister addressing the nation", "Indian flag waving"
  
  - headline: The main headline displayed in a bold lime-green box - short, impactful, uppercase preferred.
    EX: "CLAT 2026 TOPPER'S EMOTIONAL
MOMENT"
  
  - sub_headline: Supporting text in white below the headline - provides the news context or main story detail.
    EX: "Geetali Gupta secured AIR 1 in clat 2026 and a video of her emotional reaction to the result went viral"

  ### Text Input:
    {{
      "name": "thumbnail_slide",
      "image_description": "str",
      "text":{{
      "headline": "str",
      "sub_headline": "str"
      }}
    }}

NOTE: 
- To emphasize specific words or phrases in your text, wrap them with double asterisks (**like this**) for bold highlighting.
- Use '\\n' to indicate line breaks within the text.
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
- Headlines work best when short and impactful - focus on the key news angle.
- Sub-headline should provide essential context or the main story detail.
- Content should be factual, newsworthy, and focused on pan-India developments.
- Only one slide is required for this template.
"""

THUMBNAIL_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>News Post Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap"
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
        background-color: #f0f0f0;
        display: flex;
        justify-content: center;
        min-height: 100vh;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        background: #000;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        object-fit: {crop_type};
        object-position: center;
        /* Slight zoom effect often seen in these templates */
        transform: scale(1.01);
      }}

      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 80%;
        /* Adjusted gradient to create a solid black base for text */
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 1) 0%,
          rgba(0, 0, 0, 0.9) 30%,
          rgba(0, 0, 0, 0.6) 50%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      .content-wrapper {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 0 60px 50px 60px;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
      }}    

      /* Headline Styles (Green Box) */
      .headline-container {{
        margin-bottom: 30px;
        display: flex;
        flex-direction: column;
        align-items: center;
      }}

      .headline-text {{
        background-color: #c7fa67;
        color: #000000;
        font-size: 52px;
        font-weight: 700;
        text-transform: uppercase;

        /* CHANGE 2: Reduce vertical padding slightly so there isn't too much 
     green space between the two lines of text */
        padding: 5px 25px;

        /* CHANGE 3: Tighten line-height to keep the box height snug to the text */
        line-height: 1.1;

        display: inline-block;
      }}

      /* Body Text Styles */
      .sub-headline {{
        color: #ffffff;
        font-size: 42px;
        font-weight: 700;
        line-height: 1.2;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
      }}

      /* Footer / Logo Section */
      .footer {{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }}

      .logo-row {{
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 25px;
        margin-bottom: 15px;
      }}

      .line {{
        height: 3px;
        background-color: #ffffff;
        flex: 1; /* Takes up remaining space */
        border-radius: 2px;
      }}

      .logo-img {{
        height: 180px; /* Adjust based on actual logo aspect ratio */
        width: auto;
        object-fit: contain;
      }}

      .brand-name {{
        color: #ffffff;
        font-size: 18px;
        font-weight: 600;
        letter-spacing: 1px;
        opacity: 0.9;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Background Image -->
      <img
        src="{background_image}"
        alt="Background"
        class="background-image"
      />

      <!-- Dark Gradient Overlay -->
      <div class="gradient-overlay"></div>

      <!-- Main Content -->
      <div class="content-wrapper">
        <!-- Headline Highlighted Green -->
        <div class="headline-container">
          {headline}
        </div>

        <!-- White Subtext -->
        {sub_headline}

        <!-- Footer with Logo and Lines -->
        <div class="footer">
          <div class="logo-row">
            <div class="line"></div>
            <!-- Assumes logo.png is the icon/symbol -->
            <img
              src="{logo_image}"
              alt="Smart India News Logo"
              class="logo-img"
            />
            <div class="line"></div>
          </div>
          <!-- Brand text below logo as per image -->
        </div>
      </div>
    </div>
  </body>
</html>
"""

THUMBNAIL_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>News Post Template</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap"
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
        background-color: #000;
        display: flex;
        justify-content: center;
        min-height: 100vh;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        background: #000;
      }}

      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 80%;
        /* Adjusted gradient to create a solid black base for text */
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 1) 0%,
          rgba(0, 0, 0, 0.9) 30%,
          rgba(0, 0, 0, 0.6) 50%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      .content-wrapper {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 0 60px 50px 60px;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
      }}    

      /* Headline Styles (Green Box) */
      .headline-container {{
        margin-bottom: 30px;
        display: flex;
        flex-direction: column;
        align-items: center;
      }}

      .headline-text {{
        background-color: #c7fa67;
        color: #000000;
        font-size: 52px;
        font-weight: 700;
        text-transform: uppercase;

        /* CHANGE 2: Reduce vertical padding slightly so there isn't too much 
     green space between the two lines of text */
        padding: 5px 25px;

        /* CHANGE 3: Tighten line-height to keep the box height snug to the text */
        line-height: 1.1;

        display: inline-block;
      }}

      /* Body Text Styles */
      .sub-headline {{
        color: #ffffff;
        font-size: 42px;
        font-weight: 700;
        line-height: 1.2;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
      }}

      /* Footer / Logo Section */
      .footer {{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }}

      .logo-row {{
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 25px;
        margin-bottom: 15px;
      }}

      .line {{
        height: 3px;
        background-color: #ffffff;
        flex: 1; /* Takes up remaining space */
        border-radius: 2px;
      }}

      .logo-img {{
        height: 180px; /* Adjust based on actual logo aspect ratio */
        width: auto;
        object-fit: contain;
      }}

      .brand-name {{
        color: #ffffff;
        font-size: 18px;
        font-weight: 600;
        letter-spacing: 1px;
        opacity: 0.9;
      }}
    </style>
  </head>
  <body>
    <div class="container">

      <!-- Main Content -->
      <div class="content-wrapper">
        <!-- Headline Highlighted Green -->
        <div class="headline-container">
          {headline}
        </div>

        <!-- White Subtext -->
        {sub_headline}

        <!-- Footer with Logo and Lines -->
        <div class="footer">
          <div class="logo-row">
            <div class="line"></div>
            <!-- Assumes logo.png is the icon/symbol -->
            <img
              src="{logo_image}"
              alt="Smart India News Logo"
              class="logo-img"
            />
            <div class="line"></div>
          </div>
          <!-- Brand text below logo as per image -->
        </div>
      </div>
    </div>
  </body>
</html>
"""

smart_india_news_thumbnail_template = {
    "page_name": "smart_india_news",
    "template_type": "thumbnail",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "thumbnail_slide": {
            "html_template": THUMBNAIL_HTML_TEMPLATE,
            "overlay_template": THUMBNAIL_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "span", "class": "headline-text"},
                    "sub_headline": {"type": "text_area", "tag": "div", "class": "sub-headline"},
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"default": "logo.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
            },
            "video_edits":{
              "type": {"type":"default", "values": "image_overlay"},
              "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            }
        },
    },
}