from typing import Literal
import numpy as np
from pyswarms.utils.functions import single_obj as fx

class ObjectiveFunction:
    function = lambda x: x
    limits = (0, 0)
    dimensions = 2
    mesher2DLevels = np.array([[]])

    def __init__(self, functionId: Literal['sphere', 'ackley', 'threehump', 'rastrigin']):
        match functionId:
            case 'sphere':
                self.function = fx.sphere
                self.limits = (-1, 1)
                self.mesher2DLevels = np.arange(0, 0.8, 0.015)
            case 'ackley':
                self.function = fx.ackley
                self.limits = (-10, 10)
                self.mesher2DLevels = np.arange(0, 22.0, 0.5)
            case 'threehump':
                self.function = fx.threehump
                self.limits = (-5, 5)
                self.mesher2DLevels = np.arange(0, 25, 0.5)
            case 'rastrigin':
                self.function = fx.rastrigin
                self.limits = (-5.12, 5.12)
                self.mesher2DLevels = np.arange(0, 50, 5)
            case _:
                raise Exception('Invalid function id')