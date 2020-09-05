import httplib
import socket

# Import website urls from file
with open('websiteList.txt') as f:
    lines = [line.rstrip() for line in f]

index = 0
errors = []

for i in lines:
    try:
       conn = httplib.HTTPSConnection(lines[index])
       conn.request("HEAD", "/")
       conResult = conn.getresponse()
    except (httplib.HTTPException, socket.error) as ex:
       print " "
    if r1.status < 400:
        print(lines[index] + " IS ONLINE")
        index = index + 1
    else:
        print lines[index] + " IS OFFLINE"
        errors.append(lines[index] + " IS OFFLINE. ERROR: " + str(r1.status))
        index = index + 1

print(" ")
print("-------------------------------")
print(" ")
print(str(len(lines) - len(errors))+" LIVE")
print(str(len(errors))+" DOWN")
print(" ")

index = 0
for i in errors:
    print(errors[index])
    index = index + 1
