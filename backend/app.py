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
    count = data.get('count', 5)
    
    try:
        # First check if the title exists in our dataset
        if title not in data_manager.data['title'].values:
            return jsonify({'error': f'Title "{title}" not found in our database'}), 404
            
        similar_content = recommender.find_similar_content(title, count)
        # Convert the list of tuples to a list of titles for the frontend
        recommendations = [title for title, _ in similar_content]
        return jsonify({'recommendations': recommendations})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
