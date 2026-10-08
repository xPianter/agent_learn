#scope（作用域）最核心的概念：
# 因为不在同一个作用域，所以可以存在两个同名变量。
# 这正是 namespace 和 scope 的关系。
name = "Tom"
def test():
    name = "Jerry"
    print(name)
test()
print(name)

#结果是jerry tom,因为在函数内部定义的name变量属于函数的局部作用域，
# 而在函数外部定义的name变量属于全局作用域，所以它们是两个不同的变量，互不影响。