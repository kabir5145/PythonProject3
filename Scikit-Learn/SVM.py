from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

# split it in features and labels
X = iris.data
y = iris.target

classes = ['iris Setosa','Iris Versicolor','Iris Virginica']
# print(X, y)
# print(X.shape)
# print(y.shape)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = svm.SVC()
model.fit(X_train, y_train)

print(model)

pr = model.predict(X_test)
accuracy = accuracy_score(y_test, pr)

print("Prediction : ",pr)
print("Actual : ",y_test)
print("Accuracy : ",accuracy)

for i in range(len(pr)):
    print(classes[pr[i]])