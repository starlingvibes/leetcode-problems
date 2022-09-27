# def concatenatedBinary(n):
#     res = ""
#     for i in range(1, n + 1):
#         res += bin(i)
#     out = []
#     for i in res:
#         if i == "b":
#             out.pop()
#             continue
#         out.append(i)
#     out = "".join(out)
#     return (int(out, 2)) % ((10**9) + 7)


# print(concatenatedBinary(5))

"""
API - Register, Login, Logout

request => action username password
eg: "login chidera chidera"

On register:
    If already registered:
        print("User already exists")
    else:
        print("Registered successfully")

On Login:
    If loggedIn:
        print("Already logged in")
    If not loggedIn & user exists:
        print("Logged In Successfully")
        If not exists:
            print("Login Unsuccessful")

On Logout:
    If LoggedIn:
        print("Logged out Successfully")
    else:
        print("Log out unsuccesful")
"""


# def auth_api(req):
#     users = {}
#     res = []
#     for cmd in req:
#         string = cmd.split(" ")
#     if len(string) <= 1:
#         return "Invalid action"
#     if len(string) >= 2:
#         action = string[0]
#         username = string[1]
#         password = "" if len(string) == 2 else string[2]

#     # registering a user
#     def register(username, password):
#         if username in users:
#             res.append("User already exists")
#         else:
#             users[username] = password
#             print(users)
#             res.append("User registered successfully")

#     # logging in
#     def login(username, password):
#         isLoggedIn = False
#         if isLoggedIn:
#             res.append("User already logged in")
#         else:
#             print(users, password)
#             if users[username] == password:
#                 isLoggedIn = True
#                 res.append("Logged in successfully")
#             else:
#                 res.append("Log in unsuccessful")

#     # logging out
#     def logout(username):
#         isLoggedOut = False
#         if isLoggedOut:
#             res.append("Log out unsuccessful")
#         else:
#             isLoggedOut = True
#             res.append("Logged out successfully")

# Calling relevant functions
# if action == "register":
#     return register(username, password)
# elif action == "login":
#     return login(username, password)
# elif action == "logout":
#     return logout(username)
# else:
#     return

#     register(username, password)
#     register(username, password)
#     login(username, password)
#     # print(users)
#     return res


# print(auth_api(["register chidera password",
#       "register chidera pwd", "login chidera king"]))
from collections import defaultdict


def equationsPossible(equations):
    hashmap = defaultdict(bool)
    for i in range(len(equations)):
        if equations[i][1] == "=":
            if (equations[i][0], equations[i][3]) in hashmap and hashmap[(equations[i][0], equations[i][3])] == False:
                return False
            hashmap[(equations[i][0]), (equations[i][3])] = True
            hashmap[(equations[i][3]), (equations[i][0])] = True
        else:
            if (equations[i][0], equations[i][3]) in hashmap and hashmap[(equations[i][0], equations[i][3])] == True:
                return False
            hashmap[(equations[i][0]), (equations[i][3])] = False
            hashmap[(equations[i][3]), (equations[i][0])] = False
    return True


print(equationsPossible(["c==c", "b==d", "x!=z"]))
print(equationsPossible(["a==b", "b!=a"]))
print(equationsPossible(["a==b", "b==a"]))
