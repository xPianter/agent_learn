#每一条消息其实都有几个基本信息：
# 谁发送的（role）
# 内容是什么（content）
# 消息编号或者时间（可选）

class Message:
    def __init__(self,role:str,content:str):
        self.role = role
        self.content = content
    

# message = Message("user","你好")



