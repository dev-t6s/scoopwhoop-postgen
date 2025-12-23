TEMPLATE_DESCRIPTION = """
Reel: This Social Village template creates engaging vertical video content for social media reels and stories. It features a black background with bold white text overlay (with yellow highlighting capability) positioned above the main video content, and the Social Village branding in the top right. The template is optimized for 1080x1950 dimensions (Instagram Reels/Stories format) and designed for entertainment, lifestyle content, celebrity moments, trending topics, and shareable viral content.
The template combines clean text presentation with video content - ideal for creating engaging reels that capture attention and drive shares.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Reel Slide:
  ### Attributes:
  - This should be an engaging reel for entertainment and lifestyle content. Must be attention-grabbing and shareable.
    EX: A celebrity moment, trending dance video, lifestyle tip demonstration, funny moment compilation.
  
  - video_description: A one line description of the video you would like to use for the reel.
    EX: "A celebrity dancing at an event", "A funny reaction video", "A lifestyle hack demonstration"
  
  - text_content: The main text overlay displayed above the video (bold white text with yellow highlighting capability).
    EX: "When **Deepika Padukone** walked into the room like a queen 👑", "This **life hack** will change everything", "**Viral moment** everyone is talking about"
    Note: Use **str** to highlight important words in yellow. Use \\n for line breaks.

  ### Text Input:
    {{
      "name": "reel_slide",
      "video_description": "str",
      "text": {{
      "text_content": "str"
      }}
    }}

NOTE: 
- Use **str** to highlight important words in yellow for emphasis. Use \\n for line breaks if needed.
- DO NOT COMPLICATE THE VIDEO DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
- Content should be entertaining, relatable, and focused on lifestyle, celebrities, trends, and viral moments.
- Text should be concise and engaging to work well with the video content.
- Perfect for creating shareable reels that capture attention in the first few seconds.
"""

HEADLINE_SLIDE_HTML_TEMPLATE = """
"""


HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <title>Indian Standup</title>
    <style>
      /* Load Roboto Font */
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@500;700&display=swap");

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
        height: 1920px;
        background-color: white; /* Light gray background */
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        /* Pushing content slightly below mathematical center */
        /* padding-top: 150px; */
        box-sizing: border-box;
      }}

      /* Wrapper to group Text and Video */
      .content-wrapper {{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        gap: 30px; /* Space between text and video */
        z-index: 10;
      }}

      /* Main Text Styling */
      .text-content {{
        font-family: "Roboto", sans-serif;
        font-weight: 700; /* Bold */
        font-size: 70px;
        color: #000000;
        margin: 0;
        line-height: 1.2;
        text-align: center;
      }}

      /* Video Container - Relative positioning needed for watermark overlay */
      .image-banner {{
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0;
        overflow: hidden;
        width: 1080px;
        background-color: #000;
      }}    

      .main-video {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
      }}

      /* Watermark Styling - Overlaid on video */
      .watermark-overlay {{
        position: absolute;
        bottom: 40px; /* Positioned near bottom */
        left: 0;
        right: 0;
        text-align: center;
        z-index: 20; /* Ensures it is "above" the video */

        font-family: "Roboto", sans-serif;
        font-weight: 500; /* Medium weight looks best for watermarks */
        font-size: 35px;
        color: rgba(255, 255, 255, 0.7); /* White with slight transparency */
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <div class="content-wrapper">
        <!-- Main Text -->
        {text_content}

        <!-- Video Area with Watermark -->
        <div class="image-banner">
          <video src="{background_video}" class="main-video"></video>

          <!-- Watermark Layered Above Video -->
          <div class="watermark-overlay">@indian.standup</div>
        </div>
      </div>
    </div>
  </body>
  <script>
    (function () {{
      const video = document.getElementsByClassName("main-video")[0];

      function processVideo() {{
        // Get video dimensions
        const width = video.videoWidth;
        const height = video.videoHeight;

        // Calculate the display height based on container width (1080px)
        const containerWidth = 1080;

        console.log(width, height);

        // If metadata isn't loaded yet, these might be 0
        if (width && height) {{
          {{
            const aspectRatio = height / width;
            const displayHeight = containerWidth * aspectRatio;

            // Set explicit dimensions
            video.style.width = containerWidth + "px";
            video.style.height = displayHeight + "px";
          }}
        }}
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
    "page_name": "indian_standup",
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
            }
        },
    },
}