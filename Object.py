class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


A = Dog("A", 5)
B = Dog("B", 6)


print(A.age)

import urllib.request


def internet_connection():
    try:
        urllib.request.urlopen('www.google.com')
        return True
    except:
        return False


print("Internet Status: Connected"if internet_connection() else "Internet Status: Not Connected")

def connection():
    try:
        urllib.request.urlopen('www.google.com')
        return True
    except:
        return False

print("Internet Status: Connected" if connection() else "Internet Status: Not Connected")

import netifaces as ni

#ip = ni.ifaddresses('enp0s25')[ni.AF_INET][0]['addr']
#print (ip)

if ni.ifaddresses('enp0s25')[ni.AF_INET][0]['addr'] == TypeError:
    print (ni.ifaddresses('wlp3s0')[ni.AF_INET][0]['addr'])

else:
    print (ni.ifaddresses('enp0s25')[ni.AF_INET][0]['addr'])

