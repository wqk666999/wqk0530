# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing
from sklearn.utils import shuffle
# from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
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

def train_useRF(data,options):
    model = make_pipeline(StandardScaler(),RandomForestRegressor(n_estimators=options['n_estimators']
                #criterion=options['criterion']
                # max_depth=options['max_depth'],
                #min_samples_split=options['min_samples_split'],min_weight_fraction_leaf=options['min_weight_fraction_leaf']
                ))
    model.fit(data['X_train'],data['y_train'])
    y_pred = model.predict(data['X_valid'])
    x=data['pre_feature']
    da=pd.DataFrame({'Depth':data['valid_depth'],x+'_real':data['y_valid'],x+'_pre':y_pred})
    da2 = da.sort_values(by='Depth')
    da2.to_csv(x+"_reg.csv",index=False,sep=',')  
    mae = metrics.mean_absolute_error(data['y_valid'],y_pred)
    mse = metrics.mean_squared_error(data['y_valid'],y_pred)
    r2 = metrics.r2_score(data['y_valid'],y_pred)
    #confusion_matrix = metrics.confusion_matrix(data['y_valid'], y_pred)
    res = {'mae':mae,
            'mse':mse,
           'r2':r2,
           'path':x+'_reg.csv'}
    return res

# if __name__ == '__main__':
#     options = {'n_estimators': 100,
#                'criterion': 'gini',
#                # 'max_depth': 'auto',
#                # 'min_samples_split': 2,
#                # 'min_weight_fraction_leaf':0.0
#                }
    # data = data_process('./training_data.csv', './validation_data.csv',
    #                           ['GR', 'ILD_log10', 'DeltaPHI', 'PHIND', 'PE', 'NM_M', 'RELPOS'])
    # res = train_useRF(data, options)
    # print(res)
# rfmodel = RandomForestClassifier()
# rfmodel.fit(train_data,train_label)
# print('model')
# print(rfmodel)
#
# ypredrf1 = rfmodel.predict(test_data)
# print('confusion matrix')
# print(metrics.confusion_matrix(test_label, ypredrf1))
# print('classification report')
# print(metrics.classification_report(test_label, ypredrf1))
# print('Accuracy : %f' % (metrics.accuracy_score(test_label, ypredrf1)))
#
# f1_score = metrics.f1_score(test_label,ypredrf1,average='micro')
# recall_score = metrics.recall_score(test_label,ypredrf1,average='micro')
# print(f'f1是{f1_score}')
# print(f'recall是{recall_score}')
#
# clf = svm.SVC()
# clf.fit(train_data,train_label)
# ypredrf2 = clf.predict(test_data)
# print('Accuracy : %f' % (metrics.accuracy_score(test_label, ypredrf2)))

