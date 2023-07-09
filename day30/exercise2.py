facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    # s272-1-1-1 访问dict的时候捕获keyerror
    try:
        likes = post['Likes']
    except KeyError:
        print("there is a key error")
    else:
        total_likes = total_likes + likes


print(total_likes)