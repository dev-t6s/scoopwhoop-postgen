TEMPLATE_DESCRIPTION = """
"""

JSON_DESCRIPTION = """
"""

HEADLINE_SLIDE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Meme Grid Template</title>
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@900&display=swap"
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
        background-color: #333; /* Dark background for preview only */
      }}

      .container {{
        width: 1080px;
        height: 1350px; /* Square canvas */
        background-color: #000; /* Black background fills any empty space */
        position: relative;
        overflow: hidden;
      }}

      /* --- BACKGROUND GRID (2x2) --- */
      .image-grid {{
        display: grid;
        /* Strictly force 2 equal columns and 2 equal rows */
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: repeat(2, 1fr);
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1;
      }}

      .grid-item-wrapper {{
        /* Wrapper ensures the cell stays fixed size */
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        min-width: 0; /* Prevents grid blowout */
        min-height: 0; /* Prevents grid blowout */
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
        top: 40px;
        right: 40px;
        width: 180px;
        height: auto;
        z-index: 20;
        object-fit: contain;
      }}    

      /* --- CENTERED TEXT OVERLAY --- */
      .text-overlay {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 100%;
        padding: 0 20px;
        box-sizing: border-box;
        z-index: 30;
        display: flex;
        justify-content: center;
        text-align: center;
        pointer-events: none; /* Allows clicking through text if needed */
      }}

      .meme-text {{
        font-family: "Inter", sans-serif;
        font-weight: 900;
        font-size: 64px;
        color: #ffffff;
        line-height: 1.15;
        text-transform: lowercase;
        margin: 0;

        /* The iconic heavy black outline */
        -webkit-text-stroke: 8px #000000;
        paint-order: stroke fill;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <!-- 2x2 Image Grid -->
      <div class="image-grid">
        <!-- Box 1 -->
        <div class="grid-item-wrapper">
          <img src="{background_image}" alt="Grid Image 1" class="grid-item" />
        </div>
        <!-- Box 2 -->
        <div class="grid-item-wrapper">
          <img src="{box_image_1}" alt="Grid Image 2" class="grid-item" />
        </div>
        <!-- Box 3 -->
        <div class="grid-item-wrapper">
          <img src="{box_image_2}" alt="Grid Image 3" class="grid-item" />
        </div>
        <!-- Box 4 -->
        <div class="grid-item-wrapper">
          <img src="{box_image_3}" alt="Grid Image 4" class="grid-item" />
        </div>
      </div>

      <!-- Logo (Top Right) -->
      <img src="{logo_image}" alt="Logo" class="brand-logo" />

      <!-- Centered Text -->
      <div class="text-overlay">
        {headline}
      </div>
    </div>
  </body>
</html>
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
"""

thumbnail_template = {
    "page_name": "gls",
    "template_type": "thumbnail_4",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_SLIDE_HTML_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "headline": {"type": "text_area", "tag": "h1", "class": "meme-text"},
            },
            "assets":{
                "background_image": {"type":"bytes", "file_type":"png"},
                "box_image_1": {"type":"bytes", "file_type":"png", "default": "box_image_1.png"},
                "box_image_2": {"type":"bytes", "file_type":"png", "default": "box_image_1.png"},
                "box_image_3": {"type":"bytes", "file_type":"png", "default": "box_image_1.png"},
                "logo_image": {"default": "logo.png"},
            },
            "image_edits": {
                "crop_type":{"type":"dropdown", "values":["cover", "contain"], "default":"cover"},
            },
            "video_edits":{
            }
        },
    },
}