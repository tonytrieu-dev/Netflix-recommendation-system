# Netflix Recommendation System

A full-stack app that provides personalized Netflix recommendations using a simple hybrid-based filtering system.

## Features

- Hybrid recommendation system that uses content-based filtering and collaborative filtering
- Easy-to-use interface for getting personalized recommendations
- Built-in dataset management for some Netflix content
- Frontend built with TypeScript for better maintainability
- Improved recommendation algorithms for enhanced accuracy

## Requirements

- Python >= 3.6
- pandas
- numpy
- scikit-learn
- TypeScript

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tonytrieu-dev/Netflix-recommendation-system
   cd Netflix-recommendation-system
   ```
2. Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

## Usage

1. Start the backend server:
   ```bash
   python backend/app.py
   ```
2. Start the frontend application:
   ```bash
   cd frontend
   npm start
   ```
3. Open your browser and navigate to `http://localhost:3000` to access the application.
