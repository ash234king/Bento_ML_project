import bentoml

from sklearn import svm
from sklearn import datasets

iris=datasets.load_iris()
x,y=iris.data,iris.target

clf=svm.SVC(gamma='scale')
clf.fit(x,y)

saved_model=bentoml.sklearn.save_model("iris_clf",clf)
print(f"Model saved: {saved_model}")

#iris_clf:wwmjtetav2utcuh6
