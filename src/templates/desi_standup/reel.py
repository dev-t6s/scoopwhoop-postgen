TEMPLATE_DESCRIPTION = """
Reel: This Desi Standup template creates engaging vertical video content for social media reels and stories featuring Indian standup comedy moments, funny clips, and hilarious content. It features a clean white background with bold black text overlay positioned above a square (1:1 aspect ratio) video clip. The template is optimized for 1080x1920 dimensions (Instagram Reels/Stories format) and designed specifically for standup comedy performances, funny moments, comedy sketches, and relatable humor.
The template combines minimalist design with comedy content - ideal for creating shareable standup comedy reels that capture attention and make people laugh.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Reel Slide:
  ### Attributes:
  - This should be an engaging comedy reel featuring standup moments or funny clips. Must be hilarious and shareable.
    EX: A standup comedian performing on stage, a funny reaction moment, a comedy sketch clip, a relatable humor bit.
  
  - video_description: A one line description of the comedy video you would like to use for the reel.
    EX: "A standup comedian telling a joke on stage", "A funny facial expression reaction", "A comedian doing physical comedy", "A relatable comedy bit about Indian parents"
  
  - text_content: The main text overlay displayed above the video (bold black text on white background).
    EX: "When the comedian perfectly describes your life 😂", "This joke about Indian parents hit different", "POV: You're at a standup show and can't stop laughing"
    Note: Use \\n for line breaks. This template does NOT support text highlighting.

  ### Text Input:
    {{
      "name": "reel_slide",
      "video_description": "str",
      "text": {{
      "text_content": "str"
      }}
    }}

NOTE: 
- Use \\n for line breaks if needed.
- This template does NOT support text highlighting - all text appears in black.
- DO NOT COMPLICATE THE VIDEO DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
- Content should be funny, relatable, and focused on standup comedy, comedians, humor, and laugh-out-loud moments.
- Text should be concise and set up the comedy moment in the video below.
- Perfect for creating shareable standup comedy reels that make people laugh and tag their friends.
"""

HEADLINE_SLIDE_HTML_TEMPLATE = """
"""


HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <title>Desi Standup</title>
    <style>
      /* Load Roboto Font */
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap");

      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: "Roboto", sans-serif;
        display: flex;
        justify-content: center;
        min-height: 100vh;
        background-color: white;
      }}

      .container {{
        width: 1080px;
        height: 1920px; /* Standard Vertical Video Height */
        background-color: white; /* Light gray background matching the screenshot */
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: center; /* Center content vertically */
        align-items: center;
        box-sizing: border-box;
      }}

      /* Logo Styling - Top Right (Optional, kept for consistency) */
      .logo-container {{
        position: absolute;
        top: 40px;
        right: 40px;
        z-index: 20;
        width: 250px;
        height: auto;
      }}

      .logo-img {{
        width: 100%;
        height: auto;
        display: block;
      }}

      /* Wrapper to group Text and Video */
      .content-wrapper {{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        /* Gap between text and video */
        gap: 30px;
        z-index: 10;
        /* Optional: Move slightly down from exact center if desired */
        padding-top: 50px;
      }}

      /* Text Styling */
      .text-content {{
        font-family: "Roboto", sans-serif;
        font-weight: 700; /* Bold */
        font-size: 75px; /* Large readable size */
        color: #000000; /* Black text */
        margin: 0;
        line-height: 1.2;
        text-align: center;
      }}

      /* Video Styling for 1:1 Clip */
      .image-banner {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0;
        overflow: hidden;
        width: 1080px;
        height: 1080px; /* Forces 1:1 Aspect Ratio */
        background-color: #000; /* Fallback color */
      }}

      .main-video {{
        width: 100%;
        height: 100%;
        object-fit: cover; /* Ensures video fills the square without stretching */
        display: block;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Optional Logo -->
      <div class="logo-container">
        <!-- <img src="logo.png" alt="Logo" class="logo-img" /> -->
      </div>

      <div class="content-wrapper">
        <!-- Text Overlay -->
        {text_content}

        <!-- Video Area (1:1 Square) -->
        <div class="image-banner">
          <video src="{background_video}" class="main-video"></video>
        </div>
      </div>
    </div>
  </body>
  <script>
    (function () {{
      const video = document.getElementsByClassName("main-video")[0];

      function processVideo() {{
        // Since CSS enforces 1080x1080, we primarily just need to trigger the placeholder logic

        // Set background color to green (placeholder logic)
        video.style.backgroundColor = "rgba(0, 247, 34, 1)";

        // Remove video source to show only green background (placeholder logic)
        video.removeAttribute("src");
        video.load();

        // Signal ready
        window.templateReady = true;
        document.body.setAttribute("data-ready", "true");
      }}

      if (video.readyState >= 1) {{
        processVideo();
      }} else {{
        video.addEventListener("loadedmetadata", processVideo);
      }}

      window.addEventListener("load", function () {{
        if (!window.templateReady) {{
          processVideo();
        }}
      }});
    }})();
  </script>
</html>
"""

reel_template = {
    "page_name": "desi_standup",
    "template_type": "reel",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "reel_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text": {
                    "text_content": {"type": "text_area", "tag": "div", "class": "text-content"},
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
            },
            "image_edits": {
            },
            "video_edits":{
                "type": {"type":"default", "values": "video_overlay"},
                "class_name":{"type":"default","values":"main-video"},
                "padding":{"type":"default","values":-1665},
                "green_screen":{"type":"default","values":(0,247,34,1)},
                "add_gradient":{"type":"default","values":False},
            }
        },
    },
}