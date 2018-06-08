from scipy.spatial.distance import euclidean

def knn(X_train, y_train, X_test, k, dist=euclidean):
    n_class = len(set(y_train))
    y_test = []
    for i in range(0, len(X_test)):
        distances = []
        for j in range(0, len(X_train)):
            distances.append(dist(X_train[j], X_test[i]))
        nearest = sorted(zip(distances, y_train))[:k]
        nearest_by_class = [(len([x for x in nearest if x[1] == i]), i) for i in range(1, n_classes + 1)]
        y_test.append(max(nearest_by_class)[1])
    return y_test
