#create visualization depending on the lexical category chosen
import matplotlib.pyplot as plt
import pandas

def find_lex (lex_cat, words_df):
    # Appends words that match lexical category to new df
    lex_cat_df = pandas.DataFrame()

    for i in range(len(words_df)):
        #creates dataframe of each unique word that matches lexical category
        if words_df.at[i, 'Lexical Category'] == lex_cat:
            lex_cat_df = lex_cat_df.append({
                'Word': words_df.at[i, 'Word']
            }, ignore_index=True)

    lex_cat_df = lex_cat_df['Word'].str.lower().value_counts().reset_index()
    lex_cat_df.columns = ['Word', 'Frequency']
    return lex_cat_df

def vizualize (lex_cat_df, lex_cat):
    # plot horizontal bar plot
    lex_cat_df.nlargest(10, 'Frequency').plot.barh(x="Word", y="Frequency")
    plt.title('Most Common ' + lex_cat + "'s")
    plt.show()

