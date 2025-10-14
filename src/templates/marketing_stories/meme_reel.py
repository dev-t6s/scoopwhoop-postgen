TEMPLATE_DESCRIPTION = """
Meme Reel: This Marketing Stories template creates engaging video reels combining static images with video content. The reel is split into two halves - the top half features a static image with text overlay on a white gradient background, while the bottom half shows a video with bold text overlay. This format is perfect for meme-style content that combines a setup (image + text) with a punchline or reaction (video + text).
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Meme Reel Slide:
  ### Attributes:
  - This creates a split-screen video reel with image on top and video on bottom.
  - The top half shows an image with text overlay (with yellow highlighting) on a white gradient background.
  - The bottom half shows a video with bold text overlay.
    EX: Top - "When your boss asks if you're busy" (image of someone looking calm)
        Bottom - "Meanwhile my browser tabs:" (video of chaos/multiple things happening)
  
  - image_description: A one line description of the image for the top half of the reel.
  - video_description: A one line description of the video for the bottom half of the reel.
  - top_headline: The text to display on the image (top half). Use **str** for yellow highlighting.
  - bottom_headline: The text to display on the video (bottom half). This will have white text with black outline.

  ### Text Input:
    {{
      "name": "meme_reel_slide",
      "image_description": "str",
      "video_description": "str",
      "text":{{
        "top_headline": "str",
        "bottom_headline": "str"
      }}
    }}

NOTE: 
- Use **str** to highlight parts of the top_headline text (will appear with yellow background).
- Use \\n for new lines in both headlines.
- DO NOT COMPLICATE THE IMAGE/VIDEO DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
- The video should complement or contrast with the image to create meme-style humor or engagement.
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
        min-height: 100vh;
        background: rgba(0, 247, 34, 1);
      }}

      .container {{
        width: 1080px;
        height: 1920px;
        position: relative;
        overflow: hidden;
        background: rgba(0, 247, 34, 1);
      }}

      /* Image Container (Top Half) */
      .image-container {{
        width: 100%;
        height: 50%;
        position: relative;
        overflow: hidden;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;
      }}

      /* White gradient overlay at bottom of image */
      .image-text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 80px 20px 40px 20px;
        background: linear-gradient(
          to top,
          rgba(255, 255, 255, 0.95) 0%,
          rgba(255, 255, 255, 0.85) 50%,
          transparent 100%
        );
        z-index: 10;
      }}

      .image-headline {{
        font-size: 50px;
        font-weight: 700;
        color: #000;
        line-height: 1.3;
        text-align: center;
      }}

      .image-headline .yellow {{
        background: #ffff01;
        color: #000;
        padding: 2px 8px;
        border-radius: 2px;
      }}

      /* Video Container (Bottom Half) */
      .video-container {{
        width: 100%;
        height: 50%;
        position: relative;
        overflow: hidden;
      }}        

      .background-video {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        background-color: rgba(0, 247, 34,1);
      }}

      /* Video text at center top */
      .video-text-overlay {{
        position: absolute;
        top: 100px;
        left: 0;
        right: 0;
        text-align: center;
        z-index: 10;
        padding: 0 40px;
      }}

      .video-headline {{
        font-size: 60px;
        font-weight: 800;
        color: white;
        line-height: 1.3;
        text-shadow: -3px -3px 0 #000, 3px -3px 0 #000, -3px 3px 0 #000,
          3px 3px 0 #000, 0px 3px 0 #000, 3px 0px 0 #000, 0px -3px 0 #000,
          -3px 0px 0 #000, 0 5px 18px rgba(0, 0, 0, 0.85);
      }}

      /* Marketing Stories tag at bottom */
      .marketing-tag {{
        position: absolute;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        color: rgba(185, 183, 183, 0.86);
        font-size: 46px;
        font-weight: 600;
        z-index: 10;
        text-shadow: -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000,
          2px 2px 0 #000, 0px 2px 0 #000, 2px 0px 0 #000, 0px -2px 0 #000,
          -2px 0px 0 #000, 0 4px 12px rgba(0, 0, 0, 0.7);
      }}

      /* Logo container at top right */
      .logo-container {{
        position: absolute;
        top: 20px;
        right: -10px;
        z-index: 15;
      }}

      .logo {{
        background-color: white;
        height: 64px;
        width: 140px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
      }}    

      .logo img {{
        height: 90px;
        position: relative;
        bottom: 4px;
        width: auto;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Image Container (Top Half) -->
      <div class="image-container">
        <img
          src="{top_image}"
          alt="Background"
          class="background-image"
        />

        <!-- Text with white gradient at bottom -->
        <div class="image-text-overlay">
          {top_headline}
        </div>
      </div>

      <!-- Video Container (Bottom Half) -->
      <div class="video-container">
        <video src="{background_video}" class="background-video" loop muted preload="none"></video>

        <!-- Text at center top -->
        <div class="video-text-overlay">
          {bottom_headline}
        </div>

        <!-- Marketing Stories tag at bottom -->
        <div class="marketing-tag">@Marketing.stories</div>
      </div>

      <!-- Logo at top right -->
      <div class="logo-container">
        <div class="logo">
          <img src="logo.png" alt="Marketing Stories" />
        </div>
      </div>
    </div>
  </body>
</html>

"""

meme_reel_template = {
    "page_name": "marketing_stories",
    "template_type": "meme_reel",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "meme_reel_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "video_only": True,
            "text": {
                    "top_headline": {"type": "text_area", "tag": "div", "class": "image-headline"},
                    "bottom_headline": {"type": "text_area", "tag": "div", "class": "video-headline"}
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "top_image": {"type":"bytes", "file_type":"png","default":"image.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
            },
            "video_edits":{
                "type": {"type":"default", "values": "video_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"]},
                "green_screen": {"type":"default", "values": (0, 247, 34, 1)},
                "class_name": {"type":"default", "values": "background-video"},
                "padding": {"type":"default", "values": 256},
                "add_gradient":{"type":"default","values":False},
            }
        },
    },
}
