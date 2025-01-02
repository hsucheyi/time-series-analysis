import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

from ch01 import plot_figure

mu = 0
n = 200
seed = 42
np.random.seed(seed)
alpha = np.random.normal(0, 1, n)
z = mu + alpha

# 圖2.3
plot_figure(
    x_data=range(1, 201),
    y_data=z,
    xlabel='時間',
    ylabel='Z',
    x_range=(0, 201),
    y_range=(-3.0, 3.4),
    x_ticks=range(0, 200, 12),
    y_ticks=np.arange(-3.0, 4, 1.6)
)

# 圖2.4
plot_acf(z, lags=10, title='')
plt.xlabel('落後期', fontsize=25, labelpad=10)
plt.ylabel(r'$r_k$', fontsize=25, fontname='Times New Roman', rotation=0, labelpad=15)
plt.xticks(fontsize=10, fontname='Times New Roman')
plt.yticks(fontsize=10, fontname='Times New Roman')
plt.show()

plot_pacf(z, lags=10, title='', method="ywm")
plt.xlabel('落後期', fontsize=25, labelpad=10)
plt.ylabel(r'$\hat{\phi}_{kk}$', fontsize=25, rotation=0, labelpad=15)
plt.xticks(fontsize=10, fontname='Times New Roman')
plt.yticks(fontsize=10, fontname='Times New Roman')
plt.show()