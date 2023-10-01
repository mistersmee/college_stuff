from numpy import array
from numpy import mean
from sklearn.decomposition import PCA

A=array([[2,8],
         [2,4],
         [8,3],
         [6,3],
         [2,3],
         [3,6]])
print("Array:\n",A)

M=mean(A.T,axis=1)
print("\nMean:",M)

pca=PCA(1)

pca.fit(A)

print("\nPCA Components(Normalize data):",pca.components_)

print("\nPCA Explained Variance(first principal component):",pca.explained_variance_)

B=pca.transform(A)
print("\nTransform Data:\n",B)