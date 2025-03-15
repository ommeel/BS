import hashlib
import random
import string
import math
import time
n = 10000000 # 成员数
theta = 0.01 # 错误率
m = -2.08 * n * math.log(theta) # 位数组大小
m = int(m)
k = m / n * math.log(2) # hash函数个数
k = int(k)

M = [0] * m
print("m: ", m, "k: ", k, "n: ", n)

def hash_func(x, seed):
    """ 用 SHA-256 哈希函数生成哈希值，并加入不同的种子来生成多个哈希函数 """
    return int(hashlib.sha256((str(x) + str(seed)).encode()).hexdigest(), 16)

class Time_bloomfilter:
    def __init__(self, m, k, n):
        self.m = m
        self.k = k
        self.bit_array = [0] * m
        self.seed = [random.randint(n, m) for _ in range(k)]

    def add_element(self, x):
        for i in self.seed:
            hash_value = hash_func(x, i)  
            index = hash_value % m  
            self.bit_array[index] += 1  

    def check_element(self, x):
        for i in range(k):
            hash_value = hash_func(x, i)
            index = hash_value % m
            if self.bit_array[index] == 0:
                return False  
        return True
    
    def remove_element(self, x):
        for i in self.seed:
            hash_value = hash_func(x, i)
            index = hash_value % m
            if self.bit_array[index] > 0:
                self.bit_array[index] -= 1

tbf = Time_bloomfilter(m, k, n)
def generate_random_string(length=10):
    """生成一个随机字符串，默认长度为 10"""
    characters = string.ascii_letters + string.digits  
    return ''.join(random.choice(characters) for _ in range(length))

x = n  # 成员数
t2 = time.time()
random_members = [generate_random_string() for _ in range(x)]
for member in random_members:
    tbf.add_element(member)
print(f"Time: {time.time() - t2}")


# time.sleep(100) #同于测试内存占用
round = 10000
t1 = time.time()
for _ in range(round):
    temp = random.randint(0, x-1)
    if tbf.check_element(random_members[temp]):
        pass
        # print(f"Find the same id: {random_members[temp]}")
print(f"Time: {(time.time() - t1) / round}")

fake_positive = 0
fake_members = [generate_random_string(length=11) for _ in range(x)]
for _ in range(round):
    temp = random.randint(0, x-1)
    if tbf.check_element(random_members[temp]):
        fake_positive += 1
print(f"Fake positive rate: {fake_positive / round}",fake_positive)
