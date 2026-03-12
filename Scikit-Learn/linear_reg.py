from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = datasets.fetch_california_housing()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(predictions[:5])

# use only one feature (Median Income)
X_feature = X[:, 0]

# scatter plot
plt.scatter(X_feature, y)

plt.xlabel("Median Income")
plt.ylabel("House Price")
plt.title("House Price Prediction Scatter Plot")

plt.show()
