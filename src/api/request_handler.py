from src.api.crawler import AppReviewCrawler
import re 
class RequestHandler:
    def __init__(self, request_content, database_handler, logger) -> None:
        """Constructor of RequestHandler
        """
        self.request_content = request_content
        self.database_handler = database_handler
        self.logger = logger
        
    def run(self):
        """Method to orchestrate the run for a given request 
        """
        app_instance = self.request_content['app_url']
        dataset_name = self.request_content['dataset_name']
        date_from = self.request_content['date_from']
        date_to = self.request_content['date_to']
        post_selection = self.request_content['post_selection']
        new_limit = int(self.request_content['new_limit'])
        
        min_length_reviews = self.request_content['min_length_posts']
        blacklist_posts = self.request_content['blacklist_posts']
        replace_urls = self.request_content['replace_urls']
        replace_emojis = self.request_content['replace_emojis']
        
        crawled_documents = []
        app_id = re.findall('id=(.*)&hl', app_instance)[0]
        self.logger.info(f'Starting crawling reviews of {app_id}')
        app_review_crawler = AppReviewCrawler()
        app_review_crawler.crawl(app_id, date_from, date_to, post_selection, new_limit, min_length_reviews, blacklist_posts, replace_emojis, replace_urls)
        crawled_documents = app_review_crawler.get_documents(app_id)

        self.database_handler.insert(dataset_name, crawled_documents, self.logger)