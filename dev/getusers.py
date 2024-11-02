from instagrapi import Client
from info import *
import pickle

try:
    cl = Client()
    cl.load_settings("session.json")
    cl.login(USERNAME,PASSWORD) # this doesn't actually login using username/password but uses the session
    cl.get_timeline_feed()
    print(f"session checked out")
except Exception as e:
    print(f"Login failed:{e}")
    
posts = [
    "https://www.instagram.com/p/C4F14qFtyEW/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==",
]

users = []

for post in posts:
    try:
        pk = cl.media_pk_from_url(post)
        post_id = cl.media_id(pk)
        likers = cl.media_likers(post_id)
        print(f"{post_id} likers geted")
    except Exception as e:
        print(f"Error cant get likers : {e}")
    for liker in likers:
        try:
            if liker not in users:
                users.append(liker)
                print(f"{liker.username} added")
        except Exception as e:
            print(f"cant get user {e}")
    
num = 0
for user in users:
    num = num + 1
print(f"all users added : {num}")

try:
    with open("users.pkl", "wb") as f: 
        pickle.dump(users, f) 
    print("users.pkl saved")
except Exception as e:
    print(f"Error to save pickle:{e}")