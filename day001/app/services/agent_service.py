# services负责：业务逻辑是什么
# 例如：用户输入：帮我搜索Python
# 然后：判断
#  ↓
# 调用tool
#  ↓
# 生成回复

# 这些不是 Message 的职责。所以放：services/agent_service.py
# main.py负责：启动程序.类似：FastAPI：app = FastAPI(),然后调用服务。

from app.model.tool import Tool
def search():
    return "Python 是一种编程语言"


search_tool = Tool(
    "search",
    "搜索互联网",
    search
)

from app.model.message import Message
class AgentService:
    def __init__(self):
        self.tool = search_tool
    def run(self, message: Message):
        result = self.tool.function()
        return Message(
            "assistant",result
        )



