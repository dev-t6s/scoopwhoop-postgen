TEMPLATE_DESCRIPTION = """
Twitter Post: This Indian Standup template creates authentic-looking Twitter post images for sharing funny moments, tweets. It replicates the Twitter interface with user profile information, verified badge, three-dot menu, tweet text, and optional media attachments. The template is optimized for 1080x1350 dimensions and maintains Twitter's visual design language with proper spacing, typography, and UI elements.
The template includes customizable user information (name, handle, profile picture) and supports both text-only tweets and tweets with image/video attachments
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Twitter Post Slide:
  ### Attributes:
  - This creates a realistic Twitter post interface with user profile and tweet content, perfect for funny standup moments and comedy tweets.
  
  - user_name: The display name of the Twitter user (can include emojis)
    EX: "Biswa Kalyan Rath", "Kunal Kamra", "Zakir Khan"
  
  - user_handle: The Twitter handle/username starting with @
    EX: "@biswa", "@kunalkamra88", "@aapkarakshak"
  
  - tweet_text: The main tweet content/message - funny observations, standup jokes, or relatable comedy
    EX: "When your mom says 'paise hi paise honge' after you crack a joke", "POV: You're explaining memes to your parents"
  - verified_badge: Whether to show the blue verified checkmark (use the VERIFIED_BADGE constant or empty string)

  ### Text Input:
    {{
      "name": "indian_standup_post",
      "image_description": "str",
      "text":{{
      "user_name": "str",
      "user_handle": "str", 
      "tweet_text": "str",
      "add_verified_badge": "True/False",
      "add_three_dots": "True/False"
      }}
    }}

NOTE: 
- The template automatically includes Twitter UI elements like the three-dot menu and proper styling
- Profile picture should be square/circular format for best results
- Tweet text should be concise, funny, and engaging
- Use verified_badge for verified comedian accounts or public figures
"""

VERIFIED_BADGE = """
<svg
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                version="1.1"
                width="28"
                height="28"
                viewBox="0 0 256 256"
                xml:space="preserve"
              >
                <g
                  style="
                    stroke: none;
                    stroke-width: 0;
                    stroke-dasharray: none;
                    stroke-linecap: butt;
                    stroke-linejoin: miter;
                    stroke-miterlimit: 10;
                    fill: none;
                    fill-rule: nonzero;
                    opacity: 1;
                  "
                  transform="translate(1.4065934065934016 1.4065934065934016) scale(2.81 2.81)"
                >
                  <path
                    d="M 30.091 10.131 L 30.091 10.131 c 5.28 -13.046 23.695 -13.207 29.202 -0.255 l 0 0 l 0 0 c 12.959 -5.491 26.093 7.416 20.829 20.469 l 0 0 l 0 0 c 13.046 5.28 13.207 23.695 0.255 29.202 l 0 0 l 0 0 c 5.491 12.959 -7.416 26.093 -20.469 20.829 l 0 0 l 0 0 c -5.28 13.046 -23.695 13.207 -29.202 0.255 l 0 0 l 0 0 C 17.748 86.122 4.613 73.215 9.878 60.162 l 0 0 l 0 0 C -3.169 54.881 -3.33 36.467 9.623 30.96 l 0 0 l 0 0 C 4.131 18.001 17.038 4.866 30.091 10.131 L 30.091 10.131 z"
                    style="
                      stroke: none;
                      stroke-width: 1;
                      stroke-dasharray: none;
                      stroke-linecap: butt;
                      stroke-linejoin: miter;
                      stroke-miterlimit: 10;
                      fill: rgb(0, 150, 241);
                      fill-rule: nonzero;
                      opacity: 1;
                    "
                    transform=" matrix(1 0 0 1 0 0) "
                    stroke-linecap="round"
                  />
                  <polygon
                    points="39.66,63.79 23.36,47.76 28.97,42.05 39.3,52.21 59.6,29.58 65.56,34.93 "
                    style="
                      stroke: none;
                      stroke-width: 1;
                      stroke-dasharray: none;
                      stroke-linecap: butt;
                      stroke-linejoin: miter;
                      stroke-miterlimit: 10;
                      fill: rgb(255, 255, 255);
                      fill-rule: nonzero;
                      opacity: 1;
                    "
                    transform="  matrix(1 0 0 1 0 0) "
                  />
                </g>
              </svg>
"""

THREE_DOTS = """
<div class="three-dots">
          <div class="dot"></div>
          <div class="dot"></div>
          <div class="dot"></div>
        </div>
"""

