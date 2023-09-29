# Import necessary libraries
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


app = Flask(__name__)
CORS(app, resources={r"/generate-insights": {"origins": "http://localhost:3000"}}, supports_credentials=True, methods=["POST"])

# # Function to generate a line chart
# def generate_chart():
#     # Sample data (replace with your own data)
#     x = [1, 2, 3, 4, 5]
#     y = [10, 20, 25, 30, 35]

#     # Create a line chart
#     plt.figure(figsize=(10, 6))
#     plt.plot(x, y, marker='o', linestyle='-')
#     plt.title('Sample Line Chart')
#     plt.xlabel('X-Axis')
#     plt.ylabel('Y-Axis')
#     plt.grid(True)
#     plt.tight_layout()

#     # Save the chart as an image
#     chart_image = BytesIO()
#     plt.savefig(chart_image, format='png')
#     chart_image.seek(0)  # Reset the image file position to the beginning

#     return chart_image

# # Function to extract relevant information from the article
# def extract_data(article_text):
#     data = {"Date": None, "MarketData": []}

#     # Extract date from the article text (modify this based on the article's structure)
#     date_match = re.search(r"(\w+\s*\d{1,2},?\s*\d{4}\s*at\s*\d{1,2}:\d{2}\s*[APM]+)", article_text)
#     if date_match:
#         article_date = date_match.group(0)
#         article_date = re.sub(r',', '', article_date)
#         article_date = re.sub(r'\s+', ' ', article_date)
#         article_date = datetime.strptime(article_date, "%B %d %Y at %I:%M %p")
#         data["Date"] = article_date

#     # Extract market data from the article text (modify this based on the article's structure)
#     market_data_matches = re.findall(r"([A-Z]+)\s+([+-]?\d+\.\d+%)", article_text)
#     if market_data_matches:
#         for symbol, change in market_data_matches:
#             data["MarketData"].append(f"{symbol} {change}")

#     return data


# # Function to generate insights based on market data
# def generate_market_insights(data):
#     insights = []
#     if data["MarketData"]:
#         insights.append("Market Data:")
#         insights.extend(data["MarketData"])
#     else:
#         insights.append("No market data found in the article.")
#     return insights


# # Function to analyze trends (Replace with your trend analysis logic)
# def analyze_trends():
#     trend_insights = ["Trend analysis: Replace with actual trend insights"]
#     return trend_insights

# # Function to analyze sentiment and generate insights
# def analyze_sentiment(article_texts):
#     sia = SentimentIntensityAnalyzer()
#     insights = []

#     # Log the scraped data
#     print("Scraped Data from <article> elements:")
#     for text in article_texts:
#         sentiment_scores = sia.polarity_scores(text)
#         sentiment = sentiment_scores['compound']

#         # Determine sentiment and generate insights
#         if sentiment > 0.2:
#             insights.append(f"Positive sentiment detected in: {text}")
#         elif sentiment < -0.2:
#             insights.append(f"Negative sentiment detected in: {text}")
#         else:
#             insights.append(f"Neutral sentiment detected in: {text}")

#         print(text)

#     return insights

# # Function to extract and analyze data from the provided article
# def extract_and_analyze_data(article_text):
#     # Parse the article text and extract relevant data
#     data = extract_data(article_text)
    
#     # Generate market insights based on extracted data
#     insights = generate_market_insights(data)
    
#     # Generate a chart
#     chart_image = generate_chart()
    
#     return insights, chart_image

def scrape_data(url):
    try:
        # Set up the Selenium WebDriver (update the path to your WebDriver)
        driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

        # Load the webpage
        driver.get(url)

        # Wait for the element to appear (adjust timeout as needed)
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'xray-fin-streamer')))

        # Extract the text from the element
        element_text = element.text.strip()

        # Close the browser
        driver.quit()

        # Now, 'element_text' contains the content you scraped
        print("Scraped element content:", element_text)

        return {"content": element_text}

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {"error": str(e)}

@app.route('/generate-insights', methods=['POST'])
def generate_market_data():
    try:
        data = request.get_json()
        news_site_url = data.get('newsSite')

        if not news_site_url:
            return jsonify({"error": "News site URL is required."}), 400

        # Scrape data from the news site URL
        scraping_result = scrape_data(news_site_url)

        if "error" in scraping_result:
            return jsonify(scraping_result), 400

        # Return market data in JSON format
        return jsonify(scraping_result)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)