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
    
try:
    followings = cl.user_following(cl.user_id_from_username("gem.off"))
    print("followings getted")
except Exception as e:
    print(f"Error cant get followings : {e}")
    
try:
    with open("followings.pkl", "wb") as f: 
        pickle.dump(followings, f) 
    print("followings.pkl saved")
except Exception as e:
    print(f"Error to save pickle:{e}")