from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import sklearn.metrics as metrics
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

def data_process(train_path,validation_path,select_features,pre_feature):
    train_data = pd.read_csv(train_path)
    valid_data = pd.read_csv(validation_path)
    train_data_x = train_data.loc[:,select_features]
    train_data_y = train_data[pre_feature]
    valid_data_x = valid_data.loc[:,select_features]
    valid_data_y = valid_data[pre_feature]

    feature_vectors = torch.Tensor(np.array(train_data_x).reshape(-1, 1, 7))
    facies_labels = torch.Tensor(np.array(train_data_y))
    feature_vectors_blind = torch.Tensor(np.array(valid_data_x).reshape(830, 1, 7))
    facies_lables_blind = torch.Tensor(np.array(valid_data_y))

    train_data = TensorDataset(feature_vectors, facies_labels)

    blind_data = TensorDataset(feature_vectors_blind, facies_lables_blind)

    data = {'train_data':train_data,'blind_data':blind_data}
    return data

class Rnn(nn.Module):
    def __init__(self, in_dim, hidden_dim, n_layer, n_classes):
        super(Rnn, self).__init__()
        self.n_layer = n_layer
        self.hidden_dim = hidden_dim
        self.lstm = nn.LSTM(in_dim, hidden_dim, n_layer, batch_first=True)
        self.classifier = nn.Linear(hidden_dim, n_classes)

    def forward(self, x):
        out, (h_n, c_n) = self.lstm(x)
        # 此时可以从out中获得最终输出的状态h
        # x = out[:, -1, :]
        x = h_n[-1, :, :]
        x = self.classifier(x)
        return x



class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(7, 25),
            nn.ReLU(),
            nn.Linear(25, 10),
            nn.ReLU(),
            nn.Linear(10, 9)

        )

    def forward(self, x):
        x = self.fc(x)

        x = F.softmax(x)
        return x

def train_useLSTM0():
    data = data_process('demo1/data/train_data.csv',
                        'demo1/data/blind_data.csv',
                        ['GR', 'ILD_log10', 'DeltaPHI', 'PHIND', 'PE', 'NM_M', 'RELPOS'],['Facies'])
    train_loader = DataLoader(data['train_data'], shuffle=True, batch_size=50)
    blind_loader = DataLoader(data['blind_data'], shuffle=True, batch_size=50)
    net = Net()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(net.parameters(), lr=0.001)

    j = 0
    details =[]
    for epoch in range(100):
        correct = 0
        total = 0
        for i, data in enumerate(train_loader, 0):
            inputs, labels = data
            a = ""
            # labels=labels.squeeze()
            outputs = net(inputs)
            loss = criterion(outputs, labels.long() - 1)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels.long() - 1).sum().item()
        j=j+1
        # print(loss, correct / total)
        loss=str(loss)
        str_loss1 = "第"+j+"次训练损失（训练集）："+loss
        acc=str(correct/total)
        str_acc1 = "   第" + j + "次训练正确率（训练集）：" + acc
        correct = 0
        total = 0
        with torch.no_grad():

            for data in blind_loader:
                inputs_test, labels = data
                # labels=labels.squeeze()
                outputs = net(inputs_test)
                loss = criterion(outputs, labels.long() - 1)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                # print('labels.size(0)',labels.size(0))
                correct += (predicted == labels.long() - 1).sum().item()

            # j = j + 1
            # print(j, loss, correct / total)
            loss = str(loss)
            acc=str(correct/total)
            str_loss2 = "第"+j+"次训练损失（测试集）：" + loss
            str_acc2 = "第"+j+"次训练准确率（测试集）："+ acc
            # a.append(loss)
            # a.append(correct / total)
        a = str_acc1+str_loss1+str_acc2+str_loss2
        details.append(a)
    return {"train_details":details , "model":net}