HEADLINE_SLIDE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Twitter Post Template</title>
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap"
      rel="stylesheet"
    />
    <style>
      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: "Inter", sans-serif;

        display: flex;
        justify-content: center;
        align-items: center;
      }}

      .container {{
        width: 1080px;
        height: 1350px;
        background-color: #ffffff;
        padding: 85px;
        box-sizing: border-box;
        position: relative;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
      }}
      /* --- UPDATED LOGO STYLES --- */
      .brand-logo {{
        position: absolute;
        /* Aligned with container padding */
        top: 65px;
        left: 35px;
        width: 110px; /* Increased slightly for visibility */
        height: auto;
        z-index: 10;
      }}
      /* ----------------------- */

      .tweet-header {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-shrink: 0;
        padding-bottom: 10px;

        margin-top: 120px;
      }}

      .header-left {{
        display: flex;
        align-items: center;
      }}

      .three-dots {{
        display: flex;
        flex-direction: column;
        gap: 6px;
        padding-right: 0px;
        padding-bottom: 0px;
      }}

      .dot {{
        width: 8px;
        height: 8px;
        background-color: #c0c9c8;
        border-radius: 50%;
      }}

      .profile-pic {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        margin-right: 24px;
        object-fit: cover;
      }}

      .user-info {{
        display: flex;
        flex-direction: column;
        line-height: 1.2;
      }}

      .user-name {{
        font-weight: 700;
        font-size: 36px;
        color: #0f1419;
        display: flex;
        align-items: center;
        gap: 8px;
      }}

      .verified-badge {{
        width: 28px;
        height: 28px;
        background-color: #1d9bf0;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
      }}

      .verified-badge svg {{
        width: 16px;
        height: 16px;
        fill: white;
      }}

      .verified-badge::after {{
        /* Removed the CSS content checkmark since you have an SVG */
        content: none;
      }}

      .user-handle {{
        font-size: 32px;
        color: #536471;
      }}

      .tweet-content {{
        display: flex;
        flex-direction: column;
        min-height: 0;
        align-items: flex-start;
        width: 100%;
      }}

      .tweet-text {{
        font-size: 42px;
        color: #0f1419;
        line-height: 1.3;
        margin: 25px 0 35px 0;
        word-wrap: break-word;
        flex-shrink: 0;
        text-align: left;
      }}

      .tweet-media {{
        border-radius: 24px;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
      }}

      .tweet-media.cover {{
        height: auto;
        width: 100%;
      }}

      .tweet-image {{ 
        width: 100%;
        height: auto;
        object-fit: cover;
        display: block;
        border-radius: 24px;
      }}

      .tweet-image.contain {{
        object-fit: contain;
        width: auto;
        height: 100%;
      }}

      .tweet-image.cover {{
        object-fit: cover;
        width: 100%;
        height: 100%; /* Fill the container completely */
      }}
    </style>
  </head>
  <body>
    <div class="container">

    <!-- Your original Logo asset -->
      <img src="logo.png" alt="Logo" class="brand-logo" />
      <div class="tweet-header">
        <div class="header-left">
          <img
            src="{profile_pic}"
            alt="Profile Picture"
            class="profile-pic"
          />
          <div class="user-info">
            <span class="user-name">
            {user_name}
            {add_verified_badge}
            </span>
            {user_handle}
          </div>
        </div>
        {add_three_dots}
      </div>
      <div class="tweet-content">
        {tweet_text}
        <div class="tweet-media">
          <img src="{background_image}" alt="Tweet Media" class="tweet-image" />
        </div>
      </div>
    </div>
  </body>
  <script>
    // Global crop type - change this to 'contain' or 'cover'
    const CROP_TYPE = "{crop_type}"; // Change to 'cover' to test different behavior

    function alignWidths() {{
      const tweetImage = document.querySelector(".tweet-image");
      const tweetVideo = document.querySelector(".tweet-video");
      const tweetHeader = document.querySelector(".tweet-header");
      const tweetText = document.querySelector(".tweet-text");

      // Determine which media element exists
      const mediaElement = tweetImage || tweetVideo;

      if (mediaElement && tweetHeader && tweetText) {{
        // Apply crop type class to image and media container
        if (tweetImage) {{
          tweetImage.className = `tweet-image ${{CROP_TYPE}}`;
          const tweetMedia = document.querySelector(".tweet-media");
          if (tweetMedia) {{
            tweetMedia.className = `tweet-media ${{CROP_TYPE}}`;
          }}
        }}

        if (CROP_TYPE === "contain") {{
          // For contain mode: align widths based on image dimensions (current behavior)
          function setWidths() {{
            const mediaWidth = mediaElement.offsetWidth;
            tweetHeader.style.width = mediaWidth + "px";
            tweetText.style.width = mediaWidth + "px";
          }}

          // Handle different media types
          if (tweetImage) {{
            // For images
            if (tweetImage.complete && tweetImage.naturalWidth > 0) {{
              setWidths();
            }} else {{
              tweetImage.onload = setWidths;
            }}
          }} else if (tweetVideo) {{
            // For videos
            if (tweetVideo.readyState >= 2) {{
              // Video metadata is loaded
              setWidths();
            }} else {{
              tweetVideo.addEventListener("loadedmetadata", setWidths);
            }}
          }}
        }} else if (CROP_TYPE === "cover") {{
          // For cover mode: image fills container, header and text use full container width
          const containerWidth =
            document.querySelector(".container").offsetWidth - 170; // Account for padding
          tweetHeader.style.width = containerWidth + "px";
          tweetText.style.width = containerWidth + "px";
        }}
      }}
    }}

    // Run when DOM is loaded
    document.addEventListener("DOMContentLoaded", alignWidths);

    // Run when window is resized (in case of responsive changes)
    window.addEventListener("resize", alignWidths);
  </script>
