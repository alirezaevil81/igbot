from instagrapi import Client
from info import *
import pickle

try:
    cl = Client()
    print("Client created")
    cl.delay_range = [30, 60]
    print("delay seted")
    cl.load_settings("session.json")
    print("session loading")
    cl.login(USERNAME, PASSWORD)  # this doesn't actually login using username/password but uses the session
    cl.get_timeline_feed()
    print("timeline loading")
    print(f"session successfully loaded")
except Exception as e:
    print(f"Login failed:{e}")

try:
    with open("users.pkl", "rb") as f:
        users = pickle.load(f)
        print("users loaded from pickle")
except Exception as e:
    print(f"Error to load pickle:{e}")

try:
    my_id = str(cl.user_id_from_username("gem__off"))
    print("my id seted")
except Exception as e:
    print(f"Error set my id {e}")

for user in users:
    try:
        cl.user_follow(user.pk)
        print(f"following user: {user.username}")
    except Exception as e:
        print(f"Error to following {user.username}:{e}")
    user_posts = cl.user_medias(user.pk, 6)
    if user_posts != []:
        for post in user_posts:
            try:
                cl.media_like(post.pk)
                print(f"post {post.pk} liked")
            except Exception as e:
                print(f"Error:{e}")
    else:
        print(f"no posts found for {user.username}")
    try:
        cl.direct_send(
            f"سلام {user.username} جان😍 حالت چطوره ؟ 😉 می خوای کلی لباس ارزون بخری برای عید؟ 😄 فقط کافیه بیای تویه پیجم همه چی زیر قیمت باوری نداری خودت ببین ضرر که نداره 😌 👇👇👇",
            user_ids=[user.pk])
    except Exception as e:
        print(f"Error to sending message : {e}")
    try:
        cl.direct_profile_share(my_id, user_ids=[user.pk])
    except Exception as e:
        print(f"Error to sending message : {e}")

# --- for test purposes ---

# user = cl.user_info_by_username('gem__off')
# try:
#     user_posts = cl.user_medias(user.pk,3)
#     if user_posts != []:
#         for post in user_posts:
#             try:
#                 cl.media_like(post.pk)
#                 print(f"{post.pk} liked")
#             except Exception as e:
#                 print(f"Error:{e}")
#     else:
#         print(f"no posts found for {user.username}")
# except Exception as e:
#     print(f"Error{e}")

# --- send direct message ---

# try:
#     cl.direct_send(f"سلام {user.full_name} جان😍 حالت چطوره ؟ 😉 می خوای کلی لباس ارزون بخری برای عید؟ 😄 فقط کافیه بیای تویه پیجم همه چی زیر قیمت باوری نداری خودت ببین ضرر که نداره 😌 👇👇👇", user_ids=[user.pk])
# except Exception as e:
#     print(f"Error {e}")
# try:
#     my_id = str(cl.user_id_from_username("gem__off"))
#     cl.direct_profile_share(my_id, user_ids=[user.pk])
# except Exception as e:
#     print(f"Error {e}")

print("........................... succsess .........................................")
