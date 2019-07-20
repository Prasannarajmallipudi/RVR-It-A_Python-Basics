def file_create():
    f=open("sample.txt","w")
    fh="hello 3rd It from RVRJC"
    f.write(fh)
    print("Write Data Sucessfully")
    f.close()
#file_create()

def file_read():
    f=open("sample.txt","r")
    s=f.read()
    print(s)
    f.close()
#file_read()

def file_append():
    f=open("sample.txt","a")
    fh=input("enter data:")
    f.write("\n"+fh)
    print("Data append sucessfully")
    f.close()
#file_append()

def file_with_open():
    with open("browser.py") as f:
        print(f.read())
file_with_open()
        




















    
