from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import sklearn.metrics as metrics
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import os
from PIL import Image
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np


def data_process(train_path,validation_path,select_features,pre_feature):
    train_data = pd.read_csv(train_path)
    valid_data = pd.read_csv(validation_path)
    train_depth=train_data['Depth']
    valid_depth=valid_data['Depth']
    train_data_x = train_data.loc[:,select_features]
    train_data_y = train_data[pre_feature]
    valid_data_x = valid_data.loc[:,select_features]
    valid_data_y = valid_data[pre_feature]
    data = {'X_train':train_data_x,'y_train':train_data_y,'X_valid':valid_data_x,'y_valid':valid_data_y,'train_depth':train_depth,'valid_depth':valid_depth,'pre_feature':pre_feature}
    return data

def train_useXGBoost(data,options):
                    #   n_estimators=10,           # 树的个数-10棵树建立xgboost
                    #   max_depth=4,               # 树的深度
                    #   min_child_weight = 1,      # 叶子节点最小权重
                    #   gamma=0.,                  # 惩罚项中叶子结点个数前的参数
                    #   subsample=1,               # 所有样本建立决策树
                    #   colsample_btree=1,         # 所有特征建立决策树
                    #   scale_pos_weight=1,        # 解决样本个数不平衡的问题
                    #   random_state=27,           # 随机数
                    #   slient = 0
    model = make_pipeline(StandardScaler(),XGBClassifier(
                learning_rate=0.01,
                n_estimators=10,
                max_depth=4,
                min_child_weight=1,
                gamma=0,
                subsample=1))
    model.fit(data['X_train'],data['y_train'])
    y_pred = model.predict(data['X_valid'])
    da=pd.DataFrame({'Depth':data['valid_depth'],'Facies_real':data['y_valid'],'Facies_pre':y_pred})
    #da2 = da.sort_values(by='Depth')
    da.to_csv("svm_Facies_pre.csv",index=False,sep=',') 
    logs=pd.read_csv('svm_Facies_pre.csv') 
    make_facies_log_plot(logs)
    acc = metrics.precision_score(data['y_valid'],y_pred,average='micro')
    f1_score = metrics.f1_score(data['y_valid'],y_pred,average='micro')
    recall_score = metrics.recall_score(data['y_valid'],y_pred,average='micro')
    confusion_matrix = metrics.confusion_matrix(data['y_valid'], y_pred)
    res = {'acc':acc,
           'f1_score':f1_score,
           'recall_score':recall_score,
           'confusion_matrix':confusion_matrix}
    return res

def make_facies_log_plot(logs):
    #make sure logs are sorted by depth
    logs = logs.sort_values(by='Depth')
    facies_colors = ['#F4D03F', '#F5B041','#DC7633','#6E2C00',
       '#1B4F72','#2E86C1', '#AED6F1', '#A569BD', '#196F3D']
    cmap_facies = colors.ListedColormap(
            facies_colors[0:len(facies_colors)], 'indexed')
    ztop=logs.Depth.min(); zbot=logs.Depth.max()
    cluster=np.repeat(np.expand_dims(logs['Facies_real'].values,1), 50, 1)
    cluster2=np.repeat(np.expand_dims(logs['Facies_pre'].values,1), 50, 1)
    f, ax = plt.subplots(nrows=1, ncols=2, figsize=(2, 10))
    im=ax[0].imshow(cluster, interpolation='none', aspect='auto',
                    cmap=cmap_facies,vmin=1,vmax=9)
    im=ax[1].imshow(cluster2, interpolation='none', aspect='auto',
                    cmap=cmap_facies,vmin=1,vmax=9)
    divider = make_axes_locatable(ax[1])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar=plt.colorbar(im, cax=cax)
    cbar.set_label((17*' ').join([' SS ', 'CSiS', 'FSiS', 
                                'SiSh', ' MS ', ' WS ', ' D  ', 
                                ' PS ', ' BS ']))
    cbar.set_ticks(range(0,1)); cbar.set_ticklabels('')
    ax[0].set_xlabel('Facies_real')
    ax[1].set_xlabel('Facies_pre')
    ax[0].set_yticklabels([]); 
    ax[1].set_yticklabels([])
    #plt.figure(figsize=(8, 4))
    plt.savefig('XGBoost_Facies_fig.png')
    img = Image.open('XGBoost_Facies_fig.png')
    img = img.transpose(Image.ROTATE_270)
    img.save("XGBoost_Facies_fig_270.png")
# if __name__ == '__main__':
#     options = {'C': 1.0,
#                'kernel': 'linear',
#                'gamma': 'auto',
#                'decision_function_shape': 'ovr'
#                }
#     data = data_process('./training_data.csv', './validation_data.csv',
#                               ['GR', 'ILD_log10', 'DeltaPHI', 'PHIND', 'PE', 'NM_M', 'RELPOS'],['Facies'])
#     res = train_useSVM(data, options)
#     print(res)