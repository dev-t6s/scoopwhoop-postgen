TEMPLATE_DESCRIPTION = """
Ad Reel: This Marketing Stories template creates promotional video reels with overlay text and branding. The template features a full-screen background video with bold text overlay positioned near the top, along with the Marketing Stories logo. This format is ideal for viral news, trending stories, or promotional content that needs to grab attention quickly. The video uses green screen technology for easy video compositing.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Ad Reel Slide:
  ### Attributes:
  - This creates a full-screen video reel with text overlay and logo branding.
  - The background video fills the entire frame with the text overlay positioned near the top.
  - Text appears in white with yellow highlighting for emphasis.
  - The Marketing Stories logo appears in the top-left corner.
    EX: "The powerful speech of this **Nepali student** is breaking the internet"
        (with a background video showing the student speaking)
  
  - image_description: A one line description of the image for the top half of the reel.
  - video_description: A one line description of the video for the bottom half of the reel.
  - top_headline: The text to display on the image (top half). Use **str** for yellow highlighting.
  - bottom_headline: The text to display on the video (bottom half). This will have white text with black outline.

  ### Text Input:
    {{
      "name": "ad_reel_slide",
      "video_description": "str",
      "text":{{
        "headline": "str"
      }}
    }}

NOTE: 
- Use **str** to highlight parts of the headline text (will appear with yellow color, no background).
- Use \\n for new lines in the headline.
- DO NOT COMPLICATE THE VIDEO DESCRIPTION, KEEP IT SIMPLE AND DIRECT.
- The video should be engaging and relevant to the headline text.
- This template uses green screen compositing - the actual video will be added via video editing in post-processing.
"""

HEADLINE_SLIDE_HTML_TEMPLATE = """
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Marketing Stories Template</title>
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
        height: 1920px;
      }}

      .container {{
        width: 1080px;
        height: auto;
        position: relative;
        overflow: hidden;
        background: #000;
      }}

      /* Video container */
      .video-container {{
        width: 100%;
        height: 100%;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
      }}

      /* Background image */
      .background-image {{
        width: 100%;
        height: auto;
        /* display: block; */
      }}

      /* Text block */
      .text-overlay {{
        position: absolute;
        top: 380px;
        left: 0;
        right: 0;
        text-align: center;
        z-index: 10;
      }}

      .headline {{
        font-size: 42px;
        font-weight: 700;
        color: white;
        line-height: 1.4;
      }}

      .headline .yellow {{
        background: none; /* Bright yellow highlight */
        color: #ffff01;
        padding: 2px 6px;
        border-radius: 2px;
      }}

      /* Logo container */
      .logo-container {{
        position: absolute;
        top: 80px;
        left: -5px;
        z-index: 15;
      }}

      .logo {{
        background-color: white;
        height: 57px;
        width: 140px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        padding-left: 50px;
      }}

      .logo img {{
        height: 81px;
        position: relative;
        bottom: 2px;
        width: auto;
      }}

      .swipe-indicator {{
        width: 145px;
        height: 145px;
        margin-left: 10px;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Background -->
      <div class="video-container">
        <video src="{background_video}" alt="Background" loop muted preload="metadata" class="background-image"></video>
      </div>


      <!-- Text -->
      <div class="text-overlay">
        {headline}
      </div>

      <!-- Logo at top left -->
      <div class="logo-container">
        <div class="logo">
          <img src="logo.png" alt="Marketing Stories" />
        </div>
      </div>
    </div>
  </body>
  <script>
    (function () {{
      const video = document.querySelector(".background-image");

      function processVideo() {{
        // Get video dimensions
        const width = video.videoWidth;
        const height = video.videoHeight;

        // Calculate the display height based on container width (1080px)
        const containerWidth = 1080;
        const aspectRatio = height / width;
        const displayHeight = containerWidth * aspectRatio;

        // Set explicit dimensions
        video.style.width = containerWidth + "px";
        video.style.height = displayHeight + "px";

        // Set background color to green
        video.style.backgroundColor = "rgba(0, 247, 34, 1)";

        // Remove video source to show only green background
        video.removeAttribute("src");
        video.load();

        // Signal ready
        window.templateReady = true;
        document.body.setAttribute("data-ready", "true");
      }}

      // Try multiple approaches to ensure it runs
      if (video.readyState >= 1) {{
        // Video metadata already loaded
        processVideo();
      }} else {{
        // Wait for metadata
        video.addEventListener("loadedmetadata", processVideo);
      }}

      // Fallback: also try on load
      window.addEventListener("load", function () {{
        if (!window.templateReady && video.readyState >= 1) {{
          processVideo();
        }}
      }});
    }})();
  </script>
</html>
"""

ad_reel_template = {
    "page_name": "marketing_stories",
    "template_type": "ad_reel",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "ad_reel_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "video_only": True,
            "text": {
                    "headline": {"type": "text_area", "tag": "div", "class": "headline"},
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"], "default": "contain"},
            },
            "video_edits":{
                "type": {"type":"default", "values": "video_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
                "green_screen": {"type":"default", "values": (0, 247, 34, 1)},
                "class_name": {"type":"default", "values": "background-image"},
                "padding": {"type":"default", "values": 256},
            }
        },
    },
}
