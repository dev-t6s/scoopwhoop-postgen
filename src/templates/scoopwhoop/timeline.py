TEMPLATE_DESCRIPTION = """
**Template Name:** TimeLine

**Primary Goal:** To generate content for a multi-slide visual storyboard that presents chronological stories, updates, or milestones. The output must follow a strict JSON format for each slide, detailing text and image descriptions.

**General Instructions:**
*   Adhere strictly to the specified HTML tags and class names in the examples.
*   Pay close attention to the word and line count limits for each field.
*   Image descriptions should be concise yet evocative, suitable for an AI image generator.
*   Ensure all text is proofread and fits the narrative context of a timeline.
*   body_text should not be more than 2-3 lines of content [This is so that the text does not overflow the timeline slide]
NOTE:
* Use Date and Time in the format of "Time, Date" (e.g., `10:30 PM, 9TH JUNE`), To explain each event in the timeline.
- 3-6 slides is the maximum number of slides you can have.
"""

JSON_DESCRIPTION = """
### Slide / Section Definitions

**1. Headline Slide**
*   **Purpose:** The opening slide of the storyboard. It must be eye-catching and create a strong first impression of the story.

### Attributes:
*   **`image_description`:** A clear, one-line description of the desired background image that captures the mood, subject and style - for example, a movie headline could reference the official poster, key actors or set photos, while news stories should focus on actual event stills and photos.
(e.g., "Special Ops 2025 India Poster", "Rahul Gandhi's Speech Portrait Shot").
*   **`first_line`:** The main headline of the story. Must be a powerful statement of **no more than 3-4 words**. Use plain text only.
*   **`highlight`:** The highlighted keyword or phrase of the headline. Must be **no more than 3-4 words**.
*   **`sub_heading`:** A concise subheading that provides additional context to the headline. **Must not exceed one line or 8-10 words.** Use plain text only.

### Text Input Structure:
    {{
      "name": "headline_slide",
      "image_description": "str",
      "text": {{
        "first_line": "str",
        "highlight": "str",
        "sub_heading": "str"
      }}
    }}

**2. Timeline Start Slide**
*   **Purpose:** This slide marks the first event or the beginning of the chronological sequence.

### Attributes:
*   **`image_description`:** A clear, one-line description of the desired background image that captures the mood, subject and style - for example, a movie headline could reference the official poster, key actors or set photos, while news stories should focus on actual event stills and photos.
(e.g., "Special Ops 2025 India Poster", "Rahul Gandhi's Speech Portrait Shot").
*   **`timeline_highlight`:** The timestamp for the event. **Must be in a "Time, Date" format** (e.g., `10:30 PM, 9TH JUNE`). This field should only contain the time and date. 
*   **`body_text`:** The main descriptive text for this event. Expand on the story in **2-3 lines** not more than that, explaining what happened at this point in time. Use plain text only.

### Text Input Structure:
    {{
      "name": "timeline_start_slide",
      "image_description": "str",
      "text": {{
        "timeline_highlight": "str",
        "body_text": "str"
      }}
    }}

**3. Timeline Middle Slide**
*   **Purpose:** This slide is for any subsequent event between the start and the end of the timeline. Use it for all intermediate milestones.

### Attributes:
*   **`image_description`:** A one-line description of an image relevant to this specific event in the timeline.
*   **`timeline_highlight`:** The timestamp for the event. **Must be in a "Time, Date" format** (e.g., `11:00 PM, 9TH JUNE`). This field should only contain the time and date. 
*   **`body_text`:** The main descriptive text for this event. Expand on the story in **2-3 lines** not more than that, explaining what happened at this point in time. Use plain text only.

### Text Input Structure:
    {{
      "name": "timeline_middle_slide",
      "image_description": "str",
      "text": {{
        "timeline_highlight": "str",
        "body_text": "str"
      }}
    }}

**4. Timeline End Slide**
*   **Purpose:** This is the concluding event of the timeline, used to wrap up the story or present the final milestone.

### Attributes:
*   **`image_description`:** A one-line description of an image relevant to this final event in the timeline.
*   **`timeline_highlight`:** The timestamp for the final event. **Must be in a "Time, Date" format** (e.g., `1:30 AM, 10TH JUNE`). This field should only contain the time and date.
*   **`body_text`:** The main descriptive text for this final event. Expand on the story's conclusion in **2-3 lines** not more than that. Use plain text only.

### Text Input Structure:
    {{
      "name": "timeline_end_slide",
      "image_description": "str",
      "text": {{
        "timeline_highlight": "str",
        "body_text": "str"
      }}
    }}
"""

