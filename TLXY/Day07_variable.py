# ****** 变量的作用域 ******
# 分为 全局变量 and 局部变量
a = 1                   # 函数外部定义的变量叫全局变量
def fun1():
    b = 2               # 函数内部定义的变量叫局部变量
    print(b)
    print(a)            # a是全局变量,所以在fun1中能够引用它

print(a)
#fun1(b)                # b是局部变量,所以在函数外部无法引用

print('*' * 80)

# ****** eval函数 ******
# 把字符串当做表达式来执行
# exec具有相同功能,但是没有返回值
x = 1
y = 1
z = eval('x+y')
print(z)

print('*' * 80)

# ****** 递归函数 ******
# 函数直接或间接调用自己
# 递归深度有限制
x = 0
def fun2():
    global x
    x += 1
    print(x)
    fun2()
#fun2()

print('*' * 80)

# ****** 斐波那契数列 ******
# 数列特点:第1位数为1,第二位数为1,从第3位数开始每个数的值都是前面两数之和
# 1,1,2,3,5,8......
# 表达式:f(1)=1,f(2)=2,f(n)=f(n-1)+f(n-2)
def fib(n):
    if n == 1:
        return 1
    if n ==2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(10))

w = "hihi"
#ceshi 