import webbrowser
import time
breakcount = 4
count = 0
print(time.ctime())

while count<=breakcount:
    time.sleep(10)
    if count == 1:
        webbrowser.open("www.google.com")
    elif count==2:
        webbrowser.open("www.facebook.com")
    elif count==3:
        webbrowser.open("www.w3schhols.com")
    elif count==4:
        webbrowser.open("www.apssdc.in")
    count+=1
    
