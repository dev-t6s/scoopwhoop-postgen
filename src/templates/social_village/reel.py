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
    <title>Infomance</title>
    <style>
      /* Load Local Fonts */
      @font-face {{
        font-family: "Poppins";
        src: url("Poppins-Bold.ttf") format("truetype");
        font-weight: 700;
        font-style: normal;
      }}

      @font-face {{
        font-family: "Poppins";
        src: url("Poppins-Medium.ttf") format("truetype");
        font-weight: 500;
        font-style: normal;
      }}

      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: "Poppins", sans-serif;
        display: flex;
        justify-content: center;
        min-height: 100vh;
        background-color: white;
      }}

      .container {{
        width: 1080px;
        height: 1950px;
        background-color: #000000;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;

        /* ALIGNMENT LOGIC: */
        /* Centers content vertically */
        justify-content: center;
        /* Pushes the content down so it is 'below center' and clears logo space */
        padding-top: 50px;
        box-sizing: border-box;
      }}

      /* Logo Styling - Top Right */
      .logo-container {{
        position: absolute;
        top: -80px; /* Adjusted slightly so it's not cut off */
        right: -40px;
        z-index: 20;
        width: 250px;
        height: auto;
      }}

      .logo-img {{
        width: 100%;
        height: auto;
        display: block;
      }}

      /* New Wrapper to group Text and Video together */
      .content-wrapper {{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        /* This gap controls the distance between Text and Video */
        gap: 40px;
        z-index: 10;
      }}

      /* Text Content Styling */
      .text-content-container {{
        /* Removed huge top padding, now handled by container alignment */
        padding: 0 60px;
        background-color: transparent;
        text-align: center;
        width: 100%;
        box-sizing: border-box;
      }}

      .text-content {{
        font-family: "Poppins", sans-serif;
        font-weight: 700;
        font-size: 42px;
        color: #ffffff;
        margin: 0;
        line-height: 1.4;
      }}

      /* Highlight Color */
      .yellow {{
        color: #f5c518;
      }}

      /* Video Container */
      .image-banner {{
        display: flex;
        justify-content: center;
        align-items: flex-start;
        padding: 0;
        overflow: hidden;
        object-fit: cover;
        width: 100%;
      }}

      .main-video {{
        width: 100%;
        height: auto;
        object-fit: cover;
        display: block;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Logo in Upper Right Corner -->
      <div class="logo-container">
        <img src="logo.png" alt="Logo" class="logo-img" />
      </div>

      <!-- Wrapper to keep Text and Video grouped and centered together -->
      <div class="content-wrapper">
        <!-- Text Overlay Area -->
        <div class="text-content-container">
          {text_content}
        </div>

        <!-- Video Area -->
        <div class="image-banner">
          <video src="4.mp4" class="main-video"></video>
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
          const aspectRatio = height / width;
          const displayHeight = containerWidth * aspectRatio;

          // Set explicit dimensions
          video.style.width = containerWidth + "px";
          video.style.height = displayHeight + "px";
        }}

        // Set background color to green (as per original template logic)
        video.style.backgroundColor = "rgba(0, 247, 34, 1)";

        // Remove video source to show only green background (placeholder logic)
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
        if (!window.templateReady) {{
          processVideo();
        }}
      }});
    }})();
  </script>
</html>
"""

reel_template = {
    "page_name": "social_village",
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