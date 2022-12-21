""" 
Databasehandler class to acces the database of feeduvl and write directly into it. Having helper functions needed for preprocessing 
the dataset.
"""

from datetime import datetime 
import requests 
import re 
import emoji

class DatabaseHandler:
    def insert(self, collection_name, documents, logger):
        response = requests.get(f'https://feed-uvl.ifi.uni-heidelberg.de/hitec/repository/concepts/dataset/name/{collection_name}')
        existing_collection = response.json()
        logger.info(existing_collection)
        
        if not existing_collection['documents']:
            logger.info('no existing collection detected')
            
            collection = {
                'name' : collection_name,
                'documents': documents
            }
            logger.info(collection)
            request = requests.post('https://feed-uvl.ifi.uni-heidelberg.de/hitec/repository/concepts/store/dataset/', json=collection)
        else:
            logger.info('existing collection detected')
            
            existing_collection['documents'] += documents
            request = requests.post('https://feed-uvl.ifi.uni-heidelberg.de/hitec/repository/concepts/store/dataset/', json=existing_collection)
            return request.status_code
        
def clean_reviews(app_reviews):
    for app in app_reviews:
        del app['reviewId']
        del app['userName']
        del app['userImage']
        del app['thumbsUpCount']
        del app['reviewCreatedVersion']
        del app['repliedAt']
        del app['replyContent']
        del app['at']
    return app_reviews

def filter_reviews_by_date(date_from_str, date_to_str, app_reviews):
    from_date = datetime.strptime(date_from_str, "%m/%d/%Y")
    to_date = datetime.strptime(date_to_str, "%m/%d/%Y")
    filtered_reviews = []
    for i in range(0, len(app_reviews)):
        review_date = app_reviews[i]['at']
        if(from_date <= review_date <= to_date):
            filtered_reviews.append(app_reviews[i])
    return filtered_reviews

def app_reviews_replace_urls(app_reviews):
    for i in range(len(app_reviews)):
        app_reviews[i]['content'] = re.sub(r'http\S+', '', app_reviews[i]['content'])
    return app_reviews

def app_reviews_replace_emojis(app_review):     
    for i in range(len(app_review)):
        del app_review[i]['at']
        app_review[i]['content'] = emoji.get_emoji_regexp().sub('', app_review[i]['content'])        
    return app_review 

def scale_reviews(app_reviews,  min_length):
    scaled = []
    for i in range(len(app_reviews)):
        if(len(app_reviews[i]['content'] >= min_length)):
            scaled.append(app_reviews[i])
    return scaled 
            
def scale_review_data_set(app_reviews, new_limit):
    scaled = []
    if(len(app_reviews) > new_limit):
        for i in range(0, new_limit):
            scaled.append(app_reviews[i])
        return scaled
    else:
        return scaled
    
def filter_valid_reviews(app_reviews, blacklist):
    filtered = []
    for blacklisted_word in blacklist:
        for i in range(0, len(app_reviews)):
            if blacklisted_word in app_reviews[i]['content']:
                app_reviews[i]['valid'] = "False"
            else:
                app_reviews[i]['valid'] = "True"
    for i in app_reviews:
        if i['valid'] == "True":
            filtered.append(i)
    return filtered            
        