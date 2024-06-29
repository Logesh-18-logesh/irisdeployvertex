from flask import Flask, jsonify, request
import numpy as np
import pickle

# Load the pickled model
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    # Validate input data
    required_features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    for feature in required_features:
        if feature not in data:
            return jsonify({'error': f'Missing feature: {feature}'}), 400

    # Extract features from JSON
    try:
        features = [float(data['sepal_length']), float(data['sepal_width']), float(data['petal_length']), float(data['petal_width'])]
    except ValueError:
        return jsonify({'error': 'One or more features are not numeric.'}), 400

    # Convert features to array and reshape for prediction
    X = np.array(features).reshape(1, -1)

    # Make prediction
    try:
        prediction = model.predict(X)
        return jsonify(prediction.tolist())
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error for model prediction issues
