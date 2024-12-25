from typing import Dict
from data_manager import DataManager


class UserInterface:
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

    def collect_user_ratings(self) -> Dict[str, float]:
        ratings = {}
        print('\nPlease rate items (1-10), or type "skip" to continue:')
        print('(Type "search" followed by a word to search for titles)\n')
        
        while True:
            title = input('Enter a title. Type "done" after you have added your desired amount of titles: ').strip()
            
            if title.lower() in ['done', 'skip']:
                break
                
            if title.lower().startswith('search '):
                self.handle_search(title[7:])
                continue
            
            if title in self.data_manager.data['title'].values:
                rating = self.get_rating(title)
                if rating:
                    ratings[title] = rating
            else:
                print('Title not found. Try searching for other available titles.')
                
        return ratings

    def handle_search(self, term: str) -> None:
        results = self.data_manager.search_titles(term)
        if results:
            print('\nAvailable titles:')
            for title in results:
                print(f'- {title}')
        else:
            print('No matching titles were found.')

    def get_rating(self, title: str) -> float:
        try:
            rating = float(input(f'Rate {title} (1-10): '))
            if 1 <= rating <= 10:
                return rating
            print('Please enter a rating between 1 and 10.')
        except ValueError:
            print('Invalid rating. Please enter a number between 1 and 10.')
        return None
