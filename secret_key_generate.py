import matplotlib.pyplot as plt

x_labels = [i for i in range(1, 9)]
t = [35.532, 14.895, 7.691, 4.199, 2.327, 1.29, 0.712, 0.391]
c = [t[i] * (2 ** (i + 1) - 1) for i in range(8)]

width = 0.2

plt.figure(figsize=(12, 8))

# 创建第一个 y 轴（左侧）
ax1 = plt.gca()
ax1.bar(x_labels, c, width=0.5, label='Total', linewidth=1, color='royalblue')
ax1.set_ylabel('Total(ms)', fontsize=16, color='royalblue')
ax1.set_xlabel('N', fontsize=16)

# 创建第二个 y 轴（右侧）
ax2 = ax1.twinx()
ax2.plot(x_labels, t, label='Single', linewidth=2, color='darkorange', marker='o')
ax2.set_ylabel('Single(ms)', fontsize=16, color='darkorange')

# 设置 X 轴刻度和字体大小
ax1.set_xticks(x_labels)
ax1.tick_params(axis='both', labelsize=14)

# 添加图例
ax1.legend(loc='upper left', fontsize=14)
ax2.legend(loc='upper right', fontsize=14)

plt.tight_layout()
plt.show()
