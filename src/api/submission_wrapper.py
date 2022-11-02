import re 
import emoji
import os 
from datetime import datetime 

class SubmissionWrapper:
    def __init__(self) -> None:
        self.review_length = -1
        self.blacklisted_terms = []
        self.replace_urls = ""
        self.replace_emojis = ""
        self.content = ''
        
        
    