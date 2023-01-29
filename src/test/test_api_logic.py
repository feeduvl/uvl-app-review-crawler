import unittest
import datetime
import sys
sys.path.insert(0, '../src')
from api.utils import clean_review_dates, clean_reviews, filter_reviews_by_date, filter_valid_reviews, language_filter, app_reviews_replace_emojis, app_reviews_replace_urls, scale_review_data_set, scale_reviews

class TestPreprocessing(unittest.TestCase):    
    def setUp(self)-> None:
        self.today = datetime.date.today()
        pass
    
    def test_clean_review_dates(self):
        reviews = [
        {
            'userName': "Alyssa Williams", 
            "userImage": "https://lh3.googleusercontent.com/-cVEHKr7mzv8/AAAAAAAAAAI/AAAAAAAAAAA/AKF05nB2r3GUkji31m0tC4ylFNiVMpmNWA/photo.jpg",
            "content": "This is literally the best idle game I have ever played. The penguins waddle around and live their best lives in the cutest little outfits. I just unlocked the little penguins and I have been sobbing uncontrollably for ten minutes because they are so adorable. There are only two suggestions I have for this game: more of the penguin info ads. I love them. I have learned so much about all the teeny fellas. Secondly, I would like to be able to name my 'guins so I can tell them apart.",
            "score": 5,
            "thumbsUpCount": 54,
            "reviewCreatedVersion": "1.16",
            "at": datetime.datetime(2020, 2, 24, 17, 19, 34),
            "replyContent": "Hello, We will gradually improve the various systems in the game to enhance the player's game experience. We have recorded your suggestions and feedback to the planner. If you have any other suggestions and ideas, please feel free to contact us at penguinisle@habby.com.Thank you for playing!",
            "repliedAt": datetime.datetime(2020, 2, 24, 18, 30, 42),
            "reviewId": "gp:AOqpTOE0Iy5S9Je1F8W1BgCl6l_TCFP_QN4qGtRATX3PeB5VV9aZu6UHfMWdYFF1at4qZ59xxLNHFqYLql5SL-k"
        },
        ]
        cleaned_date_reviews =  [
        {
            'userName': "Alyssa Williams", 
            "userImage": "https://lh3.googleusercontent.com/-cVEHKr7mzv8/AAAAAAAAAAI/AAAAAAAAAAA/AKF05nB2r3GUkji31m0tC4ylFNiVMpmNWA/photo.jpg",
            "content": "This is literally the best idle game I have ever played. The penguins waddle around and live their best lives in the cutest little outfits. I just unlocked the little penguins and I have been sobbing uncontrollably for ten minutes because they are so adorable. There are only two suggestions I have for this game: more of the penguin info ads. I love them. I have learned so much about all the teeny fellas. Secondly, I would like to be able to name my 'guins so I can tell them apart.",
            "score": 5,
            "thumbsUpCount": 54,
            "reviewCreatedVersion": "1.16",
            "at": datetime.datetime(2020, 2, 24, 0, 0, 0),
            "replyContent": "Hello, We will gradually improve the various systems in the game to enhance the player's game experience. We have recorded your suggestions and feedback to the planner. If you have any other suggestions and ideas, please feel free to contact us at penguinisle@habby.com.Thank you for playing!",
            "repliedAt": datetime.datetime(2020, 2, 24, 18, 30, 42),
            "reviewId": "gp:AOqpTOE0Iy5S9Je1F8W1BgCl6l_TCFP_QN4qGtRATX3PeB5VV9aZu6UHfMWdYFF1at4qZ59xxLNHFqYLql5SL-k"
        },
        ]
    
        reviews = clean_review_dates(reviews)
        self.assertEqual(reviews[0].get('at'), cleaned_date_reviews[0].get('at'))   
    
    def test_clean_reviews(self):
        reviews = [
        {
            'userName': "Alyssa Williams", 
            "userImage": "https://lh3.googleusercontent.com/-cVEHKr7mzv8/AAAAAAAAAAI/AAAAAAAAAAA/AKF05nB2r3GUkji31m0tC4ylFNiVMpmNWA/photo.jpg",
            "content": "This is literally the best idle game I have ever played. The penguins waddle around and live their best lives in the cutest little outfits. I just unlocked the little penguins and I have been sobbing uncontrollably for ten minutes because they are so adorable. There are only two suggestions I have for this game: more of the penguin info ads. I love them. I have learned so much about all the teeny fellas. Secondly, I would like to be able to name my 'guins so I can tell them apart.",
            "score": 5,
            "thumbsUpCount": 54,
            "reviewCreatedVersion": "1.16",
            "at": datetime.datetime(2020, 2, 24, 17, 19, 34),
            "replyContent": "Hello, We will gradually improve the various systems in the game to enhance the player's game experience. We have recorded your suggestions and feedback to the planner. If you have any other suggestions and ideas, please feel free to contact us at penguinisle@habby.com.Thank you for playing!",
            "repliedAt": datetime.datetime(2020, 2, 24, 18, 30, 42),
            "reviewId": "gp:AOqpTOE0Iy5S9Je1F8W1BgCl6l_TCFP_QN4qGtRATX3PeB5VV9aZu6UHfMWdYFF1at4qZ59xxLNHFqYLql5SL-k"
        },
        ]
        cleaned_reviews =  [
        {
            "content": "This is literally the best idle game I have ever played. The penguins waddle around and live their best lives in the cutest little outfits. I just unlocked the little penguins and I have been sobbing uncontrollably for ten minutes because they are so adorable. There are only two suggestions I have for this game: more of the penguin info ads. I love them. I have learned so much about all the teeny fellas. Secondly, I would like to be able to name my 'guins so I can tell them apart.",
            "score": 5,
        },
        ]
        
        reviews = clean_reviews(reviews)
        self.assertEqual(reviews[0], cleaned_reviews[0])
        
    def test_filter_by_date(self):
        reviews = [
        {
            'userName': "Alyssa Williams", 
            "userImage": "https://lh3.googleusercontent.com/-cVEHKr7mzv8/AAAAAAAAAAI/AAAAAAAAAAA/AKF05nB2r3GUkji31m0tC4ylFNiVMpmNWA/photo.jpg",
            "content": "This is literally the best idle game I have ever played. The penguins waddle around and live their best lives in the cutest little outfits. I just unlocked the little penguins and I have been sobbing uncontrollably for ten minutes because they are so adorable. There are only two suggestions I have for this game: more of the penguin info ads. I love them. I have learned so much about all the teeny fellas. Secondly, I would like to be able to name my 'guins so I can tell them apart.",
            "score": 5,
            "thumbsUpCount": 54,
            "reviewCreatedVersion": "1.16",
            "at": datetime.datetime(2020, 2, 24, 0, 0, 0),
            "replyContent": "Hello, We will gradually improve the various systems in the game to enhance the player's game experience. We have recorded your suggestions and feedback to the planner. If you have any other suggestions and ideas, please feel free to contact us at penguinisle@habby.com.Thank you for playing!",
            "repliedAt": datetime.datetime(2020, 2, 24, 18, 30, 42),
            "reviewId": "gp:AOqpTOE0Iy5S9Je1F8W1BgCl6l_TCFP_QN4qGtRATX3PeB5VV9aZu6UHfMWdYFF1at4qZ59xxLNHFqYLql5SL-k"
        },
        {
        "userName": "EasyJet 123",
        "userImage": "https://lh3.googleusercontent.com/a-/AOh14GhE3-Fsq5KDs_kmCRGcifbNUQTOtK5DpZkJ2AiqyQ",
        "content": "Easily my favorite game. Relaxing, with easy controls, no purchase necessary to advance... I love it. 100% recommend. I love how you can get gems continually by completing missions, and the low price of boosts are great. But how about adding new buildings like an airport, an army base, and a train station? Would be great to see these. And the building purchase price might be lowered so it's a bit easier to progress after the Igloo. Maybe...",
        "score": 5,
        "thumbsUpCount": 79,
        "reviewCreatedVersion": "1.14",
        "at": datetime.datetime(2020, 2, 12, 0, 0, 0),
        "replyContent": None,
        "repliedAt": None,
        "reviewId": "gp:AOqpTOHyQo9QEPtxefmvjNuqR9VmFyBaj2FNXLvHsuH19de9bC0dT_voHWSKNGFcc10jv077wOdzBrkgLKX6pUc"
        },
        {
            "userName": "Lillemann",
            "userImage": "https://lh3.googleusercontent.com/a-/AOh14GjiVSIrx033k9HZ9Tu4BQ1iYZST0IRW8UlDCX3gdw",
            "content": "Really good looking. And it runs super super smooth. I love the camera options when clicking the camera button. And the penguins looks absolutely awesome and I really love the limited eddition ones. That sometimes the ads are replaced with penguin facts is just awesome. I suggest that you set up some kind of leaderboard it could probobly show the players that are earning the most money per sec or something. But overall this game is a strong 10/10",
            "score": 5,
            "thumbsUpCount": 2,
            "reviewCreatedVersion": "1.14",
            "at": datetime.datetime(2020, 2, 11, 0, 0, 0),
            "replyContent": "Thank you very much for your review concerning our game. We will try our best to do better,If you have any other feedback or suggestions, feel free to contact us at penguinisle@habby.com. Have a nice day!",
            "repliedAt": datetime.datetime(2020, 2, 11, 0, 0, 0),
            "reviewId": "gp:AOqpTOEGUPB6HA0DIPNp3K2yAHRK-GN96dVJ-zkhPgKpclevgt8q9nR6Pv4N_F4TIPCpMeaoTutNGOZ2CSs65Ws"
        },
        ]
        filtered_reviews = [
            {
            'userName': "Alyssa Williams", 
            "userImage": "https://lh3.googleusercontent.com/-cVEHKr7mzv8/AAAAAAAAAAI/AAAAAAAAAAA/AKF05nB2r3GUkji31m0tC4ylFNiVMpmNWA/photo.jpg",
            "content": "This is literally the best idle game I have ever played. The penguins waddle around and live their best lives in the cutest little outfits. I just unlocked the little penguins and I have been sobbing uncontrollably for ten minutes because they are so adorable. There are only two suggestions I have for this game: more of the penguin info ads. I love them. I have learned so much about all the teeny fellas. Secondly, I would like to be able to name my 'guins so I can tell them apart.",
            "score": 5,
            "thumbsUpCount": 54,
            "reviewCreatedVersion": "1.16",
            "at": datetime.datetime(2020, 2, 24, 0, 0, 0),
            "replyContent": "Hello, We will gradually improve the various systems in the game to enhance the player's game experience. We have recorded your suggestions and feedback to the planner. If you have any other suggestions and ideas, please feel free to contact us at penguinisle@habby.com.Thank you for playing!",
            "repliedAt": datetime.datetime(2020, 2, 24, 18, 30, 42),
            "reviewId": "gp:AOqpTOE0Iy5S9Je1F8W1BgCl6l_TCFP_QN4qGtRATX3PeB5VV9aZu6UHfMWdYFF1at4qZ59xxLNHFqYLql5SL-k"
            },
        ]
        reviews = filter_reviews_by_date("17/02/2020", "24/02/2020", reviews)
        self.assertEqual(reviews, filtered_reviews)

    def test_replace_urls(self):
        reviews = [
            {
            'userName': "Alyssa Williams", 
            "userImage": "https://lh3.googleusercontent.com/-cVEHKr7mzv8/AAAAAAAAAAI/AAAAAAAAAAA/AKF05nB2r3GUkji31m0tC4ylFNiVMpmNWA/photo.jpg",
            "content": "this is a submission text that contains the URL https://www.reddit.com/ for replacing",
            "score": 5,
            "thumbsUpCount": 54,
            "reviewCreatedVersion": "1.16",
            "at": datetime.datetime(2020, 2, 24, 0, 0, 0),
            "replyContent": "Hello, We will gradually improve the various systems in the game to enhance the player's game experience. We have recorded your suggestions and feedback to the planner. If you have any other suggestions and ideas, please feel free to contact us at penguinisle@habby.com.Thank you for playing!",
            "repliedAt": datetime.datetime(2020, 2, 24, 18, 30, 42),
            "reviewId": "gp:AOqpTOE0Iy5S9Je1F8W1BgCl6l_TCFP_QN4qGtRATX3PeB5VV9aZu6UHfMWdYFF1at4qZ59xxLNHFqYLql5SL-k"
            },
        ]
        replaced_reviews = [
            {
            'userName': "Alyssa Williams", 
            "userImage": "https://lh3.googleusercontent.com/-cVEHKr7mzv8/AAAAAAAAAAI/AAAAAAAAAAA/AKF05nB2r3GUkji31m0tC4ylFNiVMpmNWA/photo.jpg",
            "content": "this is a submission text that contains the URL  for replacing",
            "score": 5,
            "thumbsUpCount": 54,
            "reviewCreatedVersion": "1.16",
            "at": datetime.datetime(2020, 2, 24, 0, 0, 0),
            "replyContent": "Hello, We will gradually improve the various systems in the game to enhance the player's game experience. We have recorded your suggestions and feedback to the planner. If you have any other suggestions and ideas, please feel free to contact us at penguinisle@habby.com.Thank you for playing!",
            "repliedAt": datetime.datetime(2020, 2, 24, 18, 30, 42),
            "reviewId": "gp:AOqpTOE0Iy5S9Je1F8W1BgCl6l_TCFP_QN4qGtRATX3PeB5VV9aZu6UHfMWdYFF1at4qZ59xxLNHFqYLql5SL-k"
            },
        ]
        
        reviews = app_reviews_replace_urls(reviews)
        
        self.assertEqual(reviews[0]['content'], replaced_reviews[0]['content'])
        
if __name__ == '__main__':
    unittest.main()