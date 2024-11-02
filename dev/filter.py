import pickle

try:
    with open("users.pkl", "rb") as f:
        users = pickle.load(f)
        print("users loaded from pickle")
except Exception as e:
    print(f"Error to load pickle:{e}")

try:
    with open("followings.pkl", "rb") as f:
        followings = pickle.load(f)
        print("followings loaded from pickle")
except Exception as e:
    print(f"Error to load pickle:{e}")

dicts = {}
for item in users:
    id = item.pk
    dicts[id] = item
users = dicts

for user in users.copy():
    try:
        if user in followings or users[user].is_private:
            users.pop(user)
            print(f"{user} deleted from users")
    except Exception as e:
        print(f"Error to delete user:{e}")

users = list(users.values())

try:
    with open("users.pkl", "wb") as f:
        pickle.dump(users, f)
        print("users.pkl saved")
except Exception as e:
    print(f"Error to save pickle:{e}")

print(f"all {len(users)} users saved!")
