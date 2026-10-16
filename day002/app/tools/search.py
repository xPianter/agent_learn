from app.tools.base import BaseTool

class SearchTool(BaseTool):
    """模拟搜索工具。"""

    def run(self, query: str) -> str:#重写父类的抽象方法，实现搜索功能
        if not query.strip():#如果查询字符串为空或只包含空白字符，则抛出一个 ValueError 异常，提示搜索内容不能为空。
#strip() 会移除字符串首尾的空白字符。因此，空字符串 "" 和只包含空格的字符串 "   " 都会被识别为空输入。
            raise ValueError("搜索内容不能为空")

        return f"正在搜索：{query}"
