import numpy as np

import matplotlib
import matplotlib.animation
import matplotlib.pyplot as plt

import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import (plot_cost_history, plot_contour)
from pyswarms.utils.plotters.formatters import Mesher, Designer

from utils.objectiveFunction import ObjectiveFunction

class ParticleSwarm:
    objective: ObjectiveFunction

    def __init__(self, functionId):
        self.objective = ObjectiveFunction(functionId)

    def execute(self, iterations:int=100, numberOfParticles:int=10, cognitiveParameter:float=0.5, socialParameter:float=0.3, inertiaParameter:float=0.9):
        np.random.seed(1337)

        # Set-up hyperparameters
        options = {'c1': cognitiveParameter, 'c2': socialParameter, 'w': inertiaParameter}

        # Initialize particle positions randomly in search space
        init_pos = np.random.uniform(low=self.objective.limits[0], high=self.objective.limits[1], size=(numberOfParticles, 2))

        # Call instance of PSO
        optimizer = ps.single.GlobalBestPSO(n_particles=numberOfParticles, dimensions=self.objective.dimensions, options=options, init_pos=init_pos)

        # Perform optimization
        (best_cost, best_pos) = optimizer.optimize(self.objective.function, iters=iterations)

        print('Final particle population position:\n', optimizer.pos_history[-1])
        print('Best solution:\n', best_pos)
        print('Cost of best solution:\n', best_cost)

        # Render visualization
        limits2D = [self.objective.limits, self.objective.limits]
        mesher2D = Mesher(func=self.objective.function, levels=self.objective.mesher2DLevels, limits=limits2D, delta=0.1)
        animationContour: matplotlib.animation.Animation = plot_contour(optimizer.pos_history, mesher=mesher2D, designer=Designer(limits=limits2D, label=["x-axis", "y-axis"]))
        matplotlib.animation.FFMpegWriter(animationContour)
        plot_cost_history(optimizer.cost_history)
        print('Close all visualization windows or send an interrupt signal (ctrl+c) to quit the program.')
        plt.show()