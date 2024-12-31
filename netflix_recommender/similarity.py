class SimilarityCalculator:
    @staticmethod
    def calculate_text_similarity(recently_watched_description: str, comparison_title_description: str) -> float:
        first_unique_wordset = set(recently_watched_description.lower().split())
        second_unique_wordset = set(comparison_title_description.lower().split())
        return len(first_unique_wordset & second_unique_wordset) / len(first_unique_wordset | second_unique_wordset)
