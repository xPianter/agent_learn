from app.tools.base import BaseTool


class DatabaseTool(BaseTool):
    """模拟数据库查询工具，数据保存在内存中。"""

    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)
#super() 让我们调用父类的方法。这里调用 BaseTool 的初始化方法，所以不必重复编写
#self.name 和 self.description。这就是继承带来的复用。


# 当前对象保存的模拟数据。变量名前面的单下划线
# _ 是一种约定，表示这是供类内部使用的属性，并非 Python 强制的访问限制。
        self._records = {#
            "1": {"name": "Alice", "role": "admin"},
            "2": {"name": "Bob", "role": "user"},
            "3": {"name": "Charlie", "role": "user"},
        }

    def run(self, query: str) -> str:
        user_id = query.strip()

        if not user_id:
            raise ValueError("请输入用户 ID")

        record = self._records.get(user_id)
        #dict.get() 会根据键获取数据。如果键不存在，默认返回 None，

        if record is None:
            raise ValueError(f"未找到用户 ID：{user_id}")

        return (
            f"用户 ID：{user_id}，"
            f"姓名：{record['name']}，"
            f"角色：{record['role']}"
        )
