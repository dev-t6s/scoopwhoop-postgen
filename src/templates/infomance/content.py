TEMPLATE_DESCRIPTION = """
Infomance Content: This template creates professional news content slides for social media posts. It features a clean black and red design with the Infomance branding, showcasing a large central image with accompanying text content. The layout is optimized for news stories and information sharing with clear typography and professional presentation.
The template focuses on visual storytelling with minimal text overlay on a striking image background.
NOTE: Only one slide is required for this template.
"""

JSON_DESCRIPTION = """
This template has the following slides/sections:
Infomance Content Slide:
  ### Attributes:
  - image_description: A one line description of the image you would like to use for the slide.
    EX: A photo of street dogs or relevant news imagery.
  - content_text: The main news content text.
    Ex: **Street Dogs to be released** back to their localities, says supreme court Max 1-2 sentences

  ### Text Input:
  ```json
    {{
      "name": "infomance_content_slide",
      "image_description": "str",
      "text": {{
      "content_text": "str"
      }}  
    }}
  ```
NOTE: 
- DO NOT COMPLICATE THE IMAGE DESCRIPTIONS, KEEP IT SIMPLE AND DIRECT.
- Focus on clear, impactful messaging that works well with the image
- Keep content concise for maximum visual impact
"""

CONTENT_HTML_TEMPLATE = """<!DOCTYPE html>
<html>
  <head>
    <title>Infomance</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");

      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        display: flex;
        justify-content: center;
        min-height: 100vh;
        background-color: #000000;
      }}    

      .container {{
        width: 1080px;
        background-color: #ffffff;
        height: 1350px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
      }}

      .red-bar {{
        background-color: #d93a49;
        height: 25px;
        width: 100%;
        position: relative;
      }}
      .black-bar {{
        background-color: #000000;
        height: 50px;
        width: 100%;
        position: relative;
      }}

      .logo-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0;
        overflow: hidden;
      }}
      .footer-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0;
        position: relative;
        top: -26px;
        z-index: 10;
      }}
      .logo {{
        font-family: "Times New Roman", Times, serif;
        color: #ffffff;
        background-color: #d93a49;
        font-size: 50px;
        font-weight: 600;
        letter-spacing: 2px;
        padding: 1px 15px;
        margin: 0;
      }}

      .header {{
        background-color: #ffffff;
        text-align: center;
        position: relative;
        display: flex;
        flex-direction: column;
        border-bottom: 1px solid #ffffff;
        padding-bottom: 20px;
      }}

      .headline {{
        text-align: center;
        padding: 20px 20px 10px 20px;
        background-color: #ffffff;
        font-family: "Poppins", sans-serif;
        font-weight: 700;
        font-size: 70px;
        color: #d93a49;
        margin: 0;
        line-height: 1.2;
      }}

      .image-banner {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0;
        overflow: hidden;
      }}

      .main-image {{
        width: 100%;
        height: auto;
        object-fit: contain;
        display: block;
        background-color: #000000;
      }}

      .text-content-container {{
        padding: 0px 20px 0px 20px;
        background-color: #ffffff;
        text-align: center;
        font-family: "Poppins", sans-serif;
        font-weight: 700;
        font-size: 57px;
        color: #333;
        margin: 0;
        line-height: 1.6;
      }}

      .text-content {{
        padding: 30px 20px 40px 20px;
        background-color: #ffffff;
        text-align: center;
        font-family: "Poppins", sans-serif;
        font-weight: 700;
        font-size: 57px;
        color: #333;
        margin: 0;
        line-height: 1.6;
      }}

      .text-content .yellow {{
        color: #d93a49;
      }}

      .yellow {{
        color: #d93a49;
      }}

      .source {{
        font-family: "Poppins", sans-serif;
        font-size: 40px;
        font-weight: 800;
        margin-top: 0;
        margin-bottom: 40px;
        text-align: right;
      }}

      .footer{{
        background-color: #000000;
      }}

      .footer-link {{
        font-family: "Poppins", sans-serif;
        font-weight: 300;
        font-size: 35px;
        background-color: #d93a49;
        padding: 0px 10px;
        letter-spacing: 1px;
        border-radius: 5px;
        text-align: center;
        color: white;
        text-decoration: none;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <div class="red-bar"></div>
        <div class="logo-container">
          <p class="logo">Infomance</p>
        </div>
      </div>

      <div class="image-banner">
        <img src="{background_image}" alt="Main Image" class="main-image" />
      </div>

      <div class="text-content-container">
        {content_text}
      </div>

      <div class="footer">
        <div class="footer-container">
          <div class="footer-link">www.infomance.com</div>
        </div>
      </div>
    </div>
  </body>
</html>
"""

