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
movies_path = os.path.join(current_dir, 'movies.csv')
shows_path = os.path.join(current_dir, 'tv_shows.csv')

# Initialize components
data_manager = DataManager(movies_path=movies_path, shows_path=shows_path)
data_manager.load_content('movies')  # This loads movies into data_manager.data
similarity_calculator = SimilarityCalculator()
recommender = ContentRecommender(data_manager, similarity_calculator)

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    title = data.get('title')
    number_of_recommendations = data.get('count', 5)
    
    try:
        # Check if title exists in dataset (exact match only)
        all_titles = data_manager.data['title'].tolist()
        if title not in all_titles:
            return jsonify({
                'error': f'Title "{title}" not found in our database. Please check the title and try again.',
                'available_titles': all_titles[:10]  # Show first 10 titles as suggestions
            }), 404
            
        # Get recommendations with descriptions
        similar_content = recommender.find_similar_content(title, number_of_recommendations)
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
