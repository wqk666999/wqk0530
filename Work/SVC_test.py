from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import sklearn.metrics as metrics
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import os
from PIL import Image
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
    #data = {'X_train':train_data_x,'y_train':train_data_y,'X_valid':valid_data_x,'y_valid':valid_data_y}
    return data

def train_useSVM(data,options):
    # C：错误项的惩罚系数。C越大，即对分错样本的惩罚程度越大，因此在训练样本中准确率越高，但是泛化能力降低，也就是对测试数据的分类准确率降低。相反，减小C的话，容许训练样本中有一些误分类错误样本，泛化能力强。对于训练样本带有噪声的情况，一般采用后者，把训练样本集中错误分类的样本作为噪声。
    # kernel='linear'时，为线性核，C越大分类效果越好，但有可能会过拟合（defaul C=1）。
    # kernel='rbf'时（default），为高斯核，gamma值越小，分类界面越连续；gamma值越大，分类界面越“散”，分类效果越好，但有可能会过拟合。
    # kernel='poly'时，多项式函数,degree 表示多项式的程度-----支持非线性分类。更高gamma值，将尝试精确匹配每一个训练数据集，可能会导致泛化误差和引起过度拟合问题。
    # kernel='sigmoid'时，支持非线性分类。更高gamma值，将尝试精确匹配每一个训练数据集，可能会导致泛化误差和引起过度拟合问题。
    # gamma：float参数 默认为auto。核函数系数，只对‘rbf’,‘poly’,‘sigmod’有效。如果gamma为auto，代表其值为样本特征数的倒数，即1/n_features.
    # decision_function_shape='ovr'时，为one v rest，即一个类别与其他类别进行划分，
    # decision_function_shape='ovo'时，为one v one，即将类别两两之间进行划分，用二分类的方法模拟多分类的结果。
    # probability：bool参数 默认为False，是否启用概率估计。 这必须在调用fit()之前启用，并且会fit()方法速度变慢。
    # cache_size：float参数 默认为200，指定训练所需要的内存，以MB为单位，默认为200MB。
    # class_weight：字典类型或者‘balance’字符串。默认为None，给每个类别分别设置不同的惩罚参数C，如果没有给，则会给所有类别都给C=1，即前面参数指出的参数C.如果给定参数‘balance’，则使用y的值自动调整与输入数据中的类频率成反比的权重。
    # max_iter ：int参数 默认为-1，最大迭代次数，如果为-1，表示不限制
    model = make_pipeline(StandardScaler(),SVC(C=options['C'],
                kernel=options['kernel'],
                gamma=options['gamma'],
                decision_function_shape=options['decision_function_shape']))
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
           'confusion_matrix':confusion_matrix,
           'y_pred':y_pred
           }
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
    plt.savefig('SvmFacies_fig.png')
    img = Image.open('SvmFacies_fig.png')
    img = img.transpose(Image.ROTATE_270)
    img.save("SvmFacies_fig_270.png")
    #f.suptitle('Well: %s'%logs.iloc[0]['Well Name'], fontsize=14,y=0.94)
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