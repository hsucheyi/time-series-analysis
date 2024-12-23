import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib import rcParams

import data

def plot_figure(x_data, y_data, xlabel, ylabel, x_range, y_range, x_ticks, y_ticks):
    '''
    :param x_data: x 軸的資料
    :param y_data: y 軸的資料
    :param xlabel: x 軸標籤
    :param ylabel: y 軸標籤
    :param x_range: x 軸的範圍 (tuple: (min, max))
    :param y_range: y 軸的範圍 (tuple: (min, max))
    :param x_ticks: x 軸的刻度
    :param y_ticks: y 軸的刻度
    '''
    line = plt.plot(x_data, y_data, color='black', marker='o', markersize=3)
    plt.margins(x=0)
    plt.xlabel(xlabel, fontsize=25, labelpad=10)
    plt.ylabel(ylabel, fontsize=25, rotation=0, labelpad=15)
    plt.xticks(x_ticks, fontsize=10, fontname='Times New Roman')
    plt.yticks(y_ticks, fontsize=10, fontname='Times New Roman')
    plt.xlim(*x_range)
    plt.ylim(*y_range)
    plt.setp(line, color='black', marker='o', markersize=3)
    plt.show()

rcParams['font.sans-serif'] = ['DFKai-SB']
rcParams['axes.unicode_minus'] = False

# 圖1.3
plot_figure(
    x_data=range(1, 71),
    y_data=data.fig_1_3,
    xlabel='時間',
    ylabel='產\n量',
    x_range=(0, 71),
    y_range=(10, 70),
    x_ticks=range(0, 71, 2),
    y_ticks=range(10, 71, 15)
)

# 圖1.4
plot_figure(
    x_data=range(1, 53),
    y_data=data.fig_1_4,
    xlabel='時間',
    ylabel='銷\n售\n量',
    x_range=(0, 53),
    y_range=(200, 920),
    x_ticks=range(0, 53, 2),
    y_ticks=range(200, 921, 180)
)

# 圖1.5
plot_figure(
    x_data=range(1, 157),
    y_data=data.fig_1_5,
    xlabel='時間',
    ylabel='百\n分\n比',
    x_range=(0, 157),
    y_range=(0, 6),
    x_ticks=range(0, 157, 12),
    y_ticks=np.arange(0, 7, 1.5)
)

# 圖1.6
plot_figure(
    x_data=range(1, 157),
    y_data=data.fig_1_6,
    xlabel='時間',
    ylabel='消\n費\n量',
    x_range=(0, 157),
    y_range=(15, 27),
    x_ticks=range(0, 157, 12),
    y_ticks=np.arange(15, 28, 2.4)
)

# 圖1.7
plot_figure(
    x_data=range(1, 151),
    y_data=data.fig_1_7_a,
    xlabel='時間',
    ylabel='銷\n售\n量',
    x_range=(0, 151),
    y_range=(190, 270),
    x_ticks=range(0, 150, 12),
    y_ticks=np.arange(190, 271, 20)
)

plot_figure(
    x_data=range(1, 151),
    y_data=data.fig_1_7_b,
    xlabel='時間',
    ylabel='領\n先\n指\n標',
    x_range=(0, 151),
    y_range=(9, 14.6),
    x_ticks=range(0, 150, 12),
    y_ticks=np.arange(9, 15, 1.4)
)

# 圖1.8
x = sm.add_constant(data.fig_1_7_b)
model = sm.OLS(data.fig_1_7_a, x).fit()

plt.scatter(data.fig_1_7_b, data.fig_1_7_a, color='black', marker='s', s=9)
plt.plot(data.fig_1_7_b, model.predict(x), color='black')
plt.xlabel('領先指標', fontsize=25, labelpad=10)
x_ticks = np.arange(9.7, 15, 0.54)
plt.ylabel('銷\n售\n量', fontsize=25, rotation=0, labelpad=15)
plt.xticks(x_ticks, fontsize=10, fontname='Times New Roman')
y_ticks = np.arange(190, 271, 20)
plt.yticks(y_ticks, fontsize=10, fontname='Times New Roman')
plt.xlim(9.7, 14.02)
plt.ylim(190, 270)
plt.show()