import numpy as np

def perceptron(weight, bias, x):
    model = np.add(np.dot(x, weight), bias)
    print('model: {}'.format(model))
    logit = 1/(1+np.exp(-model))
    print('Type: {}'.format(logit))
    return np.round(logit)

def compute(logictype, weightdict, dataset):
    weights = np.array([ weightdict[logictype][w] for w in weightdict[logictype].keys()[::-1]])
    output = np.array([ perceptron(weights, weightdict['bias'][logictype], val) for val in dataset])
    print(logictype)
    return logictype, output

logic = {
    '_and' : {
        'w0': -0.1,
        'w1': 0.2,
        'w2': 0.2
    },
    '_or': {
        'w0': -0.1,
        'w1': 0.7,
        'w2': 0.7
    },
    '_nand': {
        'w0': 0.6,
        'w1': -0.8,
        'w2': -0.8
    },
    '_nor': {
        'w0': 0.5,
        'w1': -0.7,
        'w2': -0.7
    },
    '_not': {
        'w0': 0.5,
        'w1': -0.7
    },
    'bias': {
        '_and': -0.2,
        '_or': -0.1,
        '_nand': 0.3,
        '_nor': 0.1,
        '_not': 0.1
    }
}
dataset = np.array([
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
])

_and = compute('_and', logic, dataset)
_or = compute('_or', logic, dataset)
_nand = compute('_nand', logic, dataset)
_nor = compute('_nor', logic, dataset)
_not = compute('_not', logic, [[1,0],[1,1]])

def template(dataset, name, data):
    print("\nLogic Function: {}".format(name[1:].upper()))
    if name is "_not":
        print("X\tY")
        toPrint = ["{3}\t{0}".format(output, *datas) for datas, output in zip(dataset, data)]
        for i in toPrint:
            print(i)
    else:
        print("X1\tX2\tY")
        toPrint = ["{2}\t{3}\t{0}".format(output, *datas) for datas, output in zip(dataset, data)]
        for i in toPrint:
            print(i)

gates = [_and, _or, _nand, _nor, _not]

for i in gates:
    template(dataset, *i)