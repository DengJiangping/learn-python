# True == 1 False == 0
print(True + 1) #the value is 2
# bool ->bool(a) == False => a = "" () {} [] 0 None
print(bool('')) #an eg
# format
print("This is knowledge about format!") #one
print("a is {},b is {}".format(2,"String")) #two
print("she likes {0},but he likes {1},and parents like {0}" #three
	.format("apple","orange"))
a = "Her name is {name}".format(name="Lily") #four
print(a)
# s% d% f
print('it is %d years age,%s...'%(3,"that"))
name = 'aaaa'
print(f"what is {name}")
# is and ==
list1 = [1,2,3,4]
list2 = list1
print("This is about is and == operate: ")
print(list2 == list1) #is checks if two variables' object whether the same
print(list1 is list2) #== checks if values are the same
list2 = [1,2,3,4]
print(list2 is list1)
print(list2 == list1)
# None
# if
print("'Hello'" if 3 > 2 else 2)
print('\n')
# []{}()
print("Below is about Sequence!")

#list 切片 
aList = [1,2,3,5]
c1 = aList[1:]
c2 = aList[:3]
c3 = aList[1:3]
c4 = aList[::] #copy aList
c5 = aList[:-1]
c6 = aList[::2] #步长为2
c7 = aList[::-1] #反向复制list
# c6 = aList[::]
print("c1:{},c2:{},c3:{},c4:{},c5:{}".format(c1,c2,c3,c4,c5))
#c1:[2, 3, 5],c2:[1, 2, 3],c3:[2, 3],c4:[1, 2, 3, 5],c5:[1, 2, 3]
print(aList)

#list 函数方法 will change list
bList = ["str",2,5,7,8]
bList.remove("str")
bList.append("end")
print("bList is :",bList)
cList = ["a","b","c"]
cList.pop()
print("cList is :",cList)
bList.extend(cList)
print("bList is :",bList)

# bList.index(7)
# bList.insert(1,3)

#tuple ()
q,w,e = (1,2,3) # q=1,w=2,c=3
# q,w,e = 3,2,1
t = ("s","b")
length1 = len(t)
length2 = len(bList)
print("t's len is {} and bList's len is {}".format(length1,length2))
print('\n')
#dictionary {} .values()/.keys()/.get/.setDefault()
d = {
	"name":'djp',
	"age":18,
	"grade":3
}
d["name"]  #djp
v = d.values()
k = d.keys()
print("d's values are {} type {} ,d's keys are {} type {}"
	.format(v,type(v),k,type(k)))

# a = input("your input is: ")
# print("a is ",a)
print('\n')
#iterable
for i in k:  #第一种
    print(i)
ite_d = iter(k)
print(next(ite_d))

print(list(k)) #third method
#对list、tuple,dict的补充
p = (1)
type(p) #int
p = (1,)
type(p) #tuple

l = [7,9,0]
l.index(0) #2
l.insert(1,3) #7,3,9,0
del l[2] #此处2为索引，即删除第三个数

dd = {
	"one":1,
	"two":2,
	"three":3
}
# dd["four"] #报错
dd.get("four") #不会报错
dd.setdefault("four",4)#dd{'one': 1, 'two': 2, 'three': 3, 'four': 5}
del dd["one"] #删除one


#modules
# from math import ceil
# dir(math)
#this line is just for test git