import numpy as np


def speed_direction_batch(dets, tracks_pre_obs):
    """
    input:
        dets: (num_dets, 2), (x, y)
        tracks_pre_obs: tracks' observation, (N_track, 3) (x, y, c)

    return: norm_dy, norm_dx (num_track, num_det)

    """
    tracks_pre_obs = tracks_pre_obs[..., np.newaxis]
    X1, Y1 = dets[:, 0], dets[:, 1]
    X2, Y2 = tracks_pre_obs[:, 0], tracks_pre_obs[:, 1]
    dx = X1 - X2
    dy = Y1 - Y2
    norm = np.sqrt(dx**2 + dy**2) + 1e-6
    dx = dx / norm
    dy = dy / norm
    return dy, dx

speed_direction_batch_tracks = np.array([1.7176, 1.4125, 0, 0]) # (num_tracks, )

# (num_dets, 2), (x, y)
detections_measurement = np.array([[2.998, 4.413], [-3.729, 5.081], [-0.145, 6.125], [-4.066, 13.969], [5.828, 19.299],
                                   [3.712, 27.416], [11.792, 25.763], [-4.386, 10.458], [10.072, 31.156],
                                   [11.512, 29.330], [9.901, 36.207], [7.136, 26.683]])
previous_obs = np.array([[6.37875, 16.45041, 1], [3.25249, 20.88135, 1], [-100, -100, -1], [-100, -100, -1]]) # (num_tracks, 3), (x, y, label)

velocities = np.array([[0.989, -0.146], [0.987, 0.157], [0, 0], [0, 0]])# (num_tracks, 2)

Y, X = speed_direction_batch(detections_measurement, previous_obs)  # norm_dy, norm_dx (num_track, num_det)
detections_orientation = np.arctan2(Y, X)
tracks_orientation = np.repeat(speed_direction_batch_tracks[:, np.newaxis], Y.shape[1], axis=1)

diff_angle = np.abs(detections_orientation - tracks_orientation)
print('done')




