X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=2)
neigh.fit(X, y)
A = neigh.kneighbors_graph()
A.toarray()

print('predict 1.9', neigh.predict([[1.9]]))
print('proba 1.9', neigh.predict_proba([[1.9]]))
