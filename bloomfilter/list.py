 
import hashlib
import random
import time

member = 100000 # 成员数
n = [i for i in range(0, member)]

id = [hashlib.sha256(str(n[i]).encode()).hexdigest() for i in range(0, member)]
round = 100
t1 = time.time()
for _ in range(round):
    temp = random.randint(0, member)
    id_f = id[temp] 
    for i in range(0, member):
        if id_f == id[i]:
            # print(f"Find the same id: {id[i]}")
            break
print(f"Time: {(time.time() - t1) / round}")


