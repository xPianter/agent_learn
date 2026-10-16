#括号匹配的算法题
def is_valid(s: str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for a in s :
        if a in '[{(':
            stack.append(a)
        elif a in ']})' :
            if not stack:
                return False
            elif stack[-1] == pairs[a]:
                stack.pop()
            else:
                return False

    return not stack




cases = {
    "()": True,
    "()[]{}": True,
    "(]": False,
    "([)]": False,
    "{[]}": True,
    "(": False,
    "]": False,
}

for s, expected in cases.items():
    actual = is_valid(s)
    assert actual == expected, (
        f"输入：{s!r}，预期：{expected}，实际：{actual}"
    )
    print(f"通过：{s!r} -> {actual}")

print("全部示例通过！")
