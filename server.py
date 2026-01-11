from textblob import TextBlob
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/analyze', methods=['POST']) 
def analyze():
    print("Request received!")
    data = request.get_json()
    message = data['message']
    
    # Analyze sentiment with TextBlob
    blob = TextBlob(message)
    polarity = blob.sentiment.polarity  # -1 (negative) to 1 (positive)
    
    # Convert to label
    if polarity > 0:
        label = "POSITIVE"
    elif polarity < 0:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"
    
    result = {
        "label": label,
    }
    
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True)


 