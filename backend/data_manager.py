from typing import Dict, Any
import pandas as pd

class DataManager:
    def __init__(self, movies_path: str, shows_path: str):
        """Initialize DataManager with paths to data files."""
        self.movies_path = movies_path
        self.shows_path = shows_path
        self.data = None

    def load_content(self, content_type: str = 'all') -> None:
        """Load content data based on type."""
        if content_type == 'movies':
            self.data = pd.read_csv(self.movies_path)
        elif content_type == 'shows':
            self.data = pd.read_csv(self.shows_path)
        elif content_type == 'all':
            # Load both movies and shows
            movies_df = pd.read_csv(self.movies_path)
            shows_df = pd.read_csv(self.shows_path)
            
            # Combine the datasets
            self.data = pd.concat([movies_df, shows_df], ignore_index=True)
        else:
            raise ValueError("Invalid content type. Use 'movies', 'shows', or 'all'.")
        
        # Ensure we have a consistent title column
        if 'title' not in self.data.columns:
            if 'name' in self.data.columns:
                self.data = self.data.rename(columns={'name': 'title'})
            elif 'show_title' in self.data.columns:
                self.data = self.data.rename(columns={'show_title': 'title'})
            else:
                raise ValueError("No title column found in the dataset")
        
        # Remove any duplicate titles, keeping the first occurrence
        self.data = self.data.drop_duplicates(subset=['title'], keep='first')

    def get_content_features(self, title: str) -> Dict[str, Any]:
        """Get features for a specific title."""
        if self.data is None:
            raise ValueError("No data loaded. Call load_content() first.")
        
        content = self.data[self.data['title'] == title]
        if content.empty:
            raise ValueError(f"Title '{title}' not found in dataset.")
        
        return content.iloc[0].to_dict()