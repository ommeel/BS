import hashlib
import random
import string
import math
import time

n = 100000  # 成员数
theta = 0.01  # 错误率
m = -2.08 * n * math.log(theta)  # 位数组大小
m = int(m)
k = m / n * math.log(2)  # 哈希函数个数
k = int(k)

print("m: ", m, "k: ", k, "n: ", n)

def hash_func(x, seed):
    """ 用 SHA-256 哈希函数生成哈希值，并加入不同的种子来生成多个哈希函数 """
    return int(hashlib.sha256((str(x) + str(seed)).encode()).hexdigest(), 16)

class BloomFilter:
    def __init__(self, m, k, n):
        self.m = m
        self.k = k
        self.bit_array = bytearray((m + 7) // 8)  # 1-bit 位数组，每个字节存储 8 个 bit
        self.seed = [random.randint(n, m) for _ in range(k)]

    def add_element(self, x):
        for seed in self.seed:
            hash_value = hash_func(x, seed)
            index = hash_value % self.m
            byte_index = index // 8  # 找到对应的字节
            bit_index = index % 8   # 找到字节中的 bit 位置
            self.bit_array[byte_index] |= (1 << bit_index)  # 置 1

    def check_element(self, x):
        for seed in self.seed:
            hash_value = hash_func(x, seed)
            index = hash_value % self.m
            byte_index = index // 8
            bit_index = index % 8
            if not (self.bit_array[byte_index] & (1 << bit_index)):
                return False  # 如果有一个 bit 为 0，则一定不在过滤器中
        return True

def generate_random_string(length=10):
    """生成一个随机字符串，默认长度为 10"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

bf = BloomFilter(m, k, n)

# 插入随机元素
t2 = time.time()
random_members = [generate_random_string() for _ in range(n)]
for member in random_members:
    bf.add_element(member)

print(f"Insert Time: {time.time() - t2:.2f}s")
time.sleep(100)
# 验证查询
t3 = time.time()
found_count = sum(bf.check_element(member) for member in random_members)
print(f"Query Time: {time.time() - t3:.2f}s")

print(f"Found {found_count} / {n} members")

