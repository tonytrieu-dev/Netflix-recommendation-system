from typing import List, Tuple, Set, Dict

class SimilarityCalculator:
    @staticmethod
    def preprocess_text(text: str) -> Set[str]:
        """
        Clean and preprocess text by:
        1. Converting to lowercase
        2. Removing special characters
        3. Removing common words
        4. Splitting into words
        """
        # Common words to remove
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        
        # Convert to lowercase and remove special characters
        text = text.lower()
        text = ''.join(c for c in text if c.isalnum() or c.isspace())
        
        # Split into words and remove common words
        words = set(text.split())
        return words - common_words

    @staticmethod
    def calculate_jaccard_similarity(first_set: Set[str], second_set: Set[str]) -> float:
        """
        Calculate Jaccard similarity between two sets of words.
        Jaccard similarity = size of intersection / size of union
        """
        if not first_set or not second_set:
            return 0.0
            
        intersection = len(first_set.intersection(second_set))
        union = len(first_set.union(second_set))
        
        return intersection / union if union > 0 else 0.0

    def calculate_content_similarity(self, first_movie: Dict[str, str], second_movie: Dict[str, str]) -> float:
        """
        Calculate similarity between two movies using multiple features:
        1. Description similarity (50% weight)
        2. Genre similarity (30% weight)
        3. Title word similarity (20% weight)
        """
        # Calculate description similarity
        description_similarity = self.calculate_jaccard_similarity(
            self.preprocess_text(first_movie.get('description', '')),
            self.preprocess_text(second_movie.get('description', ''))
        )
        
        # Calculate genre similarity
        genre_similarity = self.calculate_jaccard_similarity(
            self.preprocess_text(first_movie.get('listed_in', '')),
            self.preprocess_text(second_movie.get('listed_in', ''))
        )
        
        # Calculate title word similarity
        title_similarity = self.calculate_jaccard_similarity(
            self.preprocess_text(first_movie.get('title', '')),
            self.preprocess_text(second_movie.get('title', ''))
        )
        
        # Weighted average of similarities
        return (
            0.5 * description_similarity +
            0.3 * genre_similarity +
            0.2 * title_similarity
        )
