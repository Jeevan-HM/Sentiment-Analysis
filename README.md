# Sentiment Analysis Flask App

This application performs sentiment analysis on input text and stores the results in a SQLite database.

## Project Files

### requirements.txt

This file contains all the dependencies required to run this project.

To install all the dependencies listed in this file, navigate to the directory containing the `requirements.txt` file and run the following command in your terminal:

```bash
pip install -r requirements.txt
```

### app.py

It's a Flask application that performs sentiment analysis on input text and stores the results in a SQLite database.

#### Functions/Methods:

1. `initialize_database()`: Initializes the SQLite database and creates a table if it doesn't exist.
2. `insert_into_database(input_text, polarity, sentiment)`: Inserts the input text, polarity, and sentiment into the database.
3. `analyze_sentiment(text)`: Analyzes the sentiment of the input text and returns the polarity.
4. `interpret_polarity(polarity)`: Interprets the polarity value and returns 'Positive', 'Negative', or 'Neutral'.
5. `analyze_sentiment_api()`: A Flask route that accepts POST requests, analyzes the sentiment, interprets the polarity, inserts the data into the database, and returns the predicted sentiment.

#### Usage:

To use the sentiment analysis API, make a POST request to '/analyze_sentiment' with a JSON body that contains the 'input' field. For example:

```bash
python3 app.py
curl -X POST -H "Content-Type: application/json" -d '{"input":"I love this product!"}' http://127.0.0.1:5000/analyze_sentiment
```

Alternatively, you can also use Postman to get the output by using the following URL: `http://127.0.0.1:5000/analyze_sentiment` and provide a raw, JSON body in the format: `{"input": text}`

#### Notes:

The application initializes the database and starts running when the file is executed. The database file 'sentiment_analysis.db' is assumed to be in the same directory as this file. The application runs in debug mode.
