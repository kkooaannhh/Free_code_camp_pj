import numpy as np
def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        calculations = {}
        matrix0 = np.array(list).reshape(3,3)
        calculations['mean'] = [np.mean(matrix0,0).tolist(),np.mean(matrix0, 1).tolist(), np.mean(matrix0).tolist()]
        calculations['variance'] = [np.var(matrix0,0).tolist(),np.var(matrix0, 1).tolist(), np.var(matrix0).tolist()]
        calculations['standard deviation'] = [np.std(matrix0,0).tolist(),np.std(matrix0, 1).tolist(), np.std(matrix0).tolist()]
        calculations['max'] = [np.max(matrix0,0).tolist(),np.max(matrix0, 1).tolist(), np.max(matrix0).tolist()]
        calculations['min'] = [np.min(matrix0,0).tolist(),np.min(matrix0, 1).tolist(), np.min(matrix0).tolist()]
        calculations['sum'] = [np.sum(matrix0,0).tolist(),np.sum(matrix0, 1).tolist(), np.sum(matrix0).tolist()]
        return calculations


meanlist = calculate([2, 6, 2, 8, 4, 0, 1, 5])
print(meanlist)
