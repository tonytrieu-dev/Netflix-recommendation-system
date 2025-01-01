from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender import ContentRecommender
from data_manager import DataManager
from similarity import SimilarityCalculator
import os

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
        # Preprocess the title for flexible matching
        def preprocess_title(t):
            # Convert to lowercase and remove punctuation
            import re
            return re.sub(r'[^\w\s]', '', t).lower()
        
        # Normalize the input title
        normalized_input = preprocess_title(title)
        
        # Find matching titles (case and punctuation insensitive)
        matching_titles = data_manager.data[
            data_manager.data['title'].apply(preprocess_title).str.contains(normalized_input)
        ]
        
        if matching_titles.empty:
            return jsonify({'error': f'No titles found matching "{title}"'}), 404
        
        # Use the first matching title for recommendations
        matched_title = matching_titles['title'].iloc[0]
        
        # Get recommendations with descriptions
        similar_content = recommender.find_similar_content(matched_title, number_of_recommendations)
        recommendations = []
        
        for title, similarity in similar_content:
            description = data_manager.data[data_manager.data['title'] == title]['description'].iloc[0]
            recommendations.append({
                'title': title,
                'description': description,
                'similarity': similarity
            })
            
        return jsonify({'recommendations': recommendations})
        
    except Exception as error:
        return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
