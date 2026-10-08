# 例如：
# Tool:
#     name = "search"
#     description = "搜索互联网"
#     function = search()

# 未来 Agent：
# 用户问题
#  ↓
# Agent判断
#  ↓
# 调用Tool
#  ↓
# 返回结果

class Tool:
    def __init__(
        self,
        name: str,
        description: str,
        function
    ):
        self.name = name
        self.description = description
        self.function = function
    

