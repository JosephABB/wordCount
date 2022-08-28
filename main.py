from auth import authenticate
from loadDF import load

user_in = input('Enter subreddit in following format "r/news": ')
raw_data = authenticate('WjBdU3M9ao2qn8P1SZ6EmQ', 'C:/Users/josep/wordCount/secretKey.txt', user_in)

titles_df = load(raw_data)

print(titles_df.to_string())
