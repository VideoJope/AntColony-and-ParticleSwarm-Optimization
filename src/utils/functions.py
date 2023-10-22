from pyswarms.utils.functions import single_obj as fx

def getFunctionParametersByFunctionId(functionId):
    match functionId:
        case '1':
            return(fx.sphere)
        case '2':
            return (fx.ackley, (-10, 10))
        case '3':
            return (fx.threehump)
        case '4':
            return (fx.rastrigin)
        case _:
            raise Exception('Invalid function id')
