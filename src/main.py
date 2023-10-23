import sys
from implementations.particleSwarm import ParticleSwarm
from implementations.antColonyR import AntColonyR
from utils.menuHelpers import MenuHelpers

print('\n############\n# Welcome! #\n############')

algorithmId = MenuHelpers.getAlgorithmIdInput()
functionId = MenuHelpers.getObjectiveFunctionInput()

iterations = MenuHelpers.getPositiveIntegerInput('Insert the number of iterations the selected algorithm will run for', default=100)

#################
### PSO Setup ###
#################
if(algorithmId == 'PSO'):
    # Reading parameter values:
    numberOfParticles = MenuHelpers.getPositiveIntegerInput('Insert the number of particles', default=10)
    cognitiveParameter = MenuHelpers.getFloatInput('Insert the cognitive coefficient parameter value', default=0.5)
    socialParameter = MenuHelpers.getFloatInput('Insert the social coefficient parameter value', default=0.3)
    inertiaParameter = MenuHelpers.getFloatInput('Insert the inertia weight parameter value', default=0.9)
    # Executing optimization:
    ParticleSwarm(functionId).execute(iterations, numberOfParticles, cognitiveParameter, socialParameter, inertiaParameter)

##################
### ACOr Setup ###
##################
elif(algorithmId == 'ACOr'):
    # Reading parameter values:
    numberOfAnts =  MenuHelpers.getPositiveIntegerInput('Insert the number of ants', default=3)
    k = MenuHelpers.getPositiveIntegerInput('Insert the size k (number of lines) of the solutions archive T', default=10)
    q = MenuHelpers.getFloatInput('Insert the q coefficient parameter value', default=1)
    epsilon = MenuHelpers.getFloatInput('Insert the epsilon coefficient parameter value', default=1)
    # Executing optimization:
    AntColonyR(functionId).execute(iterations=int(iterations), numberOfAnts=3, k=10, q=1, epsilon=1)