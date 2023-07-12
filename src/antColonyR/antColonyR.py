# Import modules
import numpy as np
import math

# Import PySwarms
from pyswarms.utils.functions import single_obj as fx

seed = 1337
rng = np.random.default_rng(seed)

class ArchiveT:
    function = lambda x: x
    n = 0
    k = 0

    solutionsTable = np.array([[]])
    weights = np.array([])

    q = 1
    epsilon = 1

    def __init__(self, function, dimension, archiveSize, q, epsilon):
        self.function = function
        self.n = dimension
        self.k = archiveSize
        self.q = q
        self.epsilon = epsilon

    def __sortSolutionsTable(self):
        solutionsAppliedToFunc = self.function(self.solutionsTable)
        orderedIndexes = np.argsort(solutionsAppliedToFunc)
        self.solutionsTable = self.solutionsTable[orderedIndexes]

    def __initWeights(self):
        self.weights = np.zeros(self.k)
        for idx in range(self.k):
            rank = idx + 1
            self.weights[idx] = (1/(self.q * self.k * math.sqrt(2 * math.pi))) * math.pow(math.e, -((rank-1)**2)/(2 * (self.q**2) * (self.k**2)))

    def optimize(self, iterations=100, numberOfAnts=2): #TODO: arrumar os argumentos padrões
        self.solutionsTable = rng.uniform(-100, 100, [self.k, self.n]) #TODO: tirar o -100, 100 para depender do domínio da função a ser otimizada
        self.__initWeights()
        self.__sortSolutionsTable()

        for _ in range(iterations):
            # Sampling an archive row for each ant based on weights array:
            getRowDiscreteProbability = lambda w: w/sum(self.weights)
            sampledRowsIndexes = rng.choice(self.k, size=numberOfAnts, p=getRowDiscreteProbability(self.weights))
            newSolutionsSet = np.zeros(shape=(numberOfAnts, self.n))
            for antId in range(numberOfAnts):
                antRowIndex = sampledRowsIndexes[antId]
                # New solution construction:
                newSolution = np.zeros(self.n)
                for i in range(self.n):
                    # Constructing new solution component:
                    mean = self.solutionsTable[antRowIndex, i]
                    stdDeviation = (self.epsilon / (self.k - 1)) * sum(abs(np.delete(self.solutionsTable, antRowIndex, axis=0)[:,i] - self.solutionsTable[antRowIndex, i]))
                    newSolution[i] = rng.normal(mean, stdDeviation)
                # New solution found by this ant added to the set of new solutions found this iteration:
                newSolutionsSet[antId] = newSolution
            # Removing the numberOfAnts worst solutions from the solutions table:
            self.solutionsTable = self.solutionsTable[:-numberOfAnts]
            # Appending to the solutions table the set of new solutions found by the ants this iteration:
            self.solutionsTable = np.append(self.solutionsTable, newSolutionsSet, axis=0)
            # Sorting the updated solutions table based on the function to be optimized before starting the next iteration:
            self.__sortSolutionsTable()
        
        print(self.solutionsTable)


ArchiveT(function = fx.sphere, dimension = 2, archiveSize = 10, q=1, epsilon=1).optimize()