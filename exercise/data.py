import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# 线条的粗细
plt.plot(input_value, squares, linewidth=5)

# 设置图标标题
plt.title("Squares Numbers", fontsize=24)

# 并给坐标轴加上标签
plt.xlabel("X", fontsize=14)
plt.ylabel("Y", fontsize=14)

# 设置刻度标记
plt.tick_params(axis='both', labelsize=14)

plt.show()

