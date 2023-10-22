import sys
from implementations.particleSwarm import ParticleSwarm
from implementations.antColonyR import AntColonyR
from utils.functions import *

print('\n############\n# Welcome! #\n############')

algorithmId = '0'
while(algorithmId not in ['1', '2']):
    print('\nSelect which algorithm you wish to execute by typing their respective number:')
    print('  [1] Particle Swarm Optimization')
    print('  [2] Ant Colony Optimization (Continuous Domain)')
    algorithmId = input().strip()

functionId = '0'
while(functionId not in ['1', '2', '3', '4']):
    print('\nSelect which objective function you wish to execute the selected algorithm on:')
    print('  [1] Sphere function')
    print('  [2] Ackley function')
    print('  [3] Threehump function')
    print('  [4] Rastrigin function')
    functionId = input().strip()
(function, limits) = getFunctionParametersByFunctionId(functionId)

# PSO:
if(algorithmId == '1'):
    ParticleSwarm.execute(function, limits)

# ACOr:
elif(algorithmId == '2'):
    AntColonyR(function = function, limits=limits, dimension = 2, archiveSize = 10, q=1, epsilon=1).execute()

