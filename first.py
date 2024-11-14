nums=[1,2,3,4,5,2,7,8,9,0,4]
lst=[]
val=2
for i in nums:
    if i!=val:
        lst.append(i)
print(len(lst))