from app.tools.base import BaseTool


class CalculatorTool(BaseTool):
    """计算两个数字的和。"""

    def run(self, query: str) -> str:
        parts = query.split()

        if len(parts) != 2:
            raise ValueError("请输入两个数字，例如：3 5")

        try:
            left = float(parts[0])
            right = float(parts[1])
        except ValueError as exc:
            raise ValueError("输入必须是有效数字") from exc

        return str(left + right)


# from app.tools.base import BaseTool
# class calculator(BaseTool):
#     def run(self,query:str)->str:
#         parts = query.split()
#         if len(parts) != 2:
#             raise ValueError('请输入正确的数字,例如“3 5”')
#         try:
#             left = float(parts[0])
#             right = float(parts[1])
#         except ValueError as exc:
#             raise  ValueError('请输入正确的数字类型 ') from exc
#         else:
#             return str(left + right)
