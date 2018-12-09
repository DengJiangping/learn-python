#range
a = range(10)
print(a)
for i in a:
	print(i)
# range(a,b,c) a 起始值，b最大值但不包括b,c步长
print('\n')
#function
def create_adder(x):
	def adder(y):
		return x + y
	return adder
add_100 = create_adder(100)
print(add_100(5))

def add(x,y):
	print("x is :{} and y is:{}".format(x,y))
	return x + y
print(add(12,45)) #正常传值
print(add(y=10,x=25)) #关键字传值
arg1 = (2,3)
print(add(*arg1)) #把xy放入一个元组
arg2 = {
	"x":20,
	"y":30
}
print(add(**arg2))
print('\n')
def diff1(*args):
	for i in args:
		print(i)
diff1(20,54,47)
arg3 = (45,48,96)
diff1(*arg3)

arg4 = {
	"x":2
}
# diff1(**arg4) 报错
def diff2(**args):
	print(args.values())
diff2(x=10,y=20)
diff2(**arg4)

#scope 在函数中改变全局变量
one = 100
def tint(num):
	global one
	print("one is: ",one)
	one = num
	print("one is: ",one)
tint(36)
#lambda
(lambda x,y:print(x + y))(10,45)
#map filter
print(list(map(add_100,[1,4,7])))
print(list(map(max,[5,4,8],[1,6,3])))
print(list(filter(lambda x:x>5,[1,4,7])))

#吊炸天的数组内部取值
a = [add_100(i) for i in range(5) if i < 3]
print(a) #[100, 101, 102]
b = {x for x in "ajkbdkajf" if x not in "abc"}
print(b)
c = {x:x**2 for x in range(3,12,4)}
print(c)