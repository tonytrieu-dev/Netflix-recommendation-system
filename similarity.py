class SimilarityCalculator:
    @staticmethod
    def calculate_text_similarity(reference_description: str, current_description: str) -> float:
        first_unique_wordset = set(reference_description.lower().split())
        second_unique_wordset = set(current_description.lower().split())
        return len(first_unique_wordset & second_unique_wordset) / len(first_unique_wordset | second_unique_wordset)
