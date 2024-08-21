import numpy as np
import math
import cmath
# from openpyxl import load_workbook
import torch



def _gather_feature(feat, ind, mask=None):
  dim = feat.size(2)
  ind = ind.unsqueeze(2).expand(ind.size(0), ind.size(1), dim)
  feat = feat.gather(1, ind)
  if mask is not None:
    mask = mask.unsqueeze(2).expand_as(feat)
    feat = feat[mask]
    feat = feat.view(-1, dim)
  return feat


def _tranpose_and_gather_feature(feat, ind):
  feat = feat.permute(0, 2, 3, 1).contiguous()
  feat = feat.view(feat.size(0), -1, feat.size(3))
  feat = _gather_feature(feat, ind)
  return feat

lw_HM = torch.arange(18).view((1, 2, 3, 3))

print('TEST:', cmath.atan(lw_HM.numpy()))

# inds = torch.Tensor(3).view((1, 3))
# inds[0, 0] = 1
# inds[0, 1] = 3
# inds = inds.to(dtype=torch.int64)
# # print('inds:', inds)
#
# # print('before:', lw_HM)
# # lw_HM = [_tranpose_and_gather_feature(lw, inds) for lw in lw_HM]
# lw_HM = _tranpose_and_gather_feature(lw_HM, inds)
# print('after:', lw_HM)
# print('after:', lw_HM.detach().numpy().shape)
#
# inds_mask = torch.Tensor(3)
# inds_mask[0] = 1
# inds_mask[1] = 1
# inds_mask = inds_mask.to(dtype=torch.int64)
# print('before_inds_mask:', inds_mask, inds_mask.detach().numpy().shape)
#
#
# l_w_ = torch.arange(6).view((3, 2))
# l_w_[0, 0] = 1
# l_w_[0, 1] = 2
# l_w_[2, 0] = 0
# l_w_[2, 1] = 0
# print('l_w_:', l_w_, l_w_.detach().numpy().shape)
# inds_mask = inds_mask.expend_as(l_w_).float()
# print('after_inds_mask:', inds_mask, inds_mask.detach().numpy().shape)

