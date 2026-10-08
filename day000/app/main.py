from app.models.user import User
from app.services.user_service import create_user, parse_age


# def main():
#     age = parse_age("20")

#     user = User(
#         id=1,
#         name="Tom",
#         age=age,
#     )

#     print(user)

def main():
    use1 = create_user(1, "Tom", "20")
    use2 = create_user(2, "Jerry", "abc")

    print(use1)
    print(use2)


if __name__ == "__main__":
    main()

# 你现在这个项目已经体现了一个真正后端项目的雏形
# 
# agent_day1test2/
# │
# ├── .venv/                 # 虚拟环境
# │
# ├── app/                   # 应用代码
# │   ├── __init__.py
# │   ├── main.py            # 程序入口
# │   │
# │   ├── models/            # 数据模型
# │   │   ├── __init__.py
# │   │   └── user.py
# │   │
# │   └── services/          # 业务逻辑
# │       ├── __init__.py
# │       └── user_service.py
# │
# ├── src/                   # 之前的练习代码
# │   └── agent_day1test2/
# │       └── user.py
# │
# ├── pyproject.toml
# └── README.md

# 这里其实已经开始接近你以后写 FastAPI / AI Agent 后端时的项目组织方式了。