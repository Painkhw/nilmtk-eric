import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter
import numpy as np
 
df=pd.DataFrame(np.arange(12).reshape(4,3),columns=['aaa','bbb','c'])
df['c']=100000000*np.random.rand(len(df))
fig,ax=plt.subplots(1,1,figsize=(9,6))
ax1=ax.twinx()
@FuncFormatter
def format(x,pos):
    return '%d'%x
ax.yaxis.set_major_formatter(format)
ax1.yaxis.set_major_formatter(format)
df['c'].plot(ax=ax1,figsize=(9,6),style=['g-'])
ax1.legend(('helloworld',),loc='upper center')
df[['aaa','bbb']].plot(kind='bar',grid=True,ax=ax,figsize=(9,7)) #柱状图应该在折线图之后画，防止因为折线图所需要的坐标轴面积更小而让柱状图结果显示不全
 
ax.plot(df.index,[1,2,3,4])
ax.legend(('new','aaa','bbb'))
