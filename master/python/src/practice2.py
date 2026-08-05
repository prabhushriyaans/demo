lst1=[1,2,3,4,5,6,7,8,9]
print(lst1[1:3])
lst1.append(10)
lst1.extend([11,12,13])
lst1.insert(3,0)
lst1.remove(9)
lst1.pop()
print(lst1)
id=lst1.index(4)
print(id)
lst1.sort()
print(lst1)
lst1.reverse()
print(lst1)
if lst1.sort() == lst1.reverse():
    print("True")
lst1.clear()
print(lst1)
del lst1

name="malayalam"
nml=list(name)
print(nml)
if name==name[::-1]:
    print("pallindrome")


# tuples
t=(1,2,3,4,5,6)
print(t[0])
t.count(3)
t.index(4)//3
u=(7,8,9)
print(t+u)
# sets
s1={1,2,0,3,4,5}
s2={3,4,6,7,8,9}
s3=s1.union(s2)
s4=s1.intersection(s2)
s5=s1.difference(s2)
print(s3)
print(s4)
print(s5)
print(s4.issubset(s1))
print(s2.issuperset(s4))
ls3=list(s3)
print(ls3)
nmlst=[[0,"user1"],[1,"user2"],[2,"user3"]]
print(nmlst)
nmlst=dict(nmlst)
print(nmlst)