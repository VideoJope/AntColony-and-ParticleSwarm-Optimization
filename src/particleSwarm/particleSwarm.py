# Import modules
import numpy as np

import matplotlib.animation
import matplotlib.pyplot as plt

# Import PySwarms
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import (plot_cost_history, plot_contour, plot_surface)
from pyswarms.utils.plotters.formatters import Mesher

def optimizeAndAnimate(cognitiveParameter:float = 0.5, socialParameter:float = 0.3, inertiaParameter:float = 0.9, func:str = 'sphere'):
    supportedFuncs = {
        'sphere': fx.sphere,
        'ackley': fx.ackley,
        'threehump': fx.threehump,
        'rastrigin': fx.rastrigin
    }
    if func not in supportedFuncs:
        raise Exception("Function passed as 'func' parameter is not supported")
    function = supportedFuncs[func]

    # Set-up hyperparameters
    options = {'c1': cognitiveParameter, 'c2': socialParameter, 'w': inertiaParameter}

    # Call instance of PSO
    optimizer = ps.single.GlobalBestPSO(n_particles=50, dimensions=2, options=options)

    cost_history = optimizer.cost_history
    pos_history = optimizer.pos_history

    # Perform optimization
    cost, pos = optimizer.optimize(function, iters=100, verbose=True)

    animation: matplotlib.animation.Animation = plot_contour(pos_history, mesher=Mesher(function), mark=(0,0))
    matplotlib.animation.FFMpegWriter(animation)

    plot_cost_history(cost_history)

    plt.show()