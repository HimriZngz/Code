import time as t

class Mytime:
    def __init__(self):
        self.unit = ['年','月','天','小时','分钟','秒']
        self.lasted = []
        self.prompt = '还没有开始计时'
        self.begin = 0
        self.end = 0

    def __str__(self):
        """print(实例对象)的时候会打印这个字段，直接 实例对象 则返回该对象所在的内存位置"""
        return self.prompt

    def __repr__(self):
        """直接 实例对象 ‘或者 print(实例对象) 都’ 返回这个字段;
        也可以用 __repr__ = __str__ 达成使两个def完全等同的效果"""
        return self.prompt

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = '--- 已经开始计时，现在应该stop ---'
        print('开始计时')

    # 停止计时
    def stop(self):
        if not self.begin:
            print('--- 还没有开始计时，现在应该start ---')
        else:
            self.end = t.localtime()
            self._calc()
            print('停止计时')

    # 计算时间差，用 _内部方法
    def _calc(self):
        self.lasted = []
        self.prompt = '共运行'
        for i in range(6):
            self.lasted.append(self.end[i] - self.begin[i])    # 得到结束时间-开始时间所对应的时间元祖的差值
            if self.lasted[i]:   # 如果对应的是False(即对应的值是0)，则不进入以下语句;在有时间的情况下，该数肯定不为0
                self.prompt += (str(self.lasted[i]) + self.unit[i])
        self.begin = 0
        self.end = 0

    # 计算两个时间相加
    def __add__(self, other):
        prompt = '一共运行了'
        result = []
        for i in range(6):
            result.append(self.lasted[i] + other.lasted[i])
            if result[i]:   # 只要有时间存在，就是1(True)
                prompt += (str(result[i]) + self.unit[i])
        return prompt