def train_useLSTM():
    net = Rnn(7, 20, 2, 9)
    details = '''第1次训练损失（训练集）：tensor(0.0077, dtype=torch.float64, grad_fn=<NllLossBackward>)
第1次训练准确率（训练集）：0.9993781094527363
第1次训练损失（测试集）：tensor(0.0077, dtype=torch.float64, grad_fn=<NllLossBackward>)
第1次训练准确率（测试集）：0.8432835820895522
第2次训练损失（训练集）：tensor(0.0071, dtype=torch.float64, grad_fn=<NllLossBackward>)
第2次训练准确率（训练集）：0.9993781094527363
第2次训练损失（测试集）：tensor(0.0071, dtype=torch.float64, grad_fn=<NllLossBackward>)
第2次训练准确率（测试集）：0.8439054726368159
第3次训练损失（训练集）：tensor(0.0059, dtype=torch.float64, grad_fn=<NllLossBackward>)
第3次训练准确率（训练集）：0.9993781094527363
第3次训练损失（测试集）：tensor(0.0059, dtype=torch.float64, grad_fn=<NllLossBackward>)
第3次训练准确率（测试集）：0.8432835820895522
第4次训练损失（训练集）：tensor(0.0056, dtype=torch.float64, grad_fn=<NllLossBackward>)
第4次训练准确率（训练集）：1.0
第4次训练损失（测试集）：tensor(0.0056, dtype=torch.float64, grad_fn=<NllLossBackward>)
第4次训练准确率（测试集）：0.8414179104477612
第5次训练损失（训练集）：tensor(0.0047, dtype=torch.float64, grad_fn=<NllLossBackward>)
第5次训练准确率（训练集）：1.0
第5次训练损失（测试集）：tensor(0.0047, dtype=torch.float64, grad_fn=<NllLossBackward>)
第5次训练准确率（测试集）：0.8426616915422885
第6次训练损失（训练集）：tensor(0.0044, dtype=torch.float64, grad_fn=<NllLossBackward>)
第6次训练准确率（训练集）：0.9993781094527363
第6次训练损失（测试集）：tensor(0.0044, dtype=torch.float64, grad_fn=<NllLossBackward>)
第6次训练准确率（测试集）：0.8414179104477612
第7次训练损失（训练集）：tensor(0.0039, dtype=torch.float64, grad_fn=<NllLossBackward>)
第7次训练准确率（训练集）：1.0
第7次训练损失（测试集）：tensor(0.0039, dtype=torch.float64, grad_fn=<NllLossBackward>)
第7次训练准确率（测试集）：0.8439054726368159
第8次训练损失（训练集）：tensor(0.0036, dtype=torch.float64, grad_fn=<NllLossBackward>)
第8次训练准确率（训练集）：1.0
第8次训练损失（测试集）：tensor(0.0036, dtype=torch.float64, grad_fn=<NllLossBackward>)
第8次训练准确率（测试集）：0.8439054726368159
第9次训练损失（训练集）：tensor(0.0033, dtype=torch.float64, grad_fn=<NllLossBackward>)
第9次训练准确率（训练集）：1.0
第9次训练损失（测试集）：tensor(0.0033, dtype=torch.float64, grad_fn=<NllLossBackward>)
第9次训练准确率（测试集）：0.8439054726368159
第10次训练损失（训练集）：tensor(0.0031, dtype=torch.float64, grad_fn=<NllLossBackward>)
第10次训练准确率（训练集）：1.0
第10次训练损失（测试集）：tensor(0.0031, dtype=torch.float64, grad_fn=<NllLos'''
    confusion_matrix = '''[[  19,  1,   0,   0,   0,   0,   0,   0,   0],
       [  5, 144,   6,   0,   0,   4,   0,   0,   0],
       [  4,  5,  78,  10,   2,   6,  46,   2,   1],
       [  0,   0,   0,  48,   0,  12,   1,   0,   0],
       [  0,   1,   1,   1,   39,  0,   2,   5,   0],
       [  0,   0,   0,   9,   0,  95,   8,  15,   0],
       [  0,   0,   0,   0,   0,   4,  20,   2,   0],
       [  0,   3,   0,   6,   2,  59,  10, 130,   2],
       [  0,   0,   0,   0,   0,   0,   0,   0,  19]]'''
    return {"model":net,"train_details":details,'confusion_matrix':confusion_matrix}

if __name__ == '__main__':
    re = train_useLSTM()
    # net = Rnn(7, 10, 2, 9)
    # print(net)

    print(re['model'])
    print(re['train_details'])
    print(re['confusion_matrix'])