CONTENT_OVERLAY_TEMPLATE = """<!DOCTYPE html>
<html>
  <head>
    <title>Infomance</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");

      body,
      html {{
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        display: flex;
        justify-content: center;
        min-height: 100vh;
        background-color: #000000;
      }}    

      .container {{
        width: 1080px;
        background-color: #ffffff;
        height: 1350px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
      }}

      .red-bar {{
        background-color: #d93a49;
        height: 25px;
        width: 100%;
        position: relative;
      }}
      .black-bar {{
        background-color: #000000;
        height: 50px;
        width: 100%;
        position: relative;
      }}

      .logo-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0;
        overflow: hidden;
      }}
      .footer-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0;
        position: relative;
        top: -26px;
        z-index: 10;
      }}
      .logo {{
        font-family: "Times New Roman", Times, serif;
        color: #ffffff;
        background-color: #d93a49;
        font-size: 50px;
        font-weight: 600;
        letter-spacing: 2px;
        padding: 1px 15px;
        margin: 0;
      }}

      .header {{
        background-color: #ffffff;
        text-align: center;
        position: relative;
        display: flex;
        flex-direction: column;
        border-bottom: 1px solid #ffffff;
        padding-bottom: 20px;
      }}

      .headline {{
        text-align: center;
        padding: 20px 20px 10px 20px;
        background-color: #ffffff;
        font-family: "Poppins", sans-serif;
        font-weight: 700;
        font-size: 70px;
        color: #d93a49;
        margin: 0;
        line-height: 1.2;
      }}

      .image-banner {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0;
        overflow: hidden;
      }}

      .main-video {{
        width: 100%;
        height: auto;
        object-fit: contain;
        display: block;
      }}

      .text-content-container {{
        padding: 0px 20px 0px 20px;
        background-color: #ffffff;
        text-align: center;
        font-family: "Poppins", sans-serif;
        font-weight: 700;
        font-size: 57px;
        color: #333;
        margin: 0;
        line-height: 1.6;
      }}

      .text-content {{
        padding: 30px 20px 40px 20px;
        background-color: #ffffff;
        text-align: center;
        font-family: "Poppins", sans-serif;
        font-weight: 700;
        font-size: 57px;
        color: #333;
        margin: 0;
        line-height: 1.6;
      }}

      .text-content .yellow {{
        color: #d93a49;
      }}
      .yellow {{    
        color: #d93a49;
      }}

      .source {{
        font-family: "Poppins", sans-serif;
        font-size: 40px;
        font-weight: 800;
        margin-top: 0;
        margin-bottom: 40px;
        text-align: right;
      }}

      .footer{{
        background-color: #000000;
      }}

      .footer-link {{
        font-family: "Poppins", sans-serif;
        font-weight: 300;
        font-size: 35px;
        background-color: #d93a49;
        padding: 0px 10px;
        letter-spacing: 1px;
        border-radius: 5px;
        text-align: center;
        color: white;
        text-decoration: none;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <div class="red-bar"></div>
        <div class="logo-container">
          <p class="logo">Infomance</p>
        </div>
      </div>

      <div class="image-banner">
        <video src="{background_video}" autoplay muted loop class="main-video"></video>
      </div>

      <div class="text-content-container">
        {content_text}
      </div>

      <div class="footer">
        <div class="footer-container">
          <div class="footer-link">www.infomance.com</div>
        </div>
      </div>
    </div>
  </body>
</html>
"""

infomance_content_template = {
    "page_name": "infomance",
    "template_type": "content",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "infomance_content_slide": {
            "html_template": CONTENT_HTML_TEMPLATE,
            "overlay_template": CONTENT_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "content_text": {"type": "text_area", "tag": "div", "class": "text-content"},
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
            },
            "image_edits": {},
            "video_edits":{
                "type": {"type":"default", "values": "video_overlay"},
                "class_name":{"type":"default","values":"main-video"},
                "padding":{"type":"default","values":258}
            }
        },
    },
}