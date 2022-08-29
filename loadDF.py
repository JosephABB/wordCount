#Load raw json data into dataframe
import pandas as pd

def load(raw_data):
    titles_dataframe = pd.DataFrame()

    for post in raw_data:
        titles_dataframe = titles_dataframe.append({
            'title': post['data']['title']}, ignore_index=True)

    return titles_dataframe