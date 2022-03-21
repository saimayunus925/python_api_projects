

import requests # this is for handling API requests
import random # random.choice() for lists

def daily_bebop_quote() -> str:
    # generates a random Bebop quote from our API URL
    quotes = requests.get('https://animechan.vercel.app/api/quotes/anime?title=cowboy bebop').json()
    quote = random.choice(quotes) # dictionary w/ random quote we want
    print(f"{quote['quote']} - {quote['character']}") # prints the quote and who said it

if __name__ == "__main__":
    daily_bebop_quote()