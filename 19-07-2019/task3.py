"""# input : abc123
# Output : 6
x=0
s=input("enter a string:")
for i in s:
    if i.isdigit():
        x += int(i)
print(x) """
s=input("enter a string:")
s=s.split()
sum=0
for i in s:
    if (i.isdigit()):
        sum+=int(i)
print(sum)
