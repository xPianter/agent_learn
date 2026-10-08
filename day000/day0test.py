# 1.typing
def get_name(user_id: int) -> str|None:#user_id的类型是int，返回值的类型是str或者None
    if user_id == 1:
        return "tom"  
    return None 

# 2. dataclass
from dataclasses import dataclass #python的内置模块，提供了一个装饰器和函数，用于自动为类生成特殊方法     

@dataclass   #使用方法
class User:
    name: str
    age: int

user = User("Tom", 20)#调用

# 刚才的 typing 和 dataclass 结合起来。
@dataclass
class User:
    id: int
    name: str
    email: str|None
    age: int|None

# exception异常
#异常体系
# Exception
# ├── ValueError 值错误
# ├── TypeError 类型错误
# ├── KeyError 键错误
# └── IndexError 索引错误 

#所以使用try except语句来捕获异常
try:
    age = int("abc")
except ValueError:
    print("转换失败")

def parse_age(age: str) -> int | None:
    try:
        return int(age)
    except ValueError:
        return None


#Package 封装
# Module 和 Package 的区别

# 这个一定要分清：
# module
#     ↓
# 通常就是一个 .py 文件
# package
#     ↓
# 通常就是一个 Python 包目录

# 为什么需要 __init__.py？
#_init__.py 是 package 的初始化模块它可以让目录成为传统意义上的 Python package,
# 并且可以在 package 被导入时执行初始化代码。
#但是现在 Python 支持 namespace package，所以某些情况下即使没有 __init__.py，
# 目录也可以被当作 package 使用所以不要死记：没有 __init__.py 就绝对不是 package。

# 传统 Python package 通常通过：
# __init__.py
# 告诉 Python：
# 这个目录可以作为一个 Python package 来使用。

# 例如：
# app/
# ├── __init__.py
# └── user.py

# 然后其他地方可以：
# from app.user import User


# 综合题

# 你现在不要看前面的答案，自己完成：

from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    age: int | None


# def parse_age(age: str) -> int | None:
#     ...

# 要求：
# User 用 dataclass
# id 是 int
# name 是 str
# age 可以是 int 或 None
# parse_age 接收 str
# 成功转换返回 int
# 转换失败捕获 ValueError，返回 None
# 你把完整代码自己写出来。
def parse_age(age: str) -> int | None:
     try:
         return int(age)
     except ValueError:
         return None     