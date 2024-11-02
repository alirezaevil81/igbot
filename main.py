import os, pickle
from random import randint, choice
from time import sleep
from colorama import Fore, Style
from instagrapi import Client
from prettytable import PrettyTable

login_via_session = False
login = False

print(f"{Fore.YELLOW}[!Warning]: {Style.RESET_ALL}If your account does not have two-step verification, Enter the input verification code blank.\n")

while not login:

    username = input(f"Username{Fore.CYAN}(required){Style.RESET_ALL}: ")

    if os.path.exists(f"data/json/{username}.json"):
        session_input = input(
            f"{Fore.YELLOW}[Warning]:{Style.RESET_ALL}You have a session for {Fore.BLUE}{username}{Style.RESET_ALL}. Do you want to use it?[Default is Y] [Y/N]: ")
        if session_input.lower() in ('no', 'n', 'No', 'N', 'NO'):
            login_via_session = False
        else:
            login_via_session = True

    cl = Client()

    if login_via_session:
        try:
            cl.load_settings(f"data/json/{username}.json")
            cl.login(username, '')
            cl.get_timeline_feed()
        except Exception as e:
            print(f"{Fore.RED}[Error]:{Style.RESET_ALL}to login via session :{e}")
        else:
            login = True
            print(f"{Fore.GREEN}[Successful]:{Style.RESET_ALL}login via session successful!")
    else:
        password = input(f"Password{Fore.CYAN}(required){Style.RESET_ALL}: ")
        verify_code = input(f"Verify Code{Fore.YELLOW}(optional){Style.RESET_ALL}: ")
        try:
            cl.login(username=username, password=password, verification_code=verify_code)
            cl.dump_settings(f"data/json/{username}.json")
        except Exception as e:
            print(f"{Fore.RED}[Error]:{Style.RESET_ALL}to login :{e}")
        else:
            login = True
            print(f"{Fore.GREEN}[Successful]:{Style.RESET_ALL}login successful!")

start_via_pickle = False

if os.path.exists(f"data/pickle/users.pkl"):
    start_via_pickle = input(
        f"{Fore.YELLOW}[Warning]:{Style.RESET_ALL}You have a {Fore.CYAN}user pickle{Style.RESET_ALL} file, do you want to use it?[default is Y] [Y/N] : ")
    if start_via_pickle.lower() in ('n', 'no', 'No', 'N', 'NO'):
        start_via_pickle = False
    else:
        start_via_pickle = True

if start_via_pickle:
    try:
        with open("data/pickle/users.pkl", "rb") as f:
            users = pickle.load(f)
    except Exception as e:
        print(f"{Fore.RED}[Error]:{Style.RESET_ALL}to load pickle:{e}")
    else:
        print(f"{Fore.GREEN}[Successful]:{Style.RESET_ALL}users loaded from pickle")
else:
    posts = input(
        f"Enter the link of the posts whose users you want to extract {Fore.YELLOW}[separate the links with commas]{Style.RESET_ALL}\n posts: ")
    posts = posts.split(",")

    users = []

    for post in posts:
        try:
            pk = cl.media_pk_from_url(post)
            post_id = cl.media_id(pk)
            likers = cl.media_likers(post_id)
        except Exception as e:
            print(f"{Fore.RED}[Error]:{Style.RESET_ALL}cant get likers :{e}")
        else:
            print(
                f"{Fore.GREEN}[Successful]:{Style.RESET_ALL} from {Fore.MAGENTA}{post_id}{Style.RESET_ALL} likers geted")

        for liker in likers:
            try:
                if liker not in users:
                    users.append(liker)
                    print(f"{liker.username} added")
            except Exception as e:
                print(f"{Fore.RED}[Error]:{Style.RESET_ALL}cant get user :{e}")

    try:
        following = cl.user_following(cl.user_id)
    except Exception as e:
        print(f"{Fore.RED}[Error]:{Style.RESET_ALL}cant get followings :{e}")
    else:
        print(f"{Fore.GREEN}[Successful]:{Style.RESET_ALL}your following getted")

    dicts = {}
    for item in users:
        id = item.pk
        dicts[id] = item
    users = dicts

    for user in users.copy():
        try:
            if user in following or users[user].is_private:
                users.pop(user)
                print(f"{user} deleted from users")
        except Exception as e:
            print(f"{Fore.RED}[Error]:{Style.RESET_ALL}to delete user:{e}")

    users = list(users.values())

    try:
        with open("data/pickle/users.pkl", "wb") as f:
            pickle.dump(users, f)
    except Exception as e:
        print(f"{Fore.RED}[Error]:{Style.RESET_ALL}to save pickle:{e}")
    else:
        print(f"{Fore.GREEN}[Successful]:{Style.RESET_ALL}users.pkl saved")

table_users = PrettyTable()
table_users.field_names = ["id", "Username", "Fullname", "Private"]
for user in users:
    if user.is_private:
        status = f"{Fore.RED}Private{Style.RESET_ALL}"
    else:
        status = f"{Fore.GREEN}Public{Style.RESET_ALL}"
    table_users.add_row([user.pk, user.username, user.full_name, status])

print(table_users)
print(f"all users added :{Fore.MAGENTA}{len(users)}{Style.RESET_ALL}")

# try:
#     my_id = str(cl.user_id_from_username("gem__off"))
# except Exception as e:
#     print(f"{Fore.RED}[Error]:{Style.RESET_ALL}set my id :{e}")
# else:
#     print(f"{Fore.GREEN}[Successful]:{Style.RESET_ALL}my id seted")

comments = [
    "💐💐💐💐💐💐💐💐",
    "🌸🌸🌸🌸🌸🌸🌸🌸",
    "🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️",
    "🌹🌹🌹🌹🌹🌹🌹🌹",
    "🌺🌺🌺🌺🌺🌺🌺🌺",
    "🌻🌻🌻🌻🌻🌻🌻🌻",
    "🌼🌼🌼🌼🌼🌼🌼🌼",
    "🌷🌷🌷🌷🌷🌷🌷🌷",
    "🪻🪻🪻🪻🪻🪻🪻🪻",
    "😍😍😍😍😍😍😍😍",
    "🤩🤩🤩🤩🤩🤩🤩🤩",
    "❤️❤️❤️❤️❤️❤️❤️❤️",
    "🩷🩷🩷🩷🩷🩷🩷🩷",
    "🧡🧡🧡🧡🧡🧡🧡🧡",
    "💛💛💛💛💛💛💛💛",
    "💚💚💚💚💚💚💚💚",
    "💙💙💙💙💙💙💙💙",
    "🩵🩵🩵🩵🩵🩵🩵🩵",
    "💜💜💜💜💜💜💜💜",
    "❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥",
    "❣️❣️❣️❣️❣️❣️❣️❣️",
    "💓💓💓💓💓💓💓💓",
    "💗💗💗💗💗💗💗💗",
    "💖💖💖💖💖💖💖💖",
    "💝💝💝💝💝💝💝💝"
]

cl.delay_range = [10, 15]

for user in users.copy():
    # follow user
    # try:
    #     cl.user_follow(user.pk)  
    # except Exception as e:
    #     print(f"{Fore.RED}[Error]:{Style.RESET_ALL}to following {user.username} :{e}")
    # else:
    #     print(f"{Fore.GREEN}[Successful]:{Style.RESET_ALL}followed user {user.username}")
    #     sleep(randint(15, 30))
    # like and comment user
    user_posts = cl.user_medias(user.pk, 6)
    if user_posts != []:
        for i, post in enumerate(user_posts):
            # comment user post
            if i == 0:
                try:
                    comment = choice(comments)
                    cl.media_comment(post.pk, comment)
                except Exception as e:
                    print(f"{Fore.RED}[Error]:{Style.RESET_ALL}to commenting on post {post.pk}:{e}")
                else:
                    print(f"{Fore.GREEN}[Successful]:{Style.RESET_ALL}commented={comment} on post {post.pk}")
                    sleep(randint(60, 90))
            try:
                cl.media_like(post.pk)
            except Exception as e:
                print(f"{Fore.RED}[Error]:{Style.RESET_ALL}to liking post {post.pk}:{e}")
            else:
                print(f"{Fore.GREEN}[Successful]:{Style.RESET_ALL}post {post.pk} liked")
                sleep(randint(60, 90))
    else:
        print(f"{Fore.YELLOW}no posts found for {user.username}")
    # send direct user    
    # try:
    #     cl.direct_send(
    #         f"سلام اگه دوست داشتی به پیج اصلیم یه سر بزن👇👇",
    #         user_ids=[user.pk])      
    # except Exception as e:
    #     print(f"{Fore.RED}[Error]:{Style.RESET_ALL}to sending message :{e}")  
    # else:
    #     print(f"{Fore.GREEN}[Successful]:{Style.RESET_ALL}message sent to {user.username}")
    #     sleep(randint(60, 90))
    # send profile user    
    # try:
    #     cl.direct_profile_share(my_id, user_ids=[user.pk])  
    # except Exception as e:
    #     print(f"{Fore.RED}[Error]:{Style.RESET_ALL}to sending profile :{e}")
    # else:
    #     print(f"{Fore.GREEN}[Successful]:{Style.RESET_ALL}profile sent to {user.username}")
    #     sleep(randint(60, 90))
    # update user pikle 
    print(f"{Fore.MAGENTA}updating pickle users...{Style.RESET_ALL}")
    users.remove(user)
    with open("data/pickle/users.pkl", "wb") as f:
        pickle.dump(users, f)
    if users == []:
        os.remove("data/pickle/users.pkl")
        print(f"{Fore.RED}deleted pickle users.{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}updated pickle users.{Style.RESET_ALL}")
    print(f"The number of remaining users is :{Fore.MAGENTA}{len(users)}{Style.RESET_ALL}")

print(f"{Fore.BLUE}------------------------ all done ---------------------------{Style.RESET_ALL}")
