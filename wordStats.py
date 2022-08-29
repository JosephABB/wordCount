#load verbs, nouns, adjectives into a dataframe
#return a tables with the frequency of each word in each dataframe

from nltk.tokenize import word_tokenize
import nltk
import pandas as pd


def load_words(titles):
    words_df = pd.DataFrame()
    conditions = ['JJ', 'JJR', 'JJS', 'NN', 'NNP', 'NNS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

    for i in range(len(titles)):
        #iterate through titles
        text = word_tokenize(titles.at[i,'title'])
        word_list = nltk.pos_tag(text)
        for i in range(len(word_list)):
            #iterate through words and tags in title
            if word_list[i][1] in conditions:
                #if word matches conditional, append to dataframe
                words_df = words_df.append({
                    'Word': word_list[i][0],
                    'Lexical Category': word_list[i][1]
                }, ignore_index=True)

    return words_df





