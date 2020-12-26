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

from plotnine import *  ## 导入plotnine库

## 绘制前加括号
(
    ggplot(data,aes(x='x',y='value',fill='product')) ## 数据对象
    + geom_bar(stat='identity',width=0.5) ## 绘制柱状图的API
    + theme(  ## 对绘图的表现进行调整
            text = element_text(family = "SimHei"),  ## 设置黑体，可以显示中文
            legend_direction ='horizontal',  ## 图例水平呈现
            legend_title = element_blank(),  ## 图例标题不显示
            legend_background = element_rect('none'),  ##  图例没有背景色
            legend_position = (0.52,0.83),  ## 设置图例位置
            figure_size = (9,5),  ##  画布的大小
            axis_title_x = element_blank(),  ## X轴标题为空
            axis_title_y = element_blank()  ## Y轴标题为空
           )
)