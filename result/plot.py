'''
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")
# 获取数据
titanic = sns.load_dataset("titanic")
"""
案例5：使用catplot()来实现countplot()的统计效果，必须设置kind="count"
当要对其他分类变量进行分组时，使用catplot()比直接使用FacetGrid更加安全
"""
sns.catplot(x="class", hue="who", col="survived",
            data=titanic, kind="count",
            height=4, aspect=.7);

plt.show()
'''

'''
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(8)
y = np.array([1,5,3,6,2,4,5,6])

df = pd.DataFrame({"x-axis": x,"y-axis": y})

sns.barplot(x="class",y=,palette="RdBu_r",data=df)
plt.xticks(rotation=90)
plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt

size = 5
x = np.arange(size)
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)

total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2

plt.bar(x, a,  width=width, label='a')
plt.bar(x + width, b, width=width, label='b')
plt.bar(x + 2 * width, c, width=width, label='c')
plt.legend()
plt.show()
