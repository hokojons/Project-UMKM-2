username = "steven"
password = "opo"
level = ["kasir","owner","manager","rampok"]
username= input("username: ")
password= input("password: ")
level = input("level: ")

if username == "steven" and password == "opo":
    if level == "kasir":
        print("akses di tolak ")
    elif level == "manager":
        print("akses di tolak ")
    elif level == "owner":
        print("akses di tolak ")
    elif level == "maling":
        print("selamat akses di trima ")
else:
    print("akses di tolak")