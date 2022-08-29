from auth import authenticate
from loadDF import load
from wordStats import load_words

user_in = input('Enter subreddit in following format "r/news": ')
raw_data = authenticate('WjBdU3M9ao2qn8P1SZ6EmQ', 'C:/Users/josep/wordCount/secretKey.txt', user_in)
titles_df = load(raw_data)
words_df = load_words(titles_df)

print(words_df.to_string())
