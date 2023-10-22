LINE_UP = '\033[1A' #ANSI escape code

class MenuHelpers:
    def getAlgorithmIdInput():
        while(True):
            print('\nSelect which algorithm you wish to execute by typing their respective number:')
            print('  [1] Particle Swarm Optimization')
            print('  [2] Ant Colony Optimization (Continuous Domain)')
            inputString = input().strip()
            if(inputString == '1'): return 'PSO'
            if(inputString == '2'): return 'ACOr'
            else: print('ERROR: Invalid value. Please insert one of the listed options\' number.')

    def getObjectiveFunctionInput():
        while(True):
            print('\nSelect which objective function you wish to optimize:')
            print('  [1] Sphere function')
            print('  [2] Ackley function')
            print('  [3] Threehump function')
            print('  [4] Rastrigin function')
            inputString = input().strip()
            if(inputString == '1'): return 'sphere'
            if(inputString == '2'): return 'ackley'
            if(inputString == '3'): return 'threehump'
            if(inputString == '4'): return 'rastrigin'
            else: print('ERROR: Invalid value. Please insert one of the listed options\' number.')


    def getPositiveIntegerInput(message:str, default:int):
        while(True):
            print(f'\n{message} [default={default}]:')
            inputString = input().strip()
            if(inputString.isdigit()):
                return int(inputString)
            if(inputString == ''):
                print(f'{LINE_UP}{default}')
                return default
            else:
                print('ERROR: Invalid value. Please insert a positive integer.')

    def getFloatInput(message:str, default:float):
        while(True):
            print(f'\n{message} [default={default}]:')
            inputString = input().strip()
            if(inputString == ''):
                print(f'{LINE_UP}{default}')
                return default
            try:
                output = float(inputString)
                return output
            except ValueError:
                print('ERROR: Invalid value. Please insert a floating point number.')

