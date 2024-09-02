import os

print("hello, lets check your connection by pinging")

os.system("ping 10.20.10.10 > ping_google.txt")
with open("ping_google.txt", "r") as pingfile:
    content = pingfile.read()
    if "TTL" in content:
        print("you have internet connection")
    elif "Request timed out." in content:
        print("time out, problem with internet")
    elif "unreachable" in content:
        print("the target is unreachable")

