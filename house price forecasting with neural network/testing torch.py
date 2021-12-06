import torch.nn as nn
import torch.optim as optim
import torch.utils.data.DataLoader as DataLoader

inputs_number = 1
outputs_number = 1
first_layer_neurons = 10
second_layer_neurons = 10
features_number = 75

model = nn.Sequential(
        nn.Linear(inputs_number, first_layer_neurons, bias = True), nn.ReLU(), nn.BatchNorm1d(features_number), nn.Dropout(0.1),
        nn.Linear(first_layer_neurons, second_layer_neurons, bias = True), nn.ReLU(), nn.BatchNorm1d(features_number), nn.Dropout(0.1),
        nn.Linear(second_layer_neurons, outputs_number, bias = True), nn.ReLU(),
    )

loss = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

train_data = pd.read_csv("C:/denFiles/git/introduction-to-ai/house price forecasting with neural network/train.csv")
test_data = pd.read_csv("C:/denFiles/git/introduction-to-ai/house price forecasting with neural network/test.csv")

test_edited = test_data.drop(['Alley','FireplaceQu','PoolQC', 'Fence', 'MiscFeature'], axis=1)
train_edited = train_data.drop(['Alley','FireplaceQu','PoolQC', 'Fence', 'MiscFeature'], axis=1)


def nan_filler(data):
    for label, content in data.items():
        if pd.api.types.is_numeric_dtype(content):
            data[label] = content.fillna(content.median())
        else:
            data[label] = content.astype("category").cat.as_ordered()
            data[label] = pd.Categorical(content).codes+1


nan_filler(test_edited)
nan_filler(train_edited)

X = train_edited.drop('SalePrice', axis=1)
y = train_edited['SalePrice']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = 0.2)

train_dataset = DataLoader