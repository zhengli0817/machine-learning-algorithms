import numpy as np

def kmeans(X, n_clusters):
    centers = init_centers(X, n_clusters) #centers = X[:n_clusters]
    y = None
    while True:
        new_y = np.argmin(np.linalg.norm(X.reshape(n_samples, 1, n_features) - centers, axis=2), axis=1)
        if np.array_equal(y, new_y):
            break
        y = new_y
        for i in range(n_clusters):
            centers[i] = X[y == i].mean(axis=0)
    return centers, y 
