# ****** 字典遍历 ******
a = {'name':"liyihang", 'age':18, 'addr':'HuNan'}
for k,v in a.items():
    print(k, '---', v)

print('*' * 80)

# ****** 普通参数 ******
def introduction(name, age, hobby):
    print('Hello')
    print("my name is {0}, i'm {1} years old, my hobby is {2}.".format(name, age, hobby))

introduction('liyihang', 25, 'music')

print('*' * 80)

# ****** 关键字参数 ******
# 普通参数在调用时可能会因为位置顺序错误而导致调用错误,例如:
introduction(18, 'liyihang', 'music')

# 所以使用关键字参数更为准确
def introduction_key(name='None', age=0, hobby='None'):
    print('Hello')
    print("my name is {0}, i'm {1} years old, my hobby is {2}.".format(name, age, hobby))

introduction_key(name='liyihang', age=25, hobby='music')
#随意打乱调用顺序,调用值不受影响
introduction_key(hobby='music', name='liyihang', age=25)

print('*' * 80)

# ****** 收集参数 ******
# 收集参数的使用场景一般是在你不知道将来函数会传入多少个参数的情况下使用
# 例如,自我介绍,没有限制你介绍的任何内容,你可以介绍你的姓名年龄或者更多,甚至可以什么都不说
# 收集参数传入后会打包成tuple类型,所以用for循环遍历其中的值
def intro(*args):
    print('Hello')
    for i in args:
        print(i)
intro('liyihang', 25, 'music')

print('*' * 80)

# 关于函数参数的解包问题
# 首先定义了一个tuple,然后将其传入intro函数,此时intro为收集函数,参数传入后会打包成tuple
# 但我现在在调用时直接就传入了一个tuple,所以python就把这个tuple当成了一个值传入了函数
# 这种情况下,我们需要先解包然后再传入函数,解包在调用函数的实参前加上一个*
l = ('liyihang', 25, 'music')
intro(*l)

print('*' * 80)

# 字典解包在实参前加两个星号

# ****** 关键字收集参数 ******
# 上面说收集参数会打包成tuple类型,而关键字收集参数则会打包成dict类型
# 关键字收集参数使用**kwargs定义
def fun1(**kwargs):
    print('Hello')
    for k,v in kwargs.items():           #字典遍历!!!!!
        print(k, ':', v)

fun1(name='liyihang', age=18, hobby='music')

print('*' * 80)

# ****** 函数参数总结:各种参数混合调用! ******
# 定义一个自我介绍的函数,参数包含普通参数,关键字参数,收集参数,关键字收集参数
# 然后调用它
# 注意:定义包含多种参数类型的函数时,参数定义的顺序依次是
#      普通参数,收集参数,关键字参数,关键字收集参数
# 总之就是一个原则,普通在一块儿,关键字在一块儿
def fun2(name, age,*args, hobby='music', **kwargs):
    print("Hello,my name is {0}, i'm {1} years old".format(name, age))
    if hobby == 'None':                     # 判断关键字参数hobby
        print('i have no hobby')
    else:
        print('my hobby is {0}'.format(hobby))

    for i in args:                          # 遍历收集参数
        print(i)

    for k,v in kwargs.items():              # 遍历关键字收集参数
        print(k, ':', v)

fun2('liyihang', 25, 'hahahahah', grilfriend='liuyifei')

print('*' * 80)

# ****** 函数的返回值 ******
# 函数不管有没有返回值,推荐写法都以return结尾
# return后面有值则函数有返回值,return后面没有值,则函数的返回值为none
def fun3(name):
    print(name)
    return name
fun3('liyihang')

print('*' * 80)

# ****** 函数的文档注释 ******
# 函数的文档注释推荐用三引号来写
def fun4(name, age, hobby):
    '''
    这是一个自我介绍的函数,打印name,age,hobby三种个人属性
    :param name: 姓名
    :param age: 年龄
    :param hobby: 爱好
    :return: name, age, hobby
    '''
    print(name, age, hobby)
    return name, age, hobby
fun4('liyihang', 25, 'music')
help(fun4)


# PS:
# 注意遍历字典的方法的使用
# 注意函数参数的返回值
# 注意收集参数以及关键字参数传入后会打包成tuple以及dict类型
# 注意收集参数在传入tuple以及dict类型时,需要先解包再传入使用


