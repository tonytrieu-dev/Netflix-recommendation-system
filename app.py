from flask import Flask, render_template, request, jsonify
from recommender import ContentRecommender
from data_manager import DataManager
from similarity import SimilarityCalculator

app = Flask(__name__)

# Initialize components
data_manager = DataManager()
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