HEADLINE_SLIDE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@700&display=swap");
      @import url("https://fonts.googleapis.com/css2?family=Golos+Text:wght@400..900&display=swap");
      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Bebas Neue", sans-serif;
        background-color: #f0f0f0;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        display: block;
        /* 'cover' scales the image to fill the container, cropping sides or top/bottom as needed */
        object-fit: {crop_type};
        /* Aligns the image. 'center' horizontally, and 25% from the top vertically to shift it up. */
        object-position: center 25%;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 110px; /* Increased logo size */
        filter: brightness(0) invert(1);
      }}

      .text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 1) 30%,
          rgba(0, 0, 0, 0) 100%
        );
        padding: 60px 40px 70px 40px;
        color: white;
        text-align: center;
      }}

      .first-line {{
        font-size: 110px;
        font-weight: 590;
        line-height: 1.2;
        display: block; /* Changed from inline-block */
        transform: scaleY(1.1);
      }}

      .highlight {{
        background-color: #fbe10a;
        color: black;
        padding: 5px 20px 0px 20px;
        font-size: 110px;
        display: block; /* Changed from inline-block */
        font-weight: 590;
        line-height: 1.2;
        transform: scaleY(1.1);
        /* The following properties help to center the block and fit the background to the text */
        margin-left: auto;
        margin-right: auto;
        width: -moz-fit-content;
        width: fit-content;
      }}

      .dashed-line {{
        width: 780px;
        height: 3px; /* thickness of line */
        margin: 28px auto 20px auto;
        background-image: repeating-linear-gradient(
          to right,
          white 0 3px,
          /* dash length */ transparent 10px 15px /* gap length */
        );
      }}

      .yellow {{
        color: #FBE10A;
      }}

      .sub-heading {{
        background-color: white;
        color: black;
        font-family: "Golos Text", sans-serif;
        font-weight: 700;
        font-size: 32px;
        padding: 8px 40px;
        display: block; /* Changed from inline-block */
        border-radius: 3px;
        letter-spacing: 0px;
        /* The following properties help to center the block and fit the background to the text */
        margin-left: auto;
        margin-right: auto;
        width: -moz-fit-content;
        width: fit-content;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <img src="{background_image}" class="background-image" />
      <div class="text-overlay">
        {first_line}
        {highlight}
        <div class="dashed-line"></div>
        {sub_heading}
      </div>
      </div>
    </div>
  </body>
</html>
"""

HEADLINE_SLIDE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@700&display=swap");
      @import url("https://fonts.googleapis.com/css2?family=Golos+Text:wght@400..900&display=swap");
      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Bebas Neue", sans-serif;
        background-color: #000000;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 110px; /* Increased logo size */
        filter: brightness(0) invert(1);
      }}

      .text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 1) 30%,
          rgba(0, 0, 0, 0) 100%
        );
        padding: 60px 40px 70px 40px;
        color: white;
        text-align: center;
      }}

      .first-line {{
        font-size: 110px;
        font-weight: 590;
        line-height: 1.2;
        display: block; /* Changed from inline-block */
        transform: scaleY(1.1);
      }}

      .highlight {{
        background-color: #fbe10a;
        color: black;
        padding: 5px 20px 0px 20px;
        font-size: 110px;
        display: block; /* Changed from inline-block */
        font-weight: 590;
        line-height: 1.2;
        transform: scaleY(1.1);
        /* The following properties help to center the block and fit the background to the text */
        margin-left: auto;
        margin-right: auto;
        width: -moz-fit-content;
        width: fit-content;
      }}

      .dashed-line {{
        width: 780px;
        height: 3px; /* thickness of line */
        margin: 28px auto 20px auto;
        background-image: repeating-linear-gradient(
          to right,
          white 0 3px,
          /* dash length */ transparent 10px 15px /* gap length */
        );
      }}

      .yellow {{
        color: #FBE10A;
      }}

      .sub-heading {{
        background-color: white;
        color: black;
        font-family: "Golos Text", sans-serif;
        font-weight: 700;
        font-size: 32px;
        padding: 8px 40px;
        display: block; /* Changed from inline-block */
        border-radius: 3px;
        letter-spacing: 0px;
        /* The following properties help to center the block and fit the background to the text */
        margin-left: auto;
        margin-right: auto;
        width: -moz-fit-content;
        width: fit-content;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <div class="text-overlay">
        {first_line}
        {highlight}
        <div class="dashed-line"></div>
        {sub_heading}
      </div>
      </div>
    </div>
  </body>
</html>
"""

TIMELINE_START_SLIDE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template - Modular Timeline</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@700&display=swap");
      @import url("https://fonts.googleapis.com/css2?family=Golos+Text:wght@400..900&display=swap");
      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Bebas Neue", sans-serif;
        background-color: #f0f0f0;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        display: block;
        /* 'cover' scales the image to fill the container, cropping sides or top/bottom as needed */
        object-fit: {crop_type};
        /* Aligns the image. 'center' horizontally, and 25% from the top vertically to shift it up. */
        object-position: center 25%;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 110px; /* Increased logo size */
        filter: brightness(0) invert(1);
      }}

      .text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.9) 10%,
          rgba(0, 0, 0, 0.9) 40%,
          rgba(0, 0, 0, 0.8) 50%,
          rgba(0, 0, 0, 0.5) 70%,
          rgba(0, 0, 0, 0) 100%
        );
        padding: 40px 80px 20px 80px;
        color: white;
        text-align: center;
         /* --- FIX STARTS HERE --- */
        height: 550px; /* This gives the overlay a fixed height. */
        box-sizing: border-box; /* This ensures padding is included in the height calculation, not added to it. */
        /* --- FIX ENDS HERE --- */
      }}

      /* --- MODULAR TIMELINE STYLES START --- */

      /* This is the flex container for the line-circle-line structure */
      .timeline-track {{
        display: flex;
        align-items: center;
        /* Use negative margin to break out of the parent's padding */
        margin: 0 -80px;
        margin-bottom: 50px; /* Creates space for the connector to connect */
      }}

      /* Style for the horizontal line elements */
      .line {{
        height: 3px;
        background-color: #fbe10a;
        flex-grow: 1; /* This makes the lines fill the available space */
      }}
      .no_line {{
        height: 3px;
        background-color: transparent;
        flex-grow: 1; /* This makes the lines fill the available space */
      }}

      /* Style for the circle element */
      .circle {{
        width: 25px;
        height: 25px;
        background-color: #fbe10a;
        border-radius: 50%;
        flex-shrink: 0; /* Prevents the circle from shrinking */
        position: relative;
      }}

      /* The vertical line connecting the circle down to the highlight box */
      .circle::after {{
        content: "";
        position: absolute;
        left: 50%;
        top: 100%;
        transform: translateX(-50%);
        width: 3px;
        height: 50px; /* Length of the connector line */
        background-color: #fbe10a;
      }}

      /* --- MODULAR TIMELINE STYLES END --- */

      .timeline-highlight {{
        background-color: #fbe10a;
        color: black;
        padding: 5px 20px 0px 20px;
        font-size: 95px;
        display: inline-block;
        /* margin-top: 2px; Closer to the first line */
        font-weight: 590;
        letter-spacing: 2px;
        /* line-height: 1.1; */
        transform: scaleY(1.1);
      }}
      .yellow {{
        color: #FBE10A;
      }}
      .body-text {{
        font-family: "Golos Text", sans-serif;
        font-weight: 400;
        font-size: 34px;
        line-height: 1.4;
        text-align: center;
        margin-top: 40px;
        color: #ffffff;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <img src="{background_image}" class="background-image" />
      <div class="text-overlay">
        <!-- MODIFIED TIMELINE STRUCTURE -->
        <div class="timeline-track">
          <div class="no_line"></div>
          <div class="circle"></div>
          <div class="line"></div>
        </div>
        {timeline_highlight}
        {body_text}
      </div>
    </div>
  </body>
</html>
"""

TIMELINE_START_SLIDE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template - Modular Timeline</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@700&display=swap");
      @import url("https://fonts.googleapis.com/css2?family=Golos+Text:wght@400..900&display=swap");
      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Bebas Neue", sans-serif;
        background-color: #f0f0f0;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 110px; /* Increased logo size */
        filter: brightness(0) invert(1);
      }}

      .text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.9) 10%,
          rgba(0, 0, 0, 0.9) 40%,
          rgba(0, 0, 0, 0.8) 50%,
          rgba(0, 0, 0, 0.5) 70%,
          rgba(0, 0, 0, 0) 100%
        );
        padding: 40px 80px 20px 80px;
        color: white;
        text-align: center;
         /* --- FIX STARTS HERE --- */
        height: 550px; /* This gives the overlay a fixed height. */
        box-sizing: border-box; /* This ensures padding is included in the height calculation, not added to it. */
        /* --- FIX ENDS HERE --- */
      }}

      /* --- MODULAR TIMELINE STYLES START --- */

      /* This is the flex container for the line-circle-line structure */
      .timeline-track {{
        display: flex;
        align-items: center;
        /* Use negative margin to break out of the parent's padding */
        margin: 0 -80px;
        margin-bottom: 50px; /* Creates space for the connector to connect */
      }}

      /* Style for the horizontal line elements */
      .line {{
        height: 3px;
        background-color: #fbe10a;
        flex-grow: 1; /* This makes the lines fill the available space */
      }}
      .no_line {{
        height: 3px;
        background-color: transparent;
        flex-grow: 1; /* This makes the lines fill the available space */
      }}

      /* Style for the circle element */
      .circle {{
        width: 25px;
        height: 25px;
        background-color: #fbe10a;
        border-radius: 50%;
        flex-shrink: 0; /* Prevents the circle from shrinking */
        position: relative;
      }}

      /* The vertical line connecting the circle down to the highlight box */
      .circle::after {{
        content: "";
        position: absolute;
        left: 50%;
        top: 100%;
        transform: translateX(-50%);
        width: 3px;
        height: 50px; /* Length of the connector line */
        background-color: #fbe10a;
      }}

      /* --- MODULAR TIMELINE STYLES END --- */

      .timeline-highlight {{
        background-color: #fbe10a;
        color: black;
        padding: 5px 20px 0px 20px;
        font-size: 95px;
        display: inline-block;
        /* margin-top: 2px; Closer to the first line */
        font-weight: 590;
        letter-spacing: 2px;
        /* line-height: 1.1; */
        transform: scaleY(1.1);
      }}
      .yellow {{
        color: #FBE10A;
      }}
      .body-text {{
        font-family: "Golos Text", sans-serif;
        font-weight: 400;
        font-size: 34px;
        line-height: 1.4;
        text-align: center;
        margin-top: 40px;
        color: #ffffff;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <div class="text-overlay">
        <!-- MODIFIED TIMELINE STRUCTURE -->
        <div class="timeline-track">
          <div class="no_line"></div>
          <div class="circle"></div>
          <div class="line"></div>
        </div>
        {timeline_highlight}
        {body_text}
      </div>
    </div>
  </body>
</html>
"""

TIMELINE_MIDDLE_SLIDE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template - Modular Timeline</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@700&display=swap");
      @import url("https://fonts.googleapis.com/css2?family=Golos+Text:wght@400..900&display=swap");
      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Bebas Neue", sans-serif;
        background-color: #f0f0f0;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        display: block;
        /* 'cover' scales the image to fill the container, cropping sides or top/bottom as needed */
        object-fit: {crop_type};
        /* Aligns the image. 'center' horizontally, and 25% from the top vertically to shift it up. */
        object-position: center 25%;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 110px; /* Increased logo size */
        filter: brightness(0) invert(1);
      }}

      .text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.9) 10%,
          rgba(0, 0, 0, 0.9) 40%,
          rgba(0, 0, 0, 0.8) 50%,
          rgba(0, 0, 0, 0.5) 70%,
          rgba(0, 0, 0, 0) 100%
        );
        padding: 40px 80px 20px 80px;
        color: white;
        text-align: center;
         /* --- FIX STARTS HERE --- */
        height: 550px; /* This gives the overlay a fixed height. */
        box-sizing: border-box; /* This ensures padding is included in the height calculation, not added to it. */
        /* --- FIX ENDS HERE --- */
      }}

      /* --- MODULAR TIMELINE STYLES START --- */

      /* This is the flex container for the line-circle-line structure */
      .timeline-track {{
        display: flex;
        align-items: center;
        /* Use negative margin to break out of the parent's padding */
        margin: 0 -80px;
        margin-bottom: 50px; /* Creates space for the connector to connect */
      }}

      /* Style for the horizontal line elements */
      .line {{
        height: 3px;
        background-color: #fbe10a;
        flex-grow: 1; /* This makes the lines fill the available space */
      }}
      .no_line {{
        height: 3px;
        background-color: transparent;
        flex-grow: 1; /* This makes the lines fill the available space */
      }}

      /* Style for the circle element */
      .circle {{
        width: 25px;
        height: 25px;
        background-color: #fbe10a;
        border-radius: 50%;
        flex-shrink: 0; /* Prevents the circle from shrinking */
        position: relative;
      }}

      /* The vertical line connecting the circle down to the highlight box */
      .circle::after {{
        content: "";
        position: absolute;
        left: 50%;
        top: 100%;
        transform: translateX(-50%);
        width: 3px;
        height: 50px; /* Length of the connector line */
        background-color: #fbe10a;
      }}

      /* --- MODULAR TIMELINE STYLES END --- */

      .timeline-highlight {{
        background-color: #fbe10a;
        color: black;
        padding: 5px 20px 0px 20px;
        font-size: 95px;
        display: inline-block;
        /* margin-top: 2px; Closer to the first line */
        font-weight: 590;
        letter-spacing: 2px;
        /* line-height: 1.1; */
        transform: scaleY(1.1);
      }}
      .yellow {{
        color: #FBE10A;
      }}
      .body-text {{
        font-family: "Golos Text", sans-serif;
        font-weight: 400;
        font-size: 34px;
        line-height: 1.4;
        text-align: center;
        margin-top: 40px;
        color: #ffffff;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <img src="{background_image}" class="background-image" />
      <div class="text-overlay">
        <!-- MODIFIED TIMELINE STRUCTURE -->
        <div class="timeline-track">
          <div class="line"></div>
          <div class="circle"></div>
          <div class="line"></div>
        </div>
        {timeline_highlight}
        {body_text}
      </div>
    </div>
  </body>
</html>
"""

TIMELINE_MIDDLE_SLIDE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template - Modular Timeline</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@700&display=swap");
      @import url("https://fonts.googleapis.com/css2?family=Golos+Text:wght@400..900&display=swap");
      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Bebas Neue", sans-serif;
        background-color: #f0f0f0;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 110px; /* Increased logo size */
        filter: brightness(0) invert(1);
      }}

      .text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.9) 10%,
          rgba(0, 0, 0, 0.9) 40%,
          rgba(0, 0, 0, 0.8) 50%,
          rgba(0, 0, 0, 0.5) 70%,
          rgba(0, 0, 0, 0) 100%
        );
        padding: 40px 80px 20px 80px;
        color: white;
        text-align: center;
         /* --- FIX STARTS HERE --- */
        height: 550px; /* This gives the overlay a fixed height. */
        box-sizing: border-box; /* This ensures padding is included in the height calculation, not added to it. */
        /* --- FIX ENDS HERE --- */
      }}

      /* --- MODULAR TIMELINE STYLES START --- */

      /* This is the flex container for the line-circle-line structure */
      .timeline-track {{
        display: flex;
        align-items: center;
        /* Use negative margin to break out of the parent's padding */
        margin: 0 -80px;
        margin-bottom: 50px; /* Creates space for the connector to connect */
      }}

      /* Style for the horizontal line elements */
      .line {{
        height: 3px;
        background-color: #fbe10a;
        flex-grow: 1; /* This makes the lines fill the available space */
      }}
      .no_line {{
        height: 3px;
        background-color: transparent;
        flex-grow: 1; /* This makes the lines fill the available space */
      }}

      /* Style for the circle element */
      .circle {{
        width: 25px;
        height: 25px;
        background-color: #fbe10a;
        border-radius: 50%;
        flex-shrink: 0; /* Prevents the circle from shrinking */
        position: relative;
      }}

      /* The vertical line connecting the circle down to the highlight box */
      .circle::after {{
        content: "";
        position: absolute;
        left: 50%;
        top: 100%;
        transform: translateX(-50%);
        width: 3px;
        height: 50px; /* Length of the connector line */
        background-color: #fbe10a;
      }}

      /* --- MODULAR TIMELINE STYLES END --- */

      .timeline-highlight {{
        background-color: #fbe10a;
        color: black;
        padding: 5px 20px 0px 20px;
        font-size: 95px;
        display: inline-block;
        /* margin-top: 2px; Closer to the first line */
        font-weight: 590;
        letter-spacing: 2px;
        /* line-height: 1.1; */
        transform: scaleY(1.1);
      }}
      .yellow {{
        color: #FBE10A;
      }}
      .body-text {{
        font-family: "Golos Text", sans-serif;
        font-weight: 400;
        font-size: 34px;
        line-height: 1.4;
        text-align: center;
        margin-top: 40px;
        color: #ffffff;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <div class="text-overlay">
        <!-- MODIFIED TIMELINE STRUCTURE -->
        <div class="timeline-track">
          <div class="line"></div>
          <div class="circle"></div>
          <div class="line"></div>
        </div>
        {timeline_highlight}
        {body_text}
      </div>
    </div>
  </body>
</html>
"""

TIMELINE_END_SLIDE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template - Modular Timeline</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@700&display=swap");
      @import url("https://fonts.googleapis.com/css2?family=Golos+Text:wght@400..900&display=swap");
      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Bebas Neue", sans-serif;
        background-color: #f0f0f0;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
      }}

      .background-image {{
        width: 100%;
        height: 100%;
        display: block;
        /* 'cover' scales the image to fill the container, cropping sides or top/bottom as needed */
        object-fit: {crop_type};
        /* Aligns the image. 'center' horizontally, and 25% from the top vertically to shift it up. */
        object-position: center 25%;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 110px; /* Increased logo size */
        filter: brightness(0) invert(1);
      }}

      .text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.9) 10%,
          rgba(0, 0, 0, 0.9) 40%,
          rgba(0, 0, 0, 0.8) 50%,
          rgba(0, 0, 0, 0.5) 70%,
          rgba(0, 0, 0, 0) 100%
        );
        padding: 40px 80px 20px 80px;
        color: white;
        text-align: center;
         /* --- FIX STARTS HERE --- */
        height: 550px; /* This gives the overlay a fixed height. */
        box-sizing: border-box; /* This ensures padding is included in the height calculation, not added to it. */
        /* --- FIX ENDS HERE --- */
      }}

      /* --- MODULAR TIMELINE STYLES START --- */

      /* This is the flex container for the line-circle-line structure */
      .timeline-track {{
        display: flex;
        align-items: center;
        /* Use negative margin to break out of the parent's padding */
        margin: 0 -80px;
        margin-bottom: 50px; /* Creates space for the connector to connect */
      }}

      /* Style for the horizontal line elements */
      .line {{
        height: 3px;
        background-color: #fbe10a;
        flex-grow: 1; /* This makes the lines fill the available space */
      }}
      .no_line {{
        height: 3px;
        background-color: transparent;
        flex-grow: 1; /* This makes the lines fill the available space */
      }}

      /* Style for the circle element */
      .circle {{
        width: 25px;
        height: 25px;
        background-color: #fbe10a;
        border-radius: 50%;
        flex-shrink: 0; /* Prevents the circle from shrinking */
        position: relative;
      }}

      /* The vertical line connecting the circle down to the highlight box */
      .circle::after {{
        content: "";
        position: absolute;
        left: 50%;
        top: 100%;
        transform: translateX(-50%);
        width: 3px;
        height: 50px; /* Length of the connector line */
        background-color: #fbe10a;
      }}

      /* --- MODULAR TIMELINE STYLES END --- */

      .timeline-highlight {{
        background-color: #fbe10a;
        color: black;
        padding: 5px 20px 0px 20px;
        font-size: 95px;
        display: inline-block;
        /* margin-top: 2px; Closer to the first line */
        font-weight: 590;
        letter-spacing: 2px;
        /* line-height: 1.1; */
        transform: scaleY(1.1);
      }}
      .yellow {{
        color: #FBE10A;
      }}
      .body-text {{
        font-family: "Golos Text", sans-serif;
        font-weight: 400;
        font-size: 34px;
        line-height: 1.4;
        text-align: center;
        margin-top: 40px;
        color: #ffffff;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <img src="{background_image}" class="background-image" />
      <div class="text-overlay">
        <!-- MODIFIED TIMELINE STRUCTURE -->
        <div class="timeline-track">
          <div class="line"></div>
          <div class="circle"></div>
          <div class="no_line"></div>
        </div>
        {timeline_highlight}
        {body_text}
      </div>
    </div>
  </body>
</html>
"""

TIMELINE_END_SLIDE_OVERLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SW Template - Modular Timeline</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@700&display=swap");
      @import url("https://fonts.googleapis.com/css2?family=Golos+Text:wght@400..900&display=swap");
      body,
      html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Bebas Neue", sans-serif;
        background-color: #f0f0f0;
      }}

      .container {{
        position: relative;
        width: 1080px;
        height: 1350px;
        margin: auto;
        overflow: hidden;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        left: 40px;
        width: 110px; /* Increased logo size */
        filter: brightness(0) invert(1);
      }}

      .text-overlay {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(
          to top,
          rgba(0, 0, 0, 0.9) 10%,
          rgba(0, 0, 0, 0.9) 40%,
          rgba(0, 0, 0, 0.8) 50%,
          rgba(0, 0, 0, 0.5) 70%,
          rgba(0, 0, 0, 0) 100%
        );
        padding: 40px 80px 20px 80px;
        color: white;
        text-align: center;
         /* --- FIX STARTS HERE --- */
        height: 550px; /* This gives the overlay a fixed height. */
        box-sizing: border-box; /* This ensures padding is included in the height calculation, not added to it. */
        /* --- FIX ENDS HERE --- */
      }}

      /* --- MODULAR TIMELINE STYLES START --- */

      /* This is the flex container for the line-circle-line structure */
      .timeline-track {{
        display: flex;
        align-items: center;
        /* Use negative margin to break out of the parent's padding */
        margin: 0 -80px;
        margin-bottom: 50px; /* Creates space for the connector to connect */
      }}

      /* Style for the horizontal line elements */
      .line {{
        height: 3px;
        background-color: #fbe10a;
        flex-grow: 1; /* This makes the lines fill the available space */
      }}
      .no_line {{
        height: 3px;
        background-color: transparent;
        flex-grow: 1; /* This makes the lines fill the available space */
      }}

      /* Style for the circle element */
      .circle {{
        width: 25px;
        height: 25px;
        background-color: #fbe10a;
        border-radius: 50%;
        flex-shrink: 0; /* Prevents the circle from shrinking */
        position: relative;
      }}

      /* The vertical line connecting the circle down to the highlight box */
      .circle::after {{
        content: "";
        position: absolute;
        left: 50%;
        top: 100%;
        transform: translateX(-50%);
        width: 3px;
        height: 50px; /* Length of the connector line */
        background-color: #fbe10a;
      }}

      /* --- MODULAR TIMELINE STYLES END --- */

      .timeline-highlight {{
        background-color: #fbe10a;
        color: black;
        padding: 5px 20px 0px 20px;
        font-size: 95px;
        display: inline-block;
        /* margin-top: 2px; Closer to the first line */
        font-weight: 590;
        letter-spacing: 2px;
        /* line-height: 1.1; */
        transform: scaleY(1.1);
      }}
      .yellow {{
        color: #FBE10A;
      }}
      .body-text {{
        font-family: "Golos Text", sans-serif;
        font-weight: 400;
        font-size: 34px;
        line-height: 1.4;
        text-align: center;
        margin-top: 40px;
        color: #ffffff;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <img src="{logo_image}" alt="SW Logo" class="logo" />
      <div class="text-overlay">
        <!-- MODIFIED TIMELINE STRUCTURE -->
        <div class="timeline-track">
          <div class="no_line"></div>
          <div class="circle"></div>
          <div class="line"></div>
        </div>
        {timeline_highlight}
        {body_text}
      </div>
    </div>
  </body>
</html>
"""

timeline_template = {
    "page_name": "scoopwhoop",
    "template_type": "timeline",
    "text_template": {"template_description":TEMPLATE_DESCRIPTION,
            "json_description":JSON_DESCRIPTION},
    "slides": {
        "headline_slide": {
            "html_template": HEADLINE_SLIDE_TEMPLATE,
            "overlay_template": HEADLINE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "first_line": {"type": "text", "tag": "div", "class": "first-line"},
                    "highlight": {"type": "text", "tag": "div", "class": "highlight"},
                    "sub_heading": {
                        "type": "text_area",
                        "tag": "div",
                        "class": "sub-heading",
                    },
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"type": "dropdown", "values": ["logo.png","logo_original.png", "logo_hottake.png"], "default": "logo.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            }
        },
        "timeline_start_slide": {
            "html_template": TIMELINE_START_SLIDE_TEMPLATE,
            "overlay_template": TIMELINE_START_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "timeline_highlight": {
                        "type": "text",
                        "tag": "div",
                        "class": "timeline-highlight",
                    },
                    "body_text": {
                        "type": "text_area",
                        "tag": "p",
                        "class": "body-text",
                    },
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"type": "dropdown", "values": ["logo.png","logo_original.png", "logo_hottake.png"], "default": "logo.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            }
        },
        "timeline_middle_slide": {
            "html_template": TIMELINE_MIDDLE_SLIDE_TEMPLATE,
            "overlay_template": TIMELINE_MIDDLE_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "timeline_highlight": {
                        "type": "text",
                        "tag": "div",
                        "class": "timeline-highlight",
                    },
                    "body_text": {
                        "type": "text_area",
                        "tag": "p",
                        "class": "body-text",
                    },
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"type": "dropdown", "values": ["logo.png","logo_original.png", "logo_hottake.png"], "default": "logo.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            }
        },
        "timeline_end_slide": {
            "html_template": TIMELINE_END_SLIDE_TEMPLATE,
            "overlay_template": TIMELINE_END_SLIDE_OVERLAY_TEMPLATE,
            "text_only": False,
            "text": {
                    "timeline_highlight": {
                        "type": "text",
                        "tag": "div",
                        "class": "timeline-highlight",
                    },
                    "body_text": {
                        "type": "text_area",
                        "tag": "p",
                        "class": "body-text",
                    },
            },
            "assets":{
                "background_video": {"type":"bytes", "file_type":"mp4"},
                "background_image": {"type":"bytes", "file_type":"png"},
                "logo_image": {"type": "dropdown", "values": ["logo.png","logo_original.png", "logo_hottake.png"], "default": "logo.png"},
            },
            "image_edits": {
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            },
            "video_edits":{
                "type": {"type":"default", "values": "image_overlay"},
                "crop_type": {"type": "dropdown", "values": ["cover", "contain"] , "default": "cover"},
            }
        },
    },
}

if __name__ == "__main__":
    text = {
        "name": "timeline_headline_slide",
        "image_description": "Wreckage of Air India Flight 171 at crash site",
        "text_template": {
            "first_line": "<div class='first-line'>Test</div>",
            "highlight": "<div class='highlight'>Test</div>",
            "sub_heading": "<div class='sub-heading'>Test Sub Heading</div>",
        },
    }

    with open("./data_/bleh_7.html", "w") as f:
        f.write(
            HEADLINE_SLIDE_TEMPLATE.format(
                file_path="./test.png", **text["text_template"]
            )
        )
