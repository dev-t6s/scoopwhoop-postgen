TEMPLATE_DESCRIPTION = """
"""

JSON_DESCRIPTION = """
"""


THUMBNAIL_SLIDE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vertical Split Meme Template</title>

    <!-- Google Fonts: Poppins (Bold & Medium) -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;700&display=swap"
      rel="stylesheet"
    />

    <style>
      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: "Poppins", sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #222;
      }}

      .container {{
        width: 1080px;
        height: 1350px; /* Portrait 4:5 Aspect Ratio */
        background-color: #000;
        position: relative;
        overflow: hidden;
      }}

      /* --- VERTICAL SPLIT GRID --- */
      .image-grid {{
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr);
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1;
      }}

      /* Wrapper to hold the image */
      .grid-item-wrapper {{
        width: 100%;
        height: 100%;
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
      }}

      .grid-item {{
        width: 100%;
        height: 100%;
        object-fit: {crop_type};
        display: block;
      }}

      /* --- LOGO --- */
      .brand-logo {{
        position: absolute;
        top: -60px;
        right: -40px;
        width: 180px;
        height: auto;
        z-index: 20;
        object-fit: contain;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.5));
      }}

      /* --- CENTERED TEXT --- */
      .text-overlay {{      
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 90%;
        z-index: 30;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
      }}

      .headline {{
        font-family: "Poppins", sans-serif;
        font-weight: 700;
        font-size: 64px;
        color: #ffffff;
        line-height: 1.25;
        margin: 0;

        /* 1. The Black Lines (Outline) */
        -webkit-text-stroke: 3px #000000;
        /* Ensures the stroke doesn't eat into the letters */
        paint-order: stroke fill;

        /* 2. Darker, Harder Shadow */
        text-shadow: 4px 4px 0px #000000,
          /* Hard drop shadow */ 0px 0px 40px rgba(0, 0, 0, 1); /* Intense dark glow behind */
      }}

      /* Yellow Highlight */
      .yellow {{
        color: #f5c519;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- Grid with Image Wrappers -->
      <div class="image-grid">
        <!-- Top Image -->
        <div class="grid-item-wrapper">
          <img src="{background_image}" alt="Top Image" class="grid-item" />
        </div>

        <!-- Bottom Image -->
        <div class="grid-item-wrapper">
          <img src="{box_image_1}" alt="Bottom Image" class="grid-item" />
        </div>
      </div>

      <!-- Logo -->
      <img src="{logo_image}" alt="Logo" class="brand-logo" />

      <!-- Centered Text -->
      <div class="text-overlay">
        {headline}
      </div>
    </div>
  </body>
</html>
"""

THUMBNAIL_SLIDE_OVERLAY_TEMPLATE = """
"""

thumbnail_template = {
    "page_name": "social_village",
    "template_type": "thumbnail",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": THUMBNAIL_SLIDE_HTML_TEMPLATE,
            "overlay_template": THUMBNAIL_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "h1", "class": "headline"},
            },
            "assets":{
                "background_image": {"type":"bytes", "file_type":"png"},
                "box_image_1": {"type":"bytes", "file_type":"png", "default": "box_image_1.png"},
                "logo_image": {"default": "logo.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"], "default": "cover"},
            },
            "video_edits":{
            }
        },
    },
}