#Authentication module for reddit API
def authenticate (CLIENT_ID, SECRET_KEY_FILE):
    import requests

   #CLIENT_ID = 'WjBdU3M9ao2qn8P1SZ6EmQ'
    with open(SECRET_KEY_FILE, 'r') as f:
        SECRET_KEY = f.read()

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

    with open('C:/Users/josep/OneDrive/Documents/API_project/pw.txt', 'r') as f:
        pw = f.read()

    data = {
        'grant_type': 'password',
        'username': 'Ok_Currency_4100',
        'password': pw
    }

    headers = {'User-Agent': 'MyAPI/0.0.1'}

    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    TOKEN = res.json()['access_token']

    headers['Authorization'] = f'bearer {TOKEN}'

    res = requests.get('https://oauth.reddit.com/r/news/hot',
                    headers=headers, params={'limit': '100'})

    print('connected')