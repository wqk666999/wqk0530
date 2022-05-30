import pandas as pd
from sklearn.cluster import KMeans
from utils import Plot
from sklearn import preprocessing

def data_process(train_path,select_features):
    train_data = pd.read_csv(train_path)
    train_data.drop(columns='Facies',inplace=True)
    train_data['Formation'] = pd.Categorical(train_data['Formation'])
    train_data['Formation'] = train_data.Formation.cat.codes
    train_data = train_data.loc[:,select_features]
    return train_data

def train_useKmeans(data,options): # save_fig 是否存储图片
    # n_clusters:int, default=8,要形成的簇数以及要生成的质心数。
    # init:{‘k-means++’, ‘random’, ndarray, callable}, default=’k-means++’
        # 初始化方法：‘k-means++’：明智地选择初始聚类中心进行k均值聚类，加快收敛速度.有关详细信息，请参阅k_init中的Notes部分。
        # ‘random’：从初始质心的数据中随机选择n_clusters观测(行)。
        # 如果一个ndarray被传递，它应该是形状的(n_clusters, n_features)，并给出初始中心。
        # 如果传递了一个可调用函数，它应该接受参数X、n_clusters和一个随机状态，并返回一个初始化。
    # algorithm：{“auto”, “full”, “elkan”}, default=”auto”
    #表示K-means要使用的算法。经典的EM式算法是“full”的。通过三角不等式，对于具有定义良好的簇的数据，“elkan”变化更为有效。但是，由于分配了一个额外的形状数组(n_samples, n_clusters)，所以内存更多。
    # 目前，“auto”(为向后兼容而保留)选择了“Elkan”，但它将来可能会改变，以获得更好的启发式。
    scaler = preprocessing.StandardScaler().fit(data)
    data = scaler.transform(data)
    model = KMeans(
        n_clusters=options['n'],
        init=options['init'],
        algorithm=options['algorithm']
    )
    model.fit(data)
    labels = pd.Series(model.labels_)
    Plot().plot_in_2d(data, labels, title="kmeans")
    labels.to_csv('./kmeans.csv')

if __name__ == '__main__':
    options = {'n':8,
               'init':'k-means++',
               'algorithm':'auto'
              }
    data = data_process('./data/',['Formation','GR', 'ILD_log10', 'DeltaPHI', 'PHIND', 'PE', 'NM_M', 'RELPOS'])
    train_useKmeans(data,options)

