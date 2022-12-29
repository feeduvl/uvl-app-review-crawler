from datetime import datetime 
import os 
from google_play_scraper import reviews_all, Sort
from src.flask_setup import app 
from src.api.utils import clean_reviews, filter_reviews_by_date, scale_review_data_set, scale_reviews, filter_valid_reviews, app_reviews_replace_emojis, app_reviews_replace_urls, clean_review_dates
class AppReviewCrawler:
    def __init__(self) -> None:
        self.crawled_data = []
        
    def crawl(self, app_id, from_date_str, to_date_str, post_selection, new_limit,
              min_length_review, blacklist_reviews,
              replace_emojis, replace_urls):
        """Initiate a crawling job for the specified App using an optional number of 
           preprocessing parameters
        """
        result = reviews_all(
            app_id,
            lang=post_selection,
            sort=Sort.NEWEST
        )
        app.logger.info(result)
        result = clean_review_dates(result)
        result = filter_reviews_by_date(from_date_str, to_date_str, result)
        if(replace_emojis == True):
            result = app_reviews_replace_emojis(result)
        if(replace_urls == True):
            result = app_reviews_replace_urls(result)
        result = scale_reviews(result, min_length_review)
        result = scale_review_data_set(result, new_limit)       
        result = filter_valid_reviews(result, blacklist_reviews)
        #app.logger.info(result)
        result = clean_reviews(result)
        #app.logger.info(result)
        self.crawled_data = result
        app.logger.info(self.crawled_data)
                    
    def get_documents(self, collection_name):
        documents = []
        sep = os.linesep + '###'
        date = datetime.today().strftime('%Y_%m_%d')
        for dataset in enumerate(self.crawled_data):
            document_id = f'{collection_name}_{date}'
            text = dataset.get("score") + sep + dataset.get("content") + sep 
            documents.append({"id": document_id, "text": text})
        app.logger.info(documents)
        return documents