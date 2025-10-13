from src.templates.scoopwhoop.timeline import timeline_template
from src.templates.scoopwhoop.thumbnail import thumbnail_template as scoopwhoop_thumbnail_template
from src.templates.scoopwhoop.writeup import writeup_template
from src.templates.scoopwhoop.text_based import text_based_template as scoopwhoop_text_based_template
from src.templates.scoopwhoop.meme import meme_template

from src.templates.twitter.tweet_image import tweet_image_template
from src.templates.twitter.tweet_text import tweet_text_template
from src.templates.twitter.tweet_tag import tweet_tag_template

from src.templates.social_village.content import content_template
from src.templates.social_village.thumbnail import thumbnail_template as social_village_thumbnail_template

from src.templates.the_sarcastic_indian.writeup import writeup_template as sarcastic_writeup_template

from src.templates.infomance.content import infomance_content_template
from src.templates.infomance.thumbnail import infomance_thumbnail_template
from src.templates.infomance.thumbnail_3 import infomance_thumbnail_3_template

from src.templates.marketing_stories.headline import thumbnail_template as marketing_stories_thumbnail_template

from src.templates.the_thatva.headline import the_thatva_headline_template

from src.templates.the_startup_journey.scheme import scheme_template
from src.templates.the_startup_journey.news import news_template
from src.templates.the_startup_journey.founders import founders_template    
from src.templates.the_startup_journey.announcement import announcement_template

from src.templates.laughter_colors.headline import laughter_colors_headline_template

from src.templates.upsc_world.headline import upsc_world_headline_template

from src.templates.the_indian_idiot.headline import the_indian_idiot_headline_template

from src.templates.the_dope_indian.writeup import writeup_template as the_dope_indian_writeup_template

def get_template_config(template_type: str, page_name: str) -> dict:
    """Get template configuration based on type"""
    if page_name == "scoopwhoop":
        if template_type == "timeline":
            return timeline_template
        elif template_type == "thumbnail":
            return scoopwhoop_thumbnail_template
        elif template_type == "writeup":
            return writeup_template
        elif template_type == "text_based":
            return scoopwhoop_text_based_template
        elif template_type == "meme":
            return meme_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    elif page_name == "twitter":
        if template_type == "tweet_image":
            return tweet_image_template
        elif template_type == "tweet_tag":
            return tweet_tag_template
        elif template_type == "text_based":
            return tweet_text_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    
    elif page_name == "social_village":
        if template_type == "content":
            return content_template
        elif template_type == "thumbnail":
            return social_village_thumbnail_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    
    elif page_name == "the_sarcastic_indian":
        if template_type == "writeup":
            return sarcastic_writeup_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    
    elif page_name == "infomance":
        if template_type == "content":
            return infomance_content_template
        elif template_type == "thumbnail":
            return infomance_thumbnail_template
        elif template_type == "thumbnail_3":
            return infomance_thumbnail_3_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    elif page_name == "marketing_stories":
        if template_type == "thumbnail":
            return marketing_stories_thumbnail_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    elif page_name == "the_tatva":
        if template_type == "headline":
            return the_thatva_headline_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    elif page_name == "the_startup_journey":
        if template_type == "scheme":
            return scheme_template
        elif template_type == "news":
            return news_template
        elif template_type == "founders":
            return founders_template
        elif template_type == "announcement":
            return announcement_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    elif page_name == "laughter_colors":
        if template_type == "headline":
            return laughter_colors_headline_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    elif page_name == "upsc_world":
        if template_type == "headline":
            return upsc_world_headline_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    elif page_name == "the_indian_idiot":
        if template_type == "headline":
            return the_indian_idiot_headline_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    elif page_name == "the_dope_indian":
        if template_type == "writeup":
            return the_dope_indian_writeup_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    else:
        raise ValueError(f"Unknown page name: {page_name}")
        
