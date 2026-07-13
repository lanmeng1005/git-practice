"""
Git 练习项目 - 示例代码
"""

def greet(name):
    """打招呼函数"""
    return f"你好，{name}！欢迎来到 Git 的世界。"

def add(a, b):
    """加法函数"""
    return a + b

def multiply(a, b):
    """乘法函数"""
    return a * b

def subtract(a, b):
    """减法函数"""
    return a - b

if __name__ == "__main__":
    print(greet("蓝梦"))
    print(f"1 + 2 = {add(1, 2)}")
    print(f"3 × 4 = {multiply(3, 4)}")
    print(f"10 - 3 = {subtract(10, 3)}")