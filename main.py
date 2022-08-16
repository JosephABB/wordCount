from auth import authenticate

user_in = input('Enter subreddit in following format "r/news": ')
x = authenticate('WjBdU3M9ao2qn8P1SZ6EmQ', 'C:/Users/josep/wordCount/secretKey.txt', user_in)

print(x)
