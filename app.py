from flask import Flask, jsonify, request
from textblob import TextBlob
import sqlite3

app = Flask(__name__)

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('sentiment_analysis.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sentiment_analysis
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, input TEXT, polarity REAL, sentiment TEXT)''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_into_database(input_text, polarity, sentiment):
    conn = sqlite3.connect('sentiment_analysis.db')
    c = conn.cursor()
    c.execute("INSERT INTO sentiment_analysis (input, polarity, sentiment) VALUES (?, ?, ?)", (input_text, polarity, sentiment))
    conn.commit()
    conn.close()

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def interpret_polarity(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment_api():
    try:
        data = request.get_json()
        input_text = data['input']
        polarity = analyze_sentiment(input_text)
        sentiment = interpret_polarity(polarity)
        # Insert data into the database
        insert_into_database(input_text, polarity, sentiment)
        return jsonify({'Predicted Sentiment': sentiment}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Initialize the database
    initialize_database()
    app.run(port=5000)
