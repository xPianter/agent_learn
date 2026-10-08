from app.model.user import User
from app.model.conversation import Conversation
from app.model.tool import Tool
from app.model.message import Message

user = User(1,"user")
conversation = Conversation()
message = Message("user","帮我搜索 Python")
conversation.add_message(message)
def search():
    return "Python 是一种编程语言"
tool = Tool("search", "搜索互联网", search)

result = tool.function()

message2 = Message("assistant", result)

conversation.add_message(message2)

for message in conversation.messages: #输出验证
    print(message.role, message.content)


