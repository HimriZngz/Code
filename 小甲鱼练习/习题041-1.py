# 1. 按照以下要求，定义一个类实现摄氏度到华氏度的转换（转换公式：华氏度 = 摄氏度*1.8+32）


class C2F:
    def __new__(cls, c):
        c = c * 1.8 + 32
        return c


print(C2F(32))


"""
参考答案：

class C2F(float):
        "摄氏度转换为华氏度"
        def __new__(cls, arg=0.0):
                return float.__new__(cls, arg * 1.8 + 32)


"""