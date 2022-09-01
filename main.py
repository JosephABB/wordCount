from auth import authenticate
from loadDF import load
from wordStats import load_words
from viz import find_lex
from viz import vizualize

reddit_in = input('Enter subreddit in following format "r/news": ')
lex_in = input('Enter a lexical category abbreviation in all caps: ')


raw_data = authenticate('WjBdU3M9ao2qn8P1SZ6EmQ', 'C:/Users/josep/wordCount/secretKey.txt', reddit_in)
# Connect to API

titles_df = load(raw_data)
# load json titles from the hottest posts from user selected subreddit into a dataframe

words_df = load_words(titles_df)
# load verbs, nouns, adjectives into a dataframe

lex_in_df = find_lex(lex_in, words_df)
# load words from specific lexical category into a dataframe and count the frequency of the words

visual = vizualize(lex_in_df, lex_in)
# visualize the most frequently used words



