from flask import Flask, render_template, request, jsonify
from recommender import ContentRecommender
from data_manager import DataManager
from similarity import SimilarityCalculator
import os

app = Flask(__name__)

# Define paths to data files
current_dir = os.path.dirname(os.path.abspath(__file__))
movies_path = os.path.join(current_dir, 'movies.csv')
shows_path = os.path.join(current_dir, 'tv_shows.csv')

# Initialize components
data_manager = DataManager(movies_path=movies_path, shows_path=shows_path)
similarity_calculator = SimilarityCalculator()
recommender = ContentRecommender(data_manager, similarity_calculator)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    title = data.get('title')
    count = data.get('count', 5)
    
    try:
        recommendations = recommender.recommend_from_title(title, count)
        return jsonify({'recommendations': recommendations})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
