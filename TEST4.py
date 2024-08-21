import numpy as np
import torch
from torch import nn
import scipy
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import matplotlib.pyplot as plt


neighborhood_size = 3
threshold = 0
max_num_objects = 6
heat_map_scores = [[1., 7., 5., 7., 5.],
       [1.5, 9., 5.9, 8., 5.],
       [7., 7.2, 7.3, 5., 5.],
       [0.5, 0.6, 5., 7.4, 5.],
       [0.74, 0.6, 5., 1., 5.]]

bs, grid_height, grid_width = 1, 5, 5
heat_map_scores = np.array(heat_map_scores).reshape(1, 1, 5, 5)
heat_map_scores = torch.from_numpy(heat_map_scores)
my_maxpool = nn.MaxPool2d(kernel_size=(3, 3), stride=1, padding=1)
# max_scores = nn.MaxPool2d(data, kernel_size=3, padding=0)
max_scores = my_maxpool(heat_map_scores)
# threshold = 0
# data[data < threshold] = 0
# print('data:\n', heat_map_scores)
# print('max_scores:\n', max_scores)

# peak_mask = torch.equal(heat_map_scores, max_scores).long()
peak_mask = torch.eq(heat_map_scores, max_scores).type(torch.float)
filtered_heat_map = heat_map_scores * peak_mask

print('filtered_heat_map', filtered_heat_map)

flattened_t_heat_map = torch.reshape(filtered_heat_map, [1, 1, -1])
_, batch_top_k_indices = torch.topk(flattened_t_heat_map, k=max_num_objects, sorted=True)
batch_top_k_indices = batch_top_k_indices.transpose(1, 2)
batch_index = torch.arange(1, dtype=torch.float) * grid_height * grid_width * 1

flattened_indices = (
      torch.reshape(batch_index, [bs, 1, 1]) + batch_top_k_indices * 1 +
      torch.reshape(torch.arange(1, dtype=torch.float), [1, 1, 1]))
flattened_indices = torch.reshape(flattened_indices, [-1]).type(torch.int)
top_k_indices = torch.as_tensor(np.unravel_index(flattened_indices, (grid_height, grid_height)))
# top_k_indices = py_utils.HasShape(
# tf.transpose(top_k_indices), [bs * max_num_objects * nms_cls, 4])
top_k_indices = torch.reshape(torch.transpose(top_k_indices, 0, 1), [bs * max_num_objects * 1, 2])
peak_heat_map = filtered_heat_map
peak_heat_map.data = torch.where(filtered_heat_map.data >= 5., filtered_heat_map.data, 0.)


print('top_k_indices:\n', top_k_indices)
print('peak_heat_map:\n', peak_heat_map)



