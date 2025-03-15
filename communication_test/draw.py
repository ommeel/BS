import matplotlib.pyplot as plt
import numpy as np

# 设置数据
x_labels = ['1', '2', '3']  # 横坐标：1, 2, 3
data_sizes = [256, 512, 1024]  # 数据量：256, 512, 1024 bytes

# 使用你提供的数据
data_values = [
    [17.8, 27, 36.3],  # 对应 1 的 256, 512, 1024 bytes
    [30.2, 44.7, 60],  # 对应 2 的 256, 512, 1024 bytes
    [42, 66, 80]     # 对应 3 的 256, 512, 1024 bytes
]

# 设置柱状图的宽度
bar_width = 0.2
x = np.arange(len(x_labels))  # 横坐标的位置

# 绘制柱状图
fig, ax = plt.subplots()
for i, size in enumerate(data_sizes):
    ax.bar(x + i * bar_width, [data_values[j][i] for j in range(len(x_labels))], width=bar_width, label=f'{size} bytes')

# 设置横坐标和标签
ax.set_xticks(x + bar_width)
ax.set_xticklabels(x_labels)
ax.set_xlabel('N')
ax.set_ylabel('Time(ms)')
ax.set_title(' ')

# 添加图例
ax.legend()

# 显示图表
plt.tight_layout()
plt.show()