import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import matplotlib
from LogisticRegression import LogisticRegression

iris = datasets.load_iris()
X = iris.data[:, :2]
y = (iris.target != 0) * 1
model = LogisticRegression(np.array([0.01, 0.01, 0.01]), lr=0.1, num_iter=300000)
model.fit(X, y)
preds = model.predict(X)
(preds == y).mean()

matplotlib.use("TkAgg")
plt.figure(figsize=(10, 6))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color = 'g', label = '0')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color = 'y', label = '1')
plt.legend()

x1_min, x1_max = X[:, 0].min(), X[:, 0].max()
x2_min, x2_max = X[:, 1].min(), X[:, 1].max()
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
grid = np.c_[xx1.ravel(), xx2.ravel()]
probs = model.predict_prob(grid).reshape(xx1.shape)
plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors='red')
plt.show()