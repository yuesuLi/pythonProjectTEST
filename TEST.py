import scipy.signal as ss
import numpy as np
import torch
import time
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
import matplotlib.pyplot as pp


def detect_peaks(image):
    """
    Takes an image and detect the peaks using the local maximum filter.
    Returns a boolean mask of the peaks (i.e. 1 when
    the pixel's value is the neighborhood maximum, 0 otherwise)
    """

    # define an 8-connected neighborhood
    neighborhood = generate_binary_structure(2,2)

    #apply the local maximum filter; all pixel of maximal value
    #in their neighborhood are set to 1
    local_max = maximum_filter(image, footprint=neighborhood)
    print('local_max:', np.array(local_max).shape, '\n', local_max)
    #local_max is a mask that contains the peaks we are
    #looking for, but also the background.
    #In order to isolate the peaks we must remove the background from the mask.

    #we create the mask of the background
    background = (image==0)

    #a little technicality: we must erode the background in order to
    #successfully subtract it form local_max, otherwise a line will
    #appear along the background border (artifact of the local maximum filter)
    eroded_background = binary_erosion(background, structure=neighborhood, border_value=1)
    print('eroded_background:', eroded_background)
    #we obtain the final mask, containing only peaks,
    #by removing the background from the local_max mask (xor operation)
    detected_peaks = local_max ^ eroded_background

    return detected_peaks


lst = [[5., 7., 5., 7., 5.],
       [5., 9., 5.9, 5., 5.],
       [7., 7.2, 7.3, 5., 5.],
       [5., 6., 5., -2., 5.],
       [5., 6., 5., 5., 5.]]

# stime = time.time()
lst = torch.tensor(lst)
# etime = time.time()
# print(f'用时: {etime-stime}s')
print(lst[1])

peaks = detect_peaks(lst)
print(peaks)


