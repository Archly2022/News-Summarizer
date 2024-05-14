from dotenv import find_dotenv, load_dotenv
import requests
import os



# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.environ.get('api_key')

def get_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4XX or 5XX errors

        news_data = response.json()
        articles = news_data.get("articles", [])

        final_news = []

        for article in articles:
            title = article.get("title")
            
            author = article.get("author")
            
            description = article.get("description")
            url = article.get("url")
            url_to_image = article.get("urlToImage")
            content = article.get("content")

            # Constructing formatted string for each article
            article_info = f"""
                Title: {title}
                Author: {author}
                Description: {description}
                Url: {url}
                UrlToImage: {url_to_image}
                Content: {content}
            """
            final_news.append(article_info)

        return final_news

    except requests.exceptions.RequestException as e:
        print("Error occurred during API request:", e)
        return []
        
        

