import pandas as pd
from typing import List, Dict, Tuple
from data_manager import DataManager
from hybrid_recommender import HybridRecommender
from recommender import ContentRecommender, UserBasedRecommender
from similarity import SimilarityCalculator
from user_interface import UserInterface

def main():
    data_manager = DataManager('movies.csv', 'tv_shows.csv')
    similarity_calculator = SimilarityCalculator()
    content_recommender = ContentRecommender(data_manager, similarity_calculator)
    user_based_recommender = UserBasedRecommender(data_manager, similarity_calculator)
    hybrid_recommender = HybridRecommender(content_recommender, user_based_recommender)
    user_interface = UserInterface(data_manager)

    print('Welcome to the Netflix Recommendation System!')
    
    content_type = input('Would you like recommendations for movies or TV shows? ').lower()
    while content_type not in ['movies', 'tv shows']:
        print('Please enter either movies or tv shows')
        content_type = input('Would you like recommendations for movies or TV shows? ').lower()
    
    last_watched_content = content_type
    if last_watched_content == 'movies':
        last_watched_content = 'movie'
    else:
        last_watched_content = 'TV show'

    try:
        data_manager.load_content(content_type)
        user_ratings = user_interface.collect_user_ratings()

        while True:
            try:
                number_recommendations = int(input('\nHow many recommendations do you want? '))
                if number_recommendations > 0:
                    break
                else:
                    print('Please enter a positive number.')
            except ValueError:
                print('Invalid input. Please enter an integer.')
        
        recent_title = input(f'\nEnter a {last_watched_content} you have most recently watched: ').strip()
        while recent_title not in data_manager.data['title'].values:
            print('Title not found')
            recent_title = input(f'Enter a {last_watched_content} you have most recently watched: ').strip()

        print('\nPlease wait while the system generates recommendations...')
        recommendations = hybrid_recommender.get_recommendations(recent_title, user_ratings, number_recommendations)
        
        print(f'\nBased on your preferences, we recommend these {content_type}:\n')
        for index, title in enumerate(recommendations, 1):
            print(f'{index}. {title}')
            
    except Exception as error:
        print(f'An error occurred: {str(error)}')

if __name__ == '__main__':
    main()
