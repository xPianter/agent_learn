
import unittest

from app.agent import Agent
from app.tools.base import BaseTool
from app.tools.search import SearchTool
from app.tools.calculator import CalculatorTool
from app.tools.database import DatabaseTool


class TestBaseTool(unittest.TestCase):
    def test_abstract_base_tool_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            BaseTool("base", "基础工具")


class TestSearchTool(unittest.TestCase):
    def setUp(self):
        self.tool = SearchTool("search", "搜索信息")

    def test_valid_query(self):
        self.assertEqual(
            self.tool.run("Python OOP"),
            "正在搜索：Python OOP",
        )

    def test_empty_query(self):
        with self.assertRaises(ValueError):
            self.tool.run("   ")


class TestCalculatorTool(unittest.TestCase):
    def setUp(self):
        self.tool = CalculatorTool("calculator", "计算两个数字的和")

    def test_valid_addition(self):
        self.assertEqual(self.tool.run("3 5"), "8.0")
        self.assertEqual(self.tool.run("-3 5"), "2.0")

    def test_invalid_number_count(self):
        for query in ["3", "3 5 7", ""]:
            with self.subTest(query=query):
                with self.assertRaises(ValueError):
                    self.tool.run(query)

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            self.tool.run("abc 5")

    def test_zero(self):
            self.assertEqual(self.tool.run("0 0"),"0.0")

    def test_extra_whitespace(self):
            self.assertEqual(
                self.tool.run("  3   5  "),
                "8.0",
            )


class TestDatabaseTool(unittest.TestCase):
    def setUp(self):
        self.tool = DatabaseTool("database", "查询用户信息")

    def test_existing_user(self):
        result = self.tool.run("1")
        self.assertIn("Alice", result)
        self.assertIn("admin", result)

    def test_empty_user_id(self):
        with self.assertRaises(ValueError):
            self.tool.run("   ")

    def test_missing_user(self):
        with self.assertRaises(ValueError):
            self.tool.run("999")



class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = Agent([
            SearchTool("search", "搜索信息"),
            CalculatorTool("calculator", "计算两个数字的和"),
            DatabaseTool("database", "查询用户信息"),
        ])

    def test_list_tools(self):
        self.assertEqual(
            self.agent.list_tools(),
            ["search", "calculator", "database"],
        )

    def test_run_tool(self):
        self.assertEqual(
            self.agent.run_tool("calculator", "3 5"),
            "8.0",
        )

    def test_unknown_tool(self):
        with self.assertRaises(ValueError):
            self.agent.run_tool("weather", "today")

    def test_duplicate_tool_name(self):
        with self.assertRaises(ValueError):
            Agent([
                SearchTool("search", "搜索信息"),
                CalculatorTool("search", "计算数字"),
            ])


if __name__ == "__main__":
    unittest.main()
