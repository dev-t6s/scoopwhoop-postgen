from src.templates.scoopwhoop.timeline import timeline_template
from src.templates.scoopwhoop.cultural_pieces import cultural_pieces_template
from src.templates.scoopwhoop.opinion_pieces import opinion_pieces_template
from src.templates.scoopwhoop.biz import biz_template
from src.templates.scoopwhoop.ranking import ranking_template
from src.templates.scoopwhoop.body import body_template
from src.templates.scoopwhoop.text_based_1 import text_based_1_template
from src.templates.scoopwhoop.text_based_2 import text_based_2_template
from src.templates.scoopwhoop.text_based_3 import text_based_3_template
from src.templates.scoopwhoop.text_based_4 import text_based_4_template
from src.templates.scoopwhoop.reel import reel_template
from src.templates.scoopwhoop.reel_1 import reel_1_template
from src.templates.scoopwhoop.writeup import writeup_template
from src.templates.scoopwhoop.meme import meme_template

from src.templates.twitter.tweet_image import tweet_image_template
from src.templates.twitter.tweet_text import tweet_text_template
from src.templates.twitter.tweet_tag import tweet_tag_template

from src.templates.social_village.content import content_template
from src.templates.social_village.thumbnail import thumbnail_template as social_village_thumbnail_template
from src.templates.social_village.reel import reel_template as social_village_reel_template

from src.templates.the_sarcastic_indian.writeup import writeup_template as sarcastic_writeup_template

from src.templates.infomance.content import infomance_content_template
from src.templates.infomance.thumbnail import infomance_thumbnail_template
from src.templates.infomance.thumbnail_3 import infomance_thumbnail_3_template

from src.templates.marketing_stories.headline import thumbnail_template as marketing_stories_thumbnail_template
from src.templates.marketing_stories.carousel import carousel_template
from src.templates.marketing_stories.ad_reel import ad_reel_template
from src.templates.marketing_stories.meme_reel import meme_reel_template

from src.templates.the_thatva.headline import the_thatva_headline_template

from src.templates.the_startup_journey.scheme import scheme_template
from src.templates.the_startup_journey.news import news_template
from src.templates.the_startup_journey.founders import founders_template    
from src.templates.the_startup_journey.announcement import announcement_template
from src.templates.the_startup_journey.carousel import carousel_template as the_startup_journey_carousel_template
from src.templates.the_startup_journey.thumbnail import thumbnail_template as the_startup_journey_thumbnail_template

from src.templates.laughter_colors.headline import laughter_colors_headline_template

from src.templates.upsc_world.headline import upsc_world_headline_template

from src.templates.the_indian_idiot.headline import the_indian_idiot_headline_template

from src.templates.the_dope_indian.writeup import writeup_template as the_dope_indian_writeup_template

from src.templates.trolls_official.headline import trolls_official_headline_template

from src.templates.bws.static_carousel import static_carousel_template
from src.templates.bws.reel import reel_template as bws_reel_template
from src.templates.bws.post import post_template as bws_post_template

from src.templates.desi_standup.reel import reel_template as desi_standup_reel_template

from src.templates.gls.thumbnail import thumbnail_template as gls_thumbnail_template
from src.templates.gls.headline import headline_template as gls_headline_template

from src.templates.indian_standup.reel import reel_template as indian_standup_reel_template
from src.templates.indian_standup.tweet_image import tweet_image_template as indian_standup_tweet_image_template

from src.templates.smart_india_news.thumbnail import  smart_india_news_thumbnail_template

from src.templates.startuptalksindia.reel import reel_template as startuptalksindia_reel_template
from src.templates.startuptalksindia.thumbnail import thumbnail_template as startuptalksindia_thumbnail_template

from src.templates.trillionaire_culture.thumbnail import headline_template as trillionaire_culture_headline_template

def get_template_config(template_type: str, page_name: str) -> dict:
    """Get template configuration based on type"""
    if page_name == "scoopwhoop":
        if template_type == "timeline":
            return timeline_template
        elif template_type == "cultural_pieces":
            return cultural_pieces_template
        elif template_type == "opinion_pieces":
            return opinion_pieces_template
        elif template_type == "biz":
            return biz_template
        elif template_type == "ranking":
            return ranking_template
        elif template_type == "body":
            return body_template
        elif template_type == "text_based_1":
            return text_based_1_template
        elif template_type == "text_based_2":
            return text_based_2_template
        elif template_type == "text_based_3":
            return text_based_3_template
        elif template_type == "text_based_4":
            return text_based_4_template
        elif template_type == "reel":
            return reel_template
        elif template_type == "reel_1":
            return reel_1_template
        elif template_type == "meme":
            return meme_template
        elif template_type == "writeup":
            return writeup_template
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
        elif template_type == "reel":
            return social_village_reel_template
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
        elif template_type == "carousel":
            return carousel_template
        elif template_type == "ad_reel":
            return ad_reel_template
        elif template_type == "meme_reel":
            return meme_reel_template
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
        elif template_type == "carousel":
            return the_startup_journey_carousel_template
        elif template_type == "thumbnail":
            return the_startup_journey_thumbnail_template
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

    elif page_name == "trolls_official":
        if template_type == "headline":
            return trolls_official_headline_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")

    elif page_name == "bws":
        if template_type == "carousel":
            return static_carousel_template
        elif template_type == "reel":
            return bws_reel_template
        elif template_type == "post":
            return bws_post_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    
    elif page_name == "desi_standup":
        if template_type == "reel":
            return desi_standup_reel_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    
    elif page_name == "gls":
        if template_type == "thumbnail":
            return gls_thumbnail_template
        elif template_type == "headline":
            return gls_headline_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")

    elif page_name == "indian_standup":
        if template_type == "reel":
            return indian_standup_reel_template
        elif template_type == "tweet_image":
            return indian_standup_tweet_image_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    
    elif page_name == "smart_india_news":
        if template_type == "thumbnail":
            return smart_india_news_thumbnail_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")
    
    elif page_name == "startuptalksindia":
        if template_type == "reel":
            return startuptalksindia_reel_template
        elif template_type == "thumbnail":
            return startuptalksindia_thumbnail_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")

    elif page_name == "trillionaire_culture":
        if template_type == "headline":
            return trillionaire_culture_headline_template
        else:
            raise ValueError(f"Unknown template type for given {page_name}: {template_type}")

    else:
        raise ValueError(f"Unknown page name: {page_name}")
        
