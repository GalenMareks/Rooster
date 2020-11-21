import requests

addr = input("Target Website (example: example.com): ")

def kev():
    wordlist = open("wordlist.txt","r")
    att = wordlist.readlines()  
    for i in att:
        r = requests.get("http://"+addr+"/"+i)
        if r.status_code == 200:
            print("Gotcha we find it. http://"+addr+"/"+i)
        else:
            print("Not this one")

kev()



