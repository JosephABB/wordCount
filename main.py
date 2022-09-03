from auth import authenticate
from loadDF import load
from wordStats import load_words
from viz import find_lex
from viz import vizualize

reddit_in = input('Enter subreddit in following format "r/news": ')
lex_in = input('Enter a lexical category abbreviation in all caps (For options enter ?): ')

if lex_in == '?':
    print("\nJJ (ordinal adjective or numeral), JJR (comparitive adjective), JJS (superlative adjective), NN (common noun),"
          " NNP (proper singular noun), NNS (common plural noun), \nVB (base form verb), VBD (past tense verb),"
          " VBG (present participle or gerund verb), VBN (past particle verb), VBP (present tense verb), \nVBZ (3rd person singular present tense verb)\n")
    lex_in = input('Enter a lexical category abbreviation in all caps: ')

# Connect to API
raw_data = authenticate('WjBdU3M9ao2qn8P1SZ6EmQ', 'C:/Users/josep/wordCount/secretKey.txt', reddit_in)

# load json titles from the hottest posts from user selected subreddit into a dataframe
titles_df = load(raw_data)

# load verbs, nouns, adjectives into a dataframe
words_df = load_words(titles_df)

# load words from specific lexical category into a dataframe and count the frequency of the words
lex_in_df = find_lex(lex_in, words_df)

# visualize the most frequently used words
visual = vizualize(lex_in_df, lex_in)



