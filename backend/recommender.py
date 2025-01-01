from typing import List, Tuple
from data_manager import DataManager
from similarity import SimilarityCalculator

class ContentRecommender:
    def __init__(self, data_manager: DataManager, similarity_calculator: SimilarityCalculator):
        self.data_manager = data_manager
        self.similarity_calculator = similarity_calculator
        self._fit_similarity_calculator()

    def _fit_similarity_calculator(self) -> None:
        """Prepare the similarity calculator with the current dataset."""
        if self.data_manager.data is None:
            raise ValueError("No data loaded in DataManager")
        
        descriptions = self.data_manager.data['description'].fillna('').tolist()
        titles = self.data_manager.data['title'].tolist()
        self.similarity_calculator.fit(descriptions, titles)

    def find_similar_content(self, title: str, n: int = 5) -> List[Tuple[str, float]]:
        """Find n most similar titles to the given title."""
        if title not in self.data_manager.data['title'].values:
            raise ValueError(f"Title '{title}' not found in dataset")

        title_idx = self.data_manager.data[self.data_manager.data['title'] == title].index[0]
        return self.similarity_calculator.get_similar_items(title_idx, n)

class UserBasedRecommender:
    def __init__(self, data_manager: DataManager, similarity_calculator: SimilarityCalculator):
        self.data_manager = data_manager
        self.similarity_calculator = similarity_calculator

    def recommend_from_ratings(self, user_ratings: Dict[str, float], count: int) -> List[tuple]:
        if not user_ratings:
            return []
            
        recommendations = []
        for _, content in self.data_manager.data.iterrows():
            title = content['title']
            if title in user_ratings:
                continue
                
            total_score = self.calculate_rating_score(content, user_ratings)
            recommendations.append((title, total_score))
            
        return sorted(recommendations, key=lambda x: x[1], reverse=True)[:count]

    def calculate_rating_score(self, content: pd.Series, user_ratings: Dict[str, float]) -> float:
        total_score = 0
        for rated_title, rating in user_ratings.items():
            rated_description = self.data_manager.data[self.data_manager.data['title'] == rated_title]['description'].iloc[0]
            similarity = self.similarity_calculator.calculate_text_similarity(rated_description, content['description'])
            total_score += similarity * (rating / 10.0)
        return total_score
