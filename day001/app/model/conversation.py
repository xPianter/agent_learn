class Conversation:
    def __init__(self):
        self.messages = []

    def add_message(self,message:str):
            self.messages.append(message)

# 为什么要把messages.append封装在conversation的add_message方法中？
# 这就是面向对象思想：
# 对象
#  |
#  ├── 数据
#  |
#  └── 操作数据的方法
# 例如：

# Conversation：
# Conversation对象
#   数据:
#       messages
#   方法:
#       add_message()

    def get_messages(self):
        # return self.messages #直接返回原始列表，外部可以直接修改它
        return self.messages.copy()  # 返回一个副本，避免外部直接修改原始列表


 



