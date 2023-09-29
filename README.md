# AI Market Research Report

## Market Data Scraper and Insights Generator

### Overview

This project is a simple web application for scraping market data. It is intended to provide users with a basic understanding of how to extract financial market data from a website and display it on a web interface.

The primary function of this application is to scrape financial market data represented in the format `^GSPC +0.59%` or similar from a provided news site URL and present it as a JSON response on the frontend.

### Getting Started

To use this application, follow these steps:

1. Clone this repository to your local machine.

2. Install the required Python packages listed in `requirements.txt`. You can do this using pip.

3. Install the required JavaScript packages. Navigate to the frontend directory and run npm install.

4. Start the Python backend server using python app.py.

5. Start the React frontend development server using npm start.

6. Open your web browser and access the application at http://localhost:3000.

### How to Use

1. Enter the URL of the news site you want to scrape in the "News Site URL" input field.

2. Click the "Generate Insights" button.

3. The scraped market data will be displayed in JSON format on the frontend.

____
## Screenshot
You can place your category and input your URL.
![image](/public/MRR.png)
for this example we used this link : https://finance.yahoo.com/news/the-worst-government-shutdowns-and-the-stock-market-what-history-shows-usually-happens-142728907.html
____

### Future Enhancements

While this application serves as a basic example of web scraping and data presentation, you can consider adding the following features in the future:

- User Authentication: Implement user authentication to track user activity and provide a personalized experience.

- Database Storage: Store scraped data and user interaction history in a database for analysis and historical data retrieval.

- Sentiment Analysis: Incorporate sentiment analysis to provide insights into market sentiment based on news articles.

- Interactive Charts: Enhance the frontend to display interactive charts that visualize market data trends.

- Customization: Allow users to select specific financial instruments or customize the types of data they want to scrape.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

## Text-to-Video VSL Generator

### Overview

The Text-to-Video VSL Generator is a Python application that allows users to input text and generate a video with a voiceover reading the text while displaying it in the video. It's a versatile tool that can be used for various purposes, including creating Video Sales Letters (VSLs) and educational content.

**NOTE:** This is still a work in progress, so most of these functions will not be complete.

### Installation

To set up the project locally, follow these steps:

1. Clone the repository to your local machine.

2. Change to the project directory.

3. Install the required Python packages using pip.

4. Make sure you have the 'ImageMagick' binary installed. You can download it from the official website.

5. Run the application.

Now your Text-to-Video VSL Generator is up and running locally.

### Usage

To use the Text-to-Video VSL Generator, make a POST request to the /generate-video endpoint with the required parameters.

### Configuration Options

You can customize the appearance and behavior of the generated videos by adjusting the provided configuration options.

### Examples

Here are some usage examples of the Text-to-Video VSL Generator:

- Basic Usage: Generate a video with default settings.

- Customized Appearance: Customize font color and background color.

- Background Image: Add a background image to the video.

### Contributing

If you would like to contribute to this project, please follow the guidelines outlined in the repository.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Frontend

- Next.js
- Axios
- React

### Backend

- Python
- Flask
- Selenium
- BeautifulSoup

### Contact Information

If you have any questions or suggestions, feel free to contact me.
