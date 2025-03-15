import matplotlib.pyplot as plt
import numpy as np

# 数据
x_labels = ['10w', '100w', '1000w']

traditional_bf = [37.6, 39.2, 50.1]
counting_bf = [37.7, 42.7, 87.2]
difference = [39.1, 203.5, 1723]

# t1 = [0.2, 0.6, 6.1]
# t2 = [0.1, 2.7, 25]

# # 更新BF和Counting BF数据
# traditional_bf = [traditional_bf[i] + t1[i] for i in range(len(traditional_bf))]
# counting_bf = [counting_bf[i] + t2[i] for i in range(len(counting_bf))]

# x轴位置
x = np.arange(len(x_labels))
width = 0.25

# 绘图
plt.figure(figsize=(8, 5))
bar1 = plt.bar(x - width, traditional_bf, width=width, label='BF', linewidth=2)
bar2 = plt.bar(x, counting_bf, width=width, label='Counting BF', linewidth=2)
bar3 = plt.bar(x + width, difference, width=width, label='List', linewidth=2)

# 在柱状图上标注数值
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.1f}', ha='center', va='bottom', fontsize=12)

add_labels(bar1)
add_labels(bar2)
add_labels(bar3)

# 设置标签和标题
plt.xlabel('ID members', fontsize=16)
plt.ylabel('memory cost (MB)', fontsize=16)
plt.title('memory cost of different methods', fontsize=20)
plt.xticks(x, x_labels)
plt.legend(fontsize=18)

# 显示图像
plt.tight_layout()
plt.show()
