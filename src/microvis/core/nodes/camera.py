from __future__ import annotations

from abc import abstractmethod
from typing import Protocol, Tuple

import numpy as np

from microvis._types import CameraType, Matrix3x3
from microvis.core._vis_model import Field, VisModel

from .node import Node, NodeAdaptorProtocol


class Camera(Node, VisModel["CameraAdaptorProtocol"]):
    """A camera that defines the view of a scene."""

    position: Tuple[float, float, float] = Field(
        default=(0, 0, 0), description="Position of the viewpoint in the scene."
    )
    orientation: Matrix3x3 = Field(
        default=np.eye(3), description="Orientation of the view onto a scene."
    )
    zoom: float = Field(
        default=1.0,
        description="Zoom factor of the camera. Can be interpreted as number "
        "of (untransformed) data units per screen pixel.",
    )
    # are type and interactive necessarily camera attributes? Feels like the
    # camera is serving three purposes:
    # - defining the view onto scene (view matrix)
    # - defining the projection of scene from 3D -> 2D (zoom, perspective...)
    # - defining how a user interacts with the scene (type, 'interactive')
    #
    # user interactions feel like they should be attributes of the view,
    # not the camera... will not mirroring the vispy/pygfx api closely here make
    # things harder for us? leaving here for now
    type: CameraType = Field(
        default=CameraType.PANZOOM,
        description="Camera type defining ways of interactively navigating a " "scene.",
    )
    interactive: bool = Field(
        default=True,
        description="Whether the camera responds to user interaction, "
        "such as mouse and keyboard events.",
    )


# fmt: off
class CameraAdaptorProtocol(NodeAdaptorProtocol[Camera], Protocol):
    """Protocol for a backend camera adaptor object."""

    @abstractmethod
    def _vis_set_position(self, arg: tuple[float, ...]) -> None: ...
    @abstractmethod
    def _vis_set_zoom(self, arg: float) -> None: ...
    @abstractmethod
    def _vis_set_type(self, arg: CameraType) -> None: ...

# fmt: on
