from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender import ContentRecommender
from data_manager import DataManager
from similarity import SimilarityCalculator
import os
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define paths to data files
current_dir = os.path.dirname(os.path.abspath(__file__))
movies_path = os.path.join(current_dir, '../data/netflix_movies.csv')
shows_path = os.path.join(current_dir, '../data/netflix_shows.csv')

# Initialize components
data_manager = DataManager(movies_path=movies_path, shows_path=shows_path)
data_manager.load_content('all')  # Load both movies and shows
similarity_calculator = SimilarityCalculator()
recommender = ContentRecommender(data_manager, similarity_calculator)

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    title = data.get('title')
    number_of_recommendations = data.get('count', 5)
    
    try:
        # Get all titles and create a case-insensitive and punctuation-insensitive mapping
        all_titles = data_manager.data['title'].tolist()
        
        def normalize_title(t):
            # Convert to lowercase and remove punctuation
            return ''.join(c.lower() for c in t if c.isalnum() or c.isspace()).strip()
        
        # Create mapping from normalized titles to original titles
        title_mapping = {normalize_title(t): t for t in all_titles}
        
        # Normalize the search title
        normalized_search = normalize_title(title)
        
        # Check if the normalized version of the title exists
        if normalized_search not in title_mapping:
            return jsonify({
                'error': f'Title "{title}" not found in our database. Please check the title and try again.',
                'available_titles': all_titles[:10]  # Show first 10 titles as suggestions
            }), 404
            
        # Get the correctly formatted title from our mapping
        correct_title = title_mapping[normalized_search]
            
        # Get recommendations with descriptions
        similar_content = recommender.find_similar_content(correct_title, number_of_recommendations)
        recommendations = []
        
        for rec_title, similarity in similar_content:
            if rec_title in all_titles:  # Only include titles that exist in our dataset
                description = data_manager.data[data_manager.data['title'] == rec_title]['description'].iloc[0]
                recommendations.append({
                    'title': rec_title,
                    'description': description,
                    'similarity': similarity
                })
        
        if not recommendations:
            return jsonify({
                'error': 'No recommendations found for this title.',
                'available_titles': all_titles[:10]
            }), 404
            
        return jsonify({'recommendations': recommendations})
        
    except Exception as error:
        return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
