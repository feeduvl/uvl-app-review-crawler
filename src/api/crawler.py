from datetime import datetime 
import os 
from google_play_scraper import reviews_all, Sort
from src.flask_setup import app 
from src.api.utils import clean_reviews, filter_reviews_by_date, scale_review_data_set, scale_reviews, filter_valid_reviews, app_reviews_replace_emojis, app_reviews_replace_urls, clean_review_dates, language_filter
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
        result = clean_review_dates(result)
        app.logger.info(result)
        result = language_filter(result, post_selection)
        app.logger.info("Filtering reviews in valid time frame")
        result = filter_reviews_by_date(from_date_str, to_date_str, result)
        if(replace_emojis == True):
            app.logger.info("Removing emojis from review texts")
            result = app_reviews_replace_emojis(result)
        if(replace_urls == True):
            app.logger.info("Removing urls from the review texts")
            result = app_reviews_replace_urls(result)
        app.logger.info("Choosing reviews with specific length")
        result = scale_reviews(result, min_length_review) 
        app.logger.info("Handing the desired number of reviews")
        result = scale_review_data_set(result, new_limit)     
        app.logger.info("Filtering non-blacklisted reviews")  
        result = filter_valid_reviews(result, blacklist_reviews)
        app.logger.info("Removing unnecessary data")
        result = clean_reviews(result)
        self.crawled_data = result
        app.logger.info(self.crawled_data)
                    
    def get_documents(self, collection_name):
        documents = []
        sep = os.linesep + '###'
        date = datetime.today().strftime('%Y_%m_%d')
        for i in range(0, len(self.crawled_data)):
            document_id = f'"Review"_{i}_{collection_name}_{date}'
            text = str(self.crawled_data[i]['score']) + sep + self.crawled_data[i]['content'] + sep
            documents.append({"id": document_id, "text": text})
        app.logger.info("Documents for saving: ")
        app.logger.info(documents)
        
        return documents