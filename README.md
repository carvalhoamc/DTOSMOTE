# DTO-SMOTE
DELAUNAY THETRAEDRAL OVERSAMPLING SMOTE

Oversampling creates synthetic or duplicate minority class sam-
ples to match the same number of samples from the majority class.
As a result, the training data set becomes balanced before the training
phase. DTO-SMOTE constructs a mesh of simplices
for creating synthetic examples.

See test.py 


delaunay = DTO('teste1','solid_angle',7.5)
Here, we have three parameters:
'test1' is a temp filename for dtosmote.

geometry, could be: 
'area'
'volume'
'area_volume_ratio'
'edge_ratio'
'radius_ratio'
'aspect_ratio'
'max_solid_angle'
'min_solid_angle'
'solid_angle'

and dirichlet alpha: [1,10[
