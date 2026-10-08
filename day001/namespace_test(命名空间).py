#namespace 是存放“名字 → 对象”的地方。
#globals() 是 Python 内置函数，用于返回当前模块的全局命名空间字典。
# 字典的键是变量名，值是对应对象，修改该字典可直接影响全局变量。‌‌

#globals() 始终返回模块级全局变量；locals() 返回当前局部作用域，
# 且修改函数内返回的 locals() 字典通常不影响实际局部变量

name = "Tom"
print(name)
print(globals())