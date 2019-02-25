from sklearn.decomposition import PCA
def PCA_Transfer(X,comp):
    pca = PCA(n_components=comp)
    X = pca.fit_transform(X)
    return X