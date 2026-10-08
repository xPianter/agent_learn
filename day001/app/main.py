# from app.model.user import User

# user = User(1,"Tom")
# print(user.user_id)

# # User(1, "Tom")是什么？
# # ✅ 一个新的 User对象

# # user是什么？
# # 不是对象本身。更准确：
# # ✅ 一个指向 User 对象的引用（reference）

# from app.model.message import Message

# message = Message("user","你好")
# # print(message.role)
# # print(message.content)

# message2 = Message("assistant", "你好，我是AI助手")
# # print(message2.role)
# # print(message2.content)

# from app.model.conversation import Conversation
# conversation = Conversation()
# conversation.get_messages().append(message)#封装前
# # print(conversation.messages)
# conversation.add_message(message2)#封装后

# for message in conversation.messages:
#     print(message.role, message.content)


# from app.model.tool import Tool

# #为什么不把search函数写在Tool类里面？
# #因为Tool类是一个通用的工具类，里面不应该包含具体的功能实现。
# #具体的功能实现应该由具体的函数来完成，这样Agent可以动态注册工具。
# def search():
#     return "搜索结果"


# tool = Tool("search", "搜索互联网", search)
# print(tool.name)
# print(tool.description)
# print(tool.function())


from app.model.message import Message
from app.model.conversation import Conversation
from app.services.agent_service import AgentService
conversation = Conversation()

message = Message(
    "user",
    "帮我搜索 Python"
)

conversation.add_message(message)

agent = AgentService()

response = agent.run(message)#调用conversation.add_message(response)

conversation.add_message(response)

for message in conversation.messages:
    print(
        message.role,
        message.content
    )







    

