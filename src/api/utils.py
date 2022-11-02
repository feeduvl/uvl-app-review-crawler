""" 
Databasehandler class to acces the database of feeduvl and write directly into it.
"""

from datetime import datetime 
import requests 

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