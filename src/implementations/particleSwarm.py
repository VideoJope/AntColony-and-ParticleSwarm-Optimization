# Import modules
import numpy as np

import matplotlib
import matplotlib.animation
import matplotlib.pyplot as plt

# Import PySwarms
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import (plot_cost_history, plot_contour)
from pyswarms.utils.plotters.formatters import Mesher, Designer


class ParticleSwarm:
    function = lambda x: x
    limits = (0, 0)
    cognitiveParameter = 0.5
    socialParameter = 0.3
    inertiaParameter = 0.9

    def __init__(self, function, limits, cognitiveParameter:float = 0.5, socialParameter:float = 0.3, inertiaParameter:float = 0.9):
        self.function = function
        self.limits = limits
        self.cognitiveParameter = cognitiveParameter
        self.socialParameter = socialParameter
        self.inertiaParameter = inertiaParameter


    def execute(self):
        np.random.seed(1337)

        # Set-up hyperparameters
        options = {'c1': self.cognitiveParameter, 'c2': self.socialParameter, 'w': self.inertiaParameter}
        # Parameters:
        n_particles = 10
        n_iters = 100

        init_pos = np.random.uniform(low=self.limits[0], high=self.limits[1], size=(n_particles, 2))

        # Call instance of PSO
        optimizer = ps.single.GlobalBestPSO(n_particles=n_particles, dimensions=2, options=options, init_pos=init_pos)
        # Perform optimization
        optimizer.optimize(function, iters=n_iters, verbose=True)

        cost_history = optimizer.cost_history
        pos_history = optimizer.pos_history

        # print('pos_history', pos_history[0])
        # print('velocity_history', optimizer.velocity_history[1])

        limits2D = [self.limits, self.limits]
        mesher2D = Mesher(func=function, levels=np.arange(0, 22.0, 0.5), limits=limits2D, delta=0.1)
        animationContour: matplotlib.animation.Animation = plot_contour(pos_history, mesher=mesher2D, designer=Designer(limits=limits2D, label=["x-axis", "y-axis"]))

        matplotlib.animation.FFMpegWriter(animationContour)
        plot_cost_history(cost_history)
        plt.show()