import requests
from termcolor import colored

def get_random_wikipedia_article():
    try:
        # Fetch random article from Wikipedia API
        url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&generator=random&grnnamespace=0'
        response = requests.get(url)
        data = response.json()

        # Get the random article ID
        page_id = list(data['query']['pages'].keys())[0]
        article_title = data['query']['pages'][page_id]['title']

        # Generate the link
        article_link = f'https://en.wikipedia.org/wiki/{article_title}'
        
        print(colored(article_link, "light_blue"))
        return article_link
    except Exception as e:
        print(colored('Error', "light_red"), colored(e, "light_red"))


if __name__ == "__main__":
  # Get and print the random Wikipedia article link
  get_random_wikipedia_article()