</html>
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Twitter Post Template</title>
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap"
      rel="stylesheet"
    />
    <style>
      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: "Inter", sans-serif;

        display: flex;
        justify-content: center;
        align-items: center;
      }}

      .container {{
        width: 1080px;
        height: 1920px;
        background-color: #ffffff;
        padding: 85px;
        box-sizing: border-box;
        position: relative;

        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
      }}

      /* --- UPDATED LOGO STYLES --- */
      .brand-logo {{
        position: absolute;
        /* Aligned with container padding */
        top: 65px;
        left: 35px;
        width: 110px; /* Increased slightly for visibility */
        height: auto;
        z-index: 10;
      }}
      /* ----------------------- */

      .tweet-header {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-shrink: 0;
        padding-bottom: 10px;
        margin-top: 120px;
      }}

      .header-left {{
        display: flex;
        align-items: center;
      }}

      .three-dots {{
        display: flex;
        flex-direction: column;
        gap: 6px;
        padding-right: 0px;
        padding-bottom: 0px;
      }}

      .dot {{
        width: 8px;
        height: 8px;
        background-color: #c0c9c8;
        border-radius: 50%;
      }}

      .profile-pic {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        margin-right: 24px;
        object-fit: cover;
      }}

      .user-info {{
        display: flex;
        flex-direction: column;
        line-height: 1.2;
      }}

      .user-name {{
        font-weight: 700;
        font-size: 36px;
        color: #0f1419;
        display: flex;
        align-items: center;
        gap: 8px;
      }}

      .verified-badge {{
        width: 28px;
        height: 28px;
        background-color: #1d9bf0;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
      }}

      .verified-badge svg {{
        width: 16px;
        height: 16px;
        fill: white;
      }}

      .verified-badge::after {{
        /* Removed the CSS content checkmark since you have an SVG */
        content: none;
      }}

      .user-handle {{
        font-size: 32px;
        color: #536471;
      }}

      .tweet-content {{
        display: flex;
        flex-direction: column;
        min-height: 0;
        align-items: flex-start;
        width: 100%;
      }}

      .tweet-text {{
        font-size: 42px;
        color: #0f1419;
        line-height: 1.3;
        word-wrap: break-word;
        flex-shrink: 0;
        text-align: left;
      }}

      .tweet-media {{
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
      }}

      .tweet-video {{
        width: 100%;
        display: block;
        object-fit: cover;
        background-color: rgba(128,128,128,1);
      }}
    </style>
  </head>
  <body>
    <div class="container">
        <!-- Your original Logo asset -->
      <img src="logo.png" alt="Logo" class="brand-logo" />
      <div class="tweet-header">
        <div class="header-left">
          <img src="{profile_pic}" alt="Profile Picture" class="profile-pic" />
          <div class="user-info">
            <span class="user-name">
              {user_name}
              {add_verified_badge}
            </span>
            {user_handle}
          </div>
        </div>
        {add_three_dots}
      </div>
      <div class="tweet-content">
          {tweet_text}
        <div class="tweet-media">
          <video src="{background_video}" alt="Tweet Media" class="tweet-video" />
        </div>
      </div>
    </div>
  </body>
  <script>
    (function () {{
      const video = document.querySelector(".tweet-video");

      function processVideo() {{
        // Get video dimensions
        const width = video.clientWidth;
        const height = video.clientHeight;

        const containerWidth = Math.min(1080, width);
        const containerHeight = Math.min(1920, height);

        // Set explicit dimensions
        video.style.width = width + "px";
        video.style.height = height + "px";

        // Set background color to green
        video.style.backgroundColor = "rgba(128,128,128,1)";

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

tweet_image_template = {
    "page_name": "indian_standup",
    "template_type": "tweet_image",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "indian_standup_post": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "user_name": {"type": "text", "tag": "span", "class": ""},
                    "user_handle": {"type": "text", "tag": "span", "class": "user-handle"},
                    "tweet_text": {"type": "text_area", "tag": "p", "class": "tweet-text"},
                    "add_verified_badge": {"type": "checkbox", "html_snippet": VERIFIED_BADGE},
                    "add_three_dots": {"type": "checkbox", "html_snippet": THREE_DOTS},
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
                "profile_pic": {"type":"bytes", "file_type":"png", "default": "profile_pic.png"},
            },
            "image_edits": {
                "crop_type":{"type":"dropdown", "values":["cover", "contain"], "default":"cover"},
            },
            "video_edits":{
                "type": {"type":"default", "values": "video_overlay"},
                "class_name":{"type":"default","values":"tweet-media"},
                "padding":{"type":"default","values":-1665},
                "green_screen":{"type":"default","values":(128,128,128,1)},
            }
        },
    },
}