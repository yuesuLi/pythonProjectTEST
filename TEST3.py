import numpy as np
import scipy
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import matplotlib.pyplot as plt
import torch
a = input().strip().split()
neighborhood_size = 3
threshold = 0
#
# data = scipy.misc.imread(fname)
data = [[-1., -7., 5., 7., 5.],
       [-1.5, -9., 5.9, 8., 5.],
       [7., 7.2, 7.3, 5., 5.],
       [0.5, 0.6, 5., 7.4, 5.],
       [0.74, 0.6, 5., 1., 5.]]
data = np.array(data)
threshold = 0
data[data < threshold] = 0
print('data:\n', data)

data_max = filters.maximum_filter(data, neighborhood_size)
print('data_max:\n', data_max)
maxima = (data == data_max)
maxima[data == 0.] = False

print('where:', np.where(maxima==True))

# data_min = filters.minimum_filter(data, neighborhood_size)
# print('data_min:', data_min)
# diff = ((data_max - data_min) > threshold)
# maxima[diff == 0] = 0
print('maxima:\n', maxima)

labeled, num_objects = ndimage.label(maxima)
print('labeled:\n', labeled)
print('num_objects:\n', num_objects)
# xy = np.array(ndimage.center_of_mass(data, labeled, range(1, num_objects+1)))
# print('xy:', xy[:, 1], xy[:, 0])


slices = ndimage.find_objects(labeled)
print('slices:\n', slices)
x, y = [], []
for dx, dy in slices:
    x_center = (dx.start + dx.stop - 1)/2
    x.append(x_center)
    y_center = (dy.start + dy.stop - 1)/2
    y.append(y_center)

print('x:', x, 'y:', y)