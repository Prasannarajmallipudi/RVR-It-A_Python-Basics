def re(s):
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                print(s[0:j]+"@"+s[j+1:])
s=input("enter string: ")
re(s)
