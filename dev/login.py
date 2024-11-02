from instagrapi import Client
from info import *

try:
    cl = Client()
    print("Client created")
except Exception as e:
    print(f"Error creating client {e}")
    
try:
    cl.login(USERNAME, PASSWORD, verification_code='333275')
    print("Login successful")
except Exception as e:
    print(f"Error logging in {e}")
    
try:
    cl.dump_settings("session.json")
    print("session dumped")
except Exception as e:
    print(f"Error dumping session {e}")

