

import requests # this is for handling API requests
import random # random.choice() for lists
import datetime # this is for the daily Bebop quotes function

def daily_bebop_quote() -> str:
    # generates a random Bebop quote from our API URL
    todays_date = datetime.date.today() # today's date
    print("----------------- DAILY BEBOP QUOTES -----------------")
    print(f"Current Date: {todays_date}")
    quotes = requests.get('https://animechan.vercel.app/api/quotes/anime?title=cowboy bebop').json()
    quote = random.choice(quotes) # dictionary w/ random quote we want
    return f"{quote['quote']} - {quote['character']}" # returns the quote and who said it


if __name__ == "__main__":
    q = daily_bebop_quote()
    print(q)