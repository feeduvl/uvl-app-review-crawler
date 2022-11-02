from datetime import datetime 
import os 

class AppReviewCrawler:
    def __init__(self, app_instance) -> None:
        self.app = app_instance
        self.crawled_data = []
        
    def crawl(self, app_id, from_date_str, to_date_str, post_selection, new_limit,
              min_length_review= 0, blacklist_reviews = None,
              replace_emojis=False, replace_urls=False):
        """Initiate a crawling job for the specified App using an optional number of 
           preprocessing parameters
        """
        from_date = datetime.strptime(from_date_str, "%m/%d/%Y")
        to_date = datetime.strptime(to_date_str, "%m/%d/%Y")
        