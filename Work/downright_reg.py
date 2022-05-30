# 调用包  
import matplotlib as mpl  
import matplotlib.pyplot as plt  
import pandas as pd  
 
# 用Pandas读取csv格式的文件  
sj = pd.read_csv('/content/ces.csv')  
 
# 提取文件中的数据  
x = sj['Depth']  
#BB = sj['Depth']  
DeltaPHI = sj['DeltaPHI']  
PHIND = sj['PHIND']  
 
# 创建图像  
fig = plt.figure(figsize=(30,5))  
# 绘制累计频率曲线  
#plt.plot(x,DeltaPHI,'r--',linewidth = 1,label='DeltaPHI')  
plt.plot(x,PHIND,'b-',linewidth = 1,label='PHIND')  
# plt.plot(x,MB,':k',linewidth = 1)  
 
# 设置题目与坐标轴名称  
plt.title('pre and real')  
plt.ylabel('danwei')  
plt.xlabel('Depth') 
 
# 设置图例（置于右下方）  
plt.legend(loc='lower right')  
 
# 显示图片  
plt.show()