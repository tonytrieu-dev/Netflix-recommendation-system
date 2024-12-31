from typing import List, Dict
import pandas as pd

class DataManager:
    def __init__(self, movies_path: str, shows_path: str):
        self.movies_path = movies_path
        self.shows_path = shows_path
        self.data = None

    def load_content(self, content_type: str) -> pd.DataFrame:
        file_path = self.movies_path if content_type == 'movies' else self.shows_path
        self.data = pd.read_csv(file_path)[['title', 'description']]
        return self.data

    def search_titles(self, search_term: str) -> List[str]:
        return self.data[self.data['title'].str.contains(
            search_term, case=False, na=False)]['title'].tolist()
    