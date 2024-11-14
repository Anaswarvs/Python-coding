pronic_lst=[]
for n in range(1,101):
    pronic=n*(n+1)
    if pronic<=100:
        pronic_lst.append(pronic)
print(pronic_lst)