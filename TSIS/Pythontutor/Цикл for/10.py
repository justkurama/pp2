#Лесенка
a = int(input())
for i in range(1, a+1):
    for s in range(1, i+1):
        print(s, end="")
    print(end="\n")