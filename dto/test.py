from collections import Counter
from sklearn.datasets import make_classification
from dto.dto_smote import DTO

X, y = make_classification(n_classes=3, class_sep=2,
                           weights=[0.1,0.2, 0.9], n_informative=3, n_redundant=1, flip_y=0,
                           n_features=20, n_clusters_per_class=1, n_samples=100, random_state=10)

print('Original dataset shape %s' % Counter(y))
delaunay = DTO('teste1','solid_angle',7.5)
X_res, y_res = delaunay.fit_resample(X, y)
print('Resampled dataset shape %s' % Counter(y_res))

