import hashlib
import random
import string
import math
import time

n = 10000000  # 成员数
theta = 0.01  # 错误率
m = -2.08 * n * math.log(theta)  # 位数组大小
m = int(m)
k = m / n * math.log(2)  # 哈希函数个数
k = int(k)

print("m: ", m, "k: ", k, "n: ", n)

def hash_func(x, seed):
    """ 用 SHA-256 哈希函数生成哈希值，并加入不同的种子来生成多个哈希函数 """
    return int(hashlib.sha256((str(x) + str(seed)).encode()).hexdigest(), 16)

class CountingBloomFilter:
    def __init__(self, m, k, n):
        self.m = m
        self.k = k
        self.counter_array = bytearray((m + 1) // 2)  # 4-bit 计数器，每个字节存储 2 个计数器
        self.seed = [random.randint(n, m) for _ in range(k)]

    def _get_counter(self, index):
        """ 获取指定索引处的计数器值 """
        byte_index = index // 2
        if index % 2 == 0:
            return self.counter_array[byte_index] & 0x0F  # 低 4 位
        else:
            return (self.counter_array[byte_index] >> 4) & 0x0F  # 高 4 位

    def _set_counter(self, index, value):
        """ 设置指定索引处的计数器值 """
        byte_index = index // 2
        if index % 2 == 0:
            self.counter_array[byte_index] = (self.counter_array[byte_index] & 0xF0) | (value & 0x0F)
        else:
            self.counter_array[byte_index] = (self.counter_array[byte_index] & 0x0F) | ((value & 0x0F) << 4)

    def add_element(self, x):
        for seed in self.seed:
            hash_value = hash_func(x, seed)
            index = hash_value % self.m
            count = self._get_counter(index)
            if count < 15:  # 最大计数为 16，防止溢出
                self._set_counter(index, count + 1)

    def remove_element(self, x):
        for seed in self.seed:
            hash_value = hash_func(x, seed)
            index = hash_value % self.m
            count = self._get_counter(index)
            if count > 0:  # 计数不能低于 0
                self._set_counter(index, count - 1)

    def check_element(self, x):
        for seed in self.seed:
            hash_value = hash_func(x, seed)
            index = hash_value % self.m
            if self._get_counter(index) == 0:
                return False
        return True

def generate_random_string(length=10):
    """生成一个随机字符串，默认长度为 10"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

cbf = CountingBloomFilter(m, k, n)

# 插入随机元素
t2 = time.time()
random_members = [generate_random_string() for _ in range(n)]
for member in random_members:
    cbf.add_element(member)
print(f"Insert Time: {time.time() - t2:.2f}s")
random_members = 0
time.sleep(100)

# 删除部分元素
t3 = time.time()
for member in random_members[:n // 2]:
    cbf.remove_element(member)
print(f"Remove Time: {time.time() - t3:.2f}s")

# 查询验证
t4 = time.time()
found_count = sum(cbf.check_element(member) for member in random_members)
print(f"Query Time: {time.time() - t4:.2f}s")

print(f"Found {found_count} / {n} members")
