# Import modules
import numpy as np

import matplotlib
import matplotlib.animation
import matplotlib.pyplot as plt

# Import PySwarms
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import (plot_cost_history, plot_contour, plot_surface)
from pyswarms.utils.plotters.formatters import Mesher, Designer

def optimizeAndAnimate(cognitiveParameter:float = 0.5, socialParameter:float = 0.3, inertiaParameter:float = 0.9, func:str = 'sphere'):
    np.random.seed(1337)

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
    # Parameters:
    n_particles = 10
    n_iters = 100

    low = -10
    high = 10
    limits = [(low, high), (low, high)]
    init_pos = np.random.uniform(low=low, high=high, size=(n_particles, 2))

    # Call instance of PSO
    optimizer = ps.single.GlobalBestPSO(n_particles=n_particles, dimensions=2, options=options, init_pos=init_pos)
    # Perform optimization
    cost, pos = optimizer.optimize(function, iters=n_iters, verbose=True)

    cost_history = optimizer.cost_history
    pos_history = optimizer.pos_history

    # print('pos_history', pos_history[0])
    # print('velocity_history', optimizer.velocity_history[1])

    mesher2D = Mesher(func=function, levels=np.arange(0, 22.0, 0.5), limits=limits, delta=0.1)
    animationContour: matplotlib.animation.Animation = plot_contour(pos_history, mesher=mesher2D, designer=Designer(limits=limits, label=["x-axis", "y-axis"]))
    

    # limits3D = [(-10, 10), (-10, 10), (-0.5, 22)]
    # mesher3D = Mesher(func=function, limits=limits3D, levels=np.arange(0, 22.0, 1))
    # pos_history3D = mesher3D.compute_history_3d(pos_history)
    # animationSurface = plot_surface(pos_history3D, mesher=mesher3D, designer=Designer(limits=limits3D, label=["x-axis", "y-axis", "z-axis"]))

    matplotlib.animation.FFMpegWriter(animationContour)
    # matplotlib.animation.FFMpegWriter(animationSurface)

    plot_cost_history(cost_history)

    plt.show()