#1.class 类
#定义一个简单 的 SearchTool 类，包含一个 run 方法，用于模拟搜索功能。
class SearchTool:
    def __init__(self, name: str):
        self.name = name

    def run(self, query: str) -> str:
        return f"正在搜索：{query}"

#2.inheritance：继承:让子类复用父类的行为
#先定义一个基础的 Tool 类，包含 name 和 description 属性，以及一个 run 方法。
class BaseTool:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def run(self, query: str) -> str:
        raise NotImplementedError("子类需要实现 run()")

#然后让搜索工具继承它
class SearchTool(BaseTool):
      def run(self, query: str) -> str:
        return f"正在搜索：{query}"

#如果搜索工具、计算器工具和数据库工具都需要统一的 name、
#description 和 run() 方法，就可以考虑使用继承。

#注意，父类中的 run() 只是约定或占位实现时，子类需要重写它，才能实现自己的业务逻辑。


#3.composition：组合:让类之间的关系更灵活
#继承解决的是“属于什么类型”的关系；组合解决的是“由什么组成”或“使用什么”的关系。

#例如，一个 Agent 使用多个工具：
class Agent:
    def __init__(self, tools: list[BaseTool]):
        self.tools = tools

    def list_tools(self) -> list[str]:   # 列出所有工具的名称
        return [tool.name for tool in self.tools]

#在使用时
tools = [
    SearchTool("search", "搜索信息"),
]

agent = Agent(tools)
print(agent.list_tools())
#Agent 不需要继承 SearchTool。它只需要持有工具列表，就可以管理多个工具。
#这正是 AI Agent 工程里很重要的设计思路：Agent 负责协调，Tool 负责执行。


#4.abstraction：抽象，隐藏不必要的实现细节
# 调用者通常只关心：
# 这个工具叫什么？
# 它能做什么？
# 我应该如何调用它？
# 执行失败时会发生什么？
# 调用者不一定需要了解搜索工具如何请求网页，或者数据库工具如何执行 SQL。


# 我们把  共同规则  放在 BaseTool 中，把不同工具的具体实现留给各自的子类。
# 这就是抽象的核心：统一使用方式，允许内部实现不同.

#5.interface thinking：接口思维
# Python 不要求所有工具必须继承同一个父类才能被使用。只要对象具有调用方需要的方法，调用方就可以使用它——这也与 Python 的鸭子类型思想有关。

# 例如，未来可以有一个工具只实现：
class CustomTool:
    name = "custom"
    def run(self, query: str) -> str:
        return f"处理结果：{query}"
# 即使它没有继承 BaseTool，某些只调用 run() 的代码仍然可以使用它。



#
