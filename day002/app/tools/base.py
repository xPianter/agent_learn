from abc import ABC, abstractmethod


class BaseTool(ABC):
    """让basetool所有工具的抽象基类。"""

    def __init__(self, name: str, description: str) -> None:#init不返回一个值，返回None,主要是初始化对象的属性
        self.name = name
        self.description = description

    @abstractmethod#声明run方法为抽象方法，子类必须实现它
    def run(self, query: str) -> str:
        """执行工具任务，由子类实现。"""
        raise NotImplementedError#主动抛出一个 NotImplementedError 异常，
                                 #告诉程序和开发者：“这个功能还没有实现。
    #NotImplementedError,Python 内置异常类型，通常用于表示某个功能尚未实现


#@abstractmethod：入口处的约束,不允许不完整的子类被正常实例化。
#raise NotImplementedError：执行时的保护,如果执行到了尚未实现的方法，就抛出异常。
