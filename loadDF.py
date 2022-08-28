#Load raw json data into dataframe
import pandas as pd

def load(raw_data):
    titles_dataframe = pd.DataFrame()

    '''for post in range(len(raw_data)):
        for key in raw_data[post]:
            titles_dataframe = titles_dataframe.append({'title': key['data']['children']['data']['title']}, ignore_index=True)
    '''
    for post in raw_data:
        titles_dataframe = titles_dataframe.append({
            'title': post['data']['title']}, ignore_index=True)

    return titles_dataframe