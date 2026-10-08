from dataclasses import dataclass#从 Python 内置的 dataclasses 模块中导入 dataclass。
#下面这个类主要用于保存数据，帮我自动生成一些常用代码。
@dataclass
class User:#定义一个 User 数据类型。
    id:int
    name:str
    age:int|None    

user=User(1,"tom",20)
print(user)

def parse_age(age:str) ->int|None:
    try:
        return int(age)
    except ValueError:
        return None

print(parse_age("20"))
print(parse_age("abc"))
