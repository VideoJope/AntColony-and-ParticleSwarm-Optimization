from typing import Literal
import numpy as np
from pyswarms.utils.functions import single_obj as fx

def getObjectiveFunctionDataByFunctionId(functionId: Literal['sphere', 'ackley', 'threehump', 'rastrigin']):
    match functionId:
        case 'sphere':
            return(fx.sphere, (-1, 1), 2)
        case 'ackley':
            return (fx.ackley, (-10, 10), 2)
        case 'threehump':
            return (fx.threehump, (-5, 5), 2)
        case 'rastrigin':
            return (fx.rastrigin, (-5.12, 5.12), 2)
        case _:
            raise Exception('Invalid function id')


def getMesher2DLevelsByFunctionId(functionId: Literal['sphere', 'ackley', 'threehump', 'rastrigin']):
    match functionId:
        case 'sphere':
            return np.arange(0, 0.8, 0.015)
        case 'ackley':
            return np.arange(0, 22.0, 0.5)
        case 'threehump':
            return np.arange(0, 25, 0.5)
        case 'rastrigin':
            return np.arange(0, 50, 5)
        case _:
            raise Exception('Invalid function id')