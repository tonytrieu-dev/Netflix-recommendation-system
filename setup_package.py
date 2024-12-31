import os
import shutil

# Create netflix_recommender directory if it doesn't exist
if not os.path.exists('netflix_recommender'):
    os.makedirs('netflix_recommender')

# Files to move
files = [
    'data_manager.py',
    'hybrid_recommender.py',
    'recommender.py',
    'similarity.py',
    'user_interface.py',
]

# Move files
for file in files:
    if os.path.exists(file):
        shutil.copy2(file, os.path.join('netflix_recommender', file))

# Move data files
for data_file in ['movies.csv', 'tv_shows.csv']:
    if os.path.exists(data_file):
        shutil.copy2(data_file, os.path.join('netflix_recommender', data_file))
