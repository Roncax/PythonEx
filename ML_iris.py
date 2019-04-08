# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
path = "A:\Documents\Git Project\PythonEx\Iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(path, names=names)    # returned as two-dimensional data structure with labeled axes (as a matrix)

print(dataset.shape)        # In the example, 150 instances and 5 attributes
print(dataset.head(20))     # Print the first 20 instances of the dataset
print(dataset.describe())   # count, mean, standard deviation, min, max, and lower/50/upper percentiles
print(dataset.groupby('class').size())      # class distribution

# univariate plots (plot for each individual variable)
dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
dataset.hist()

# scatter plot matrix
scatter_matrix(dataset)
plt.show()

# split dataset 80% in train and 20% in validation
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


# Test options and evaluation metric - 10-fold cross validation
seed = 7
scoring = 'accuracy'        # ratio of the number of correctly predicted instances in divided by the total number of instances in the dataset multiplied by 100 to give a percentage

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))