TEMPLATE_DESCRIPTION = """
Thumbnail: This UPSC World template creates eye-catching thumbnail images for social media posts. It combines a striking background image with bold, highlighted text overlays to grab attention and drive engagement. The thumbnail should capture the essence of the story while remaining visually appealing and readable at smaller sizes.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Thumbnail Slide:
  ### Attributes:
  - image_description: A one line description of the image you would like to use for the slide.
    EX: A photo of a temple and a gurdwara created inside a game.
  
  - headline: The main headline of the story with no new lines. Max 3-4 words.
  
  - subtext: A short subtext for the post, one sentence max.

  ### Text Input:
    {{
      "name": "headline_slide",
      "image_description": "str",
      "text":{{
      "headline": "str",
      "subtext": "str",
      }}
    }}

NOTE: 
- To highlight and emphasize a specific word or phrase in your subtext, wrap only that part with double asterisks (**like this**). Use this highlighting exclusively for the "subtext" field, and only for a portion of the sentence—not the entire subtext.
- Use '\\n' to indicate line breaks within the text.
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
"""

HEADLINE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Instagram Post Template</title>
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
        font-family: 'Arial', sans-serif;
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
        background: black;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        position: absolute;
        top: 0;
        left: 0;
      }}

      /* Top yellow banner */
      /* Top yellow banner */
      .top-banner {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        background: #ffeb00;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 15px 50px;
        z-index: 10;
      }}

      .top-banner span {{
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 800; /* ExtraBold */
        font-size: 80px;
        color: #e00000;
        text-transform: uppercase;
        line-height: 1;
        letter-spacing: 0;
        white-space: nowrap; /* Prevent line breaks */
        display: inline-block;
      }}

      /* Gradient at bottom */
      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 45%;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.9) 0%,
          rgba(0, 0, 0, 0.8) 40%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      /* Bottom text */
      .text-overlay {{
        position: absolute;
        bottom: 55px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        text-align: center;
        z-index: 10;
      }}  

      .subtext {{
        font-size: 55px;
        font-weight: 600;
        color: #ffffff;
        line-height: 1.2;
      }}

      .yellow {{
        color: #ffeb00;
        font-weight: 800;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <img
        src="{background_image}"
        alt="Background"
        class="background-image"
      />

      <!-- Top Banner -->
      <div class="top-banner">
        {headline}

      </div>

      <!-- Gradient Overlay -->
      <div class="gradient-overlay"></div>

      <!-- Bottom Text -->
      <div class="text-overlay">
        {subtext}
      </div>
    </div>

    <script>
      // Function to dynamically resize headline to fit in one line
      function resizeHeadlineToFit() {{
        const headline = document.querySelector('.headline')
        const banner = headline.parentElement

        // Get the computed padding of the banner
        const computedStyle = window.getComputedStyle(banner)
        const paddingLeft = parseFloat(computedStyle.paddingLeft)
        const paddingRight = parseFloat(computedStyle.paddingRight)

        // Available width = container width - padding
        const maxWidth = 1080 - paddingLeft - paddingRight

        let fontSize = 120 // Start with default size
        headline.style.fontSize = fontSize + 'px'

        console.log('Max width:', maxWidth)
        console.log('Initial text width:', headline.offsetWidth)

        // Reduce font size until text fits
        while (headline.offsetWidth > maxWidth && fontSize > 20) {{
          fontSize -= 1
          headline.style.fontSize = fontSize + 'px'
          console.log(
            'Font:',
            fontSize,
            'Text width:',
            headline.offsetWidth,
            'Max width:',
            maxWidth
          )
        }}

        console.log('Final font size:', fontSize)
      }}

      // Run on page load
      window.addEventListener('load', resizeHeadlineToFit)

      // Re-run if window is resized
      window.addEventListener('resize', resizeHeadlineToFit)
    </script>
  </body>
</html>
"""

HEADLINE_OVERLAY_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Instagram Post Template</title>
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
        font-family: 'Arial', sans-serif;
        background: rgba(128,128,128,1);
        display: flex;
        justify-content: center;
        min-height: 100vh;
      }}  

      .container {{
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        background: black;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        position: absolute;
        top: 0;
        left: 0;
      }}

      /* Top yellow banner */
      /* Top yellow banner */
      .top-banner {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        background: #ffeb00;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 15px 50px;
        z-index: 10;
        min-height: 9%;
      }}

      .bottom-banner {{
        height: 91%;
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 10;
      }}
      .top-banner span {{
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 800; /* ExtraBold */
        font-size: 80px;
        color: #e00000;
        text-transform: uppercase;
        line-height: 1;
        letter-spacing: 0;
        white-space: nowrap; /* Prevent line breaks */
        display: inline-block;
      }}

      /* Gradient at bottom */
      .gradient-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 45%;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.9) 0%,
          rgba(0, 0, 0, 0.8) 40%,
          rgba(0, 0, 0, 0) 100%
        );
        z-index: 5;
      }}

      /* Bottom text */
      .text-overlay {{
        position: absolute;
        bottom: 55px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        text-align: center;
        z-index: 10;
      }}  

      .subtext {{
        font-size: 55px;
        font-weight: 600;
        color: #ffffff;
        line-height: 1.2;
      }}

      .yellow {{
        color: #ffeb00;
        font-weight: 800;
      }}
    </style>
  </head>
  <body>
    <div class="container">
    <!-- Top Banner -->
      <div class="top-banner">
        {headline}

      </div>
      <div class="bottom-banner">
      <!-- Gradient Overlay -->
      <div class="gradient-overlay"></div>

      <!-- Bottom Text -->
      <div class="text-overlay">
        {subtext}
      </div>
      <video
        src="{background_video}"
        alt="Background"
        class="background-image"
      />
      </div>
    </div>

    <script>
      // Function to dynamically resize headline to fit in one line
      function resizeHeadlineToFit() {{
        const headline = document.querySelector('.headline')
        const banner = headline.parentElement

        // Get the computed padding of the banner
        const computedStyle = window.getComputedStyle(banner)
        const paddingLeft = parseFloat(computedStyle.paddingLeft)
        const paddingRight = parseFloat(computedStyle.paddingRight)

        // Available width = container width - padding
        const maxWidth = 1080 - paddingLeft - paddingRight

        let fontSize = 120 // Start with default size
        headline.style.fontSize = fontSize + 'px'

        console.log('Max width:', maxWidth)
        console.log('Initial text width:', headline.offsetWidth)

        // Reduce font size until text fits
        while (headline.offsetWidth > maxWidth && fontSize > 20) {{
          fontSize -= 1
          headline.style.fontSize = fontSize + 'px'
          console.log(
            'Font:',
            fontSize,
            'Text width:',
            headline.offsetWidth,
            'Max width:',
            maxWidth
          )
        }}

        console.log('Final font size:', fontSize)
      }}

      // Run on page load
      window.addEventListener('load', resizeHeadlineToFit)

      // Re-run if window is resized
      window.addEventListener('resize', resizeHeadlineToFit)
    </script>
  </body>
</html>
"""

upsc_world_headline_template = {
    "page_name": "upsc_world",
    "template_type": "headline",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "span", "class": "headline"},
                    "subtext": {"type": "text_area", "tag": "div","class":"subtext"}
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
            },
            "image_edits": {"crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},},
            "video_edits":{
                "type": {"type":"default", "values": "video_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
                "class_name":{"type":"default","values":"background-image"},
            }
        },
    },
}