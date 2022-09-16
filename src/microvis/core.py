from itertools import product
from .viewer import Viewer
from vispy import scene
import numpy as np


def imshow(data, background_color=None) -> Viewer:
    viewer = Viewer(background_color=background_color)
    viewer.add_image(data)
    viewer.show()
    return viewer


def ortho(data: np.ndarray) -> Viewer:
    viewer = Viewer()

    shape = data.shape
    cmap = "gray"

    scene.visuals.Volume(np.transpose(data, (-1, 0, 1)), parent=viewer[0, 0].scene)
    scene.visuals.Image(data[:, :, shape[2] // 2], parent=viewer[1, 0].scene, cmap=cmap)
    scene.visuals.Image(data[:, shape[1] // 2, :], parent=viewer[0, 1].scene, cmap=cmap)
    scene.visuals.Image(
        data[shape[0] // 2, :, :].T, parent=viewer[1, 1].scene, cmap=cmap
    )

    for coord in product((0, 1), (0, 1)):
        viewer[coord].camera.set_range()

    return viewer
