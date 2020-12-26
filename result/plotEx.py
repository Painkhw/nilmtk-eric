'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 画第1个图：折线图
x=np.arange(1,100)
plt.subplot(221)
plt.plot(x,x*x)
# 画第2个图：散点图
plt.subplot(222)
plt.scatter(np.arange(0,10), np.random.rand(10))
# 画第3个图：饼图
plt.subplot(223)
plt.pie(x=[15,30,45,10],labels=list('ABCD'),autopct='%.0f',explode=[0,0.05,0,0])
# 画第4个图：条形图
plt.subplot(224)
plt.bar([20,10,30,25,15],[25,15,35,30,20],color='b')
plt.show()

'''
import matplotlib.pyplot as plt
defaultRate = (incomeRage['Defaulted'] / (incomeRage['Defaulted'] + incomeRage['Completed'])).reindex(index)#print(defaultRate)#坏账百分之
defaultRate1=defaultRate[['Not displayed','Not employed','$1-24,999','$25,000-49,999','$50,000-74,999','$75,000-99,999','$100,000+',]]#剔除$0为空NaN的值
print(defaultRate1)#坏账百分之
    # 违约率情况
    y = list(defaultRate1.values)#Dafrme转为list
    fig1 = plt.figure(1)
    # fig1.set_size_inches(15.5, 7.5)
    ax1 = fig1.add_subplot(2, 1, 2)
    x = np.arange(len(index)) + 1
    ax1.bar(x, y, width=0.4)
    ax1.set_xticks(x)
    ax1.set_xticklabels(index, rotation=0, fontsize=12)
    ax1.set_ylabel('违约百分率(%)', fontsize=14)
    for a, b in zip(x, y):
        plt.text(a, b + 0.001, '%.2f%%' % (b * 100), ha='center', va='bottom', fontsize=10)
    ax2 = fig1.add_subplot(2, 1, 1)
    incomeRage.plot(kind='bar', ax=ax2)
    ax2.set_xticklabels(index, rotation=0, fontsize=12)
    ax2.set_ylabel('数量', fontsize=14)
    plt.show()