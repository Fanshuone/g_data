import sys


# 创建自定义的输出类
class DummyOutput:
    def write(self, text):
        pass


def no_printf(func):
    def inner():
        # 将标准输出重定向到 DummyOutput 实例
        sys.stdout = DummyOutput()
        func()
        sys.stdout = sys.__stdout__

    return inner


if __name__ == '__main__':
    @no_printf
    def printf():
        print("afds")
