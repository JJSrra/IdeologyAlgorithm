import cec2014
import numpy as np
import time
from IA import *

def IAalgorithm(n_parties, politicians, R, function, function_index, max_evaluations, desertion_threshold):
    IA = IdeologyAlgorithm(n_parties=n_parties, politicians=politicians, R=R, function=function,
                function_index=function_index, max_evaluations=max_evaluations, desertion_threshold=desertion_threshold)
    return IA.ideology_algorithm()

if __name__ == "__main__":

    dim = 10
    repeats = 10
    evaluations = 10000*dim
    parties = 5
    politicians = 30
    r_values = [0.05,0.1,0.2,0.3]
    desertion_thresholds = [10,15,20,25]

    np.random.seed(10)

    def f1(x):
        return cec2014.cec14(x,1)

    f1.num_variables = dim
    f1.min_bounds = np.repeat(-100.0, dim)
    f1.max_bounds = np.repeat(100.0, dim)
    
    print("F1: Rotated High Conditioned Elliptic Function\n")

    for r in r_values:
        for desertion_threshold in desertion_thresholds:
            time1 = time.time()
            results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
                R=r, function=f1, function_index=1, max_evaluations=evaluations,
                desertion_threshold=desertion_threshold) for _ in range(repeats)])
            total_time = time.time() - time1
            print("R: {}\tDesertion threshold: {}".format(r, desertion_threshold))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")
    
    np.random.seed(10)

    def f4(x):
        return cec2014.cec14(x,4)

    f4.num_variables = dim
    f4.min_bounds = np.repeat(-100.0, dim)
    f4.max_bounds = np.repeat(100.0, dim)
    
    print("F4: Shifted and Rotated Rosenbrock’s Function\n")

    for r in r_values:
        for desertion_threshold in desertion_thresholds:
            time1 = time.time()
            results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
                R=r, function=f4, function_index=4, max_evaluations=evaluations,
                desertion_threshold=desertion_threshold) for _ in range(repeats)])
            total_time = time.time() - time1
            print("R: {}\tDesertion threshold: {}".format(r, desertion_threshold))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    def f17(x):
        return cec2014.cec14(x,17)

    f17.num_variables = dim
    f17.min_bounds = np.repeat(-100.0, dim)
    f17.max_bounds = np.repeat(100.0, dim)
    
    print("F17: Hybrid Function 1 (N=3)\n")

    for r in r_values:
        for desertion_threshold in desertion_thresholds:
            time1 = time.time()
            results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
                R=r, function=f17, function_index=17, max_evaluations=evaluations,
                desertion_threshold=desertion_threshold) for _ in range(repeats)])
            total_time = time.time() - time1
            print("R: {}\tDesertion threshold: {}".format(r, desertion_threshold))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    np.random.seed(10)

    def f23(x):
        return cec2014.cec14(x,23)

    f23.num_variables = dim
    f23.min_bounds = np.repeat(-100.0, dim)
    f23.max_bounds = np.repeat(100.0, dim)
    
    print("F23: Composition Function 1 (N=5)\n")

    for r in r_values:
        for desertion_threshold in desertion_thresholds:
            time1 = time.time()
            results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
                R=r, function=f23, function_index=23, max_evaluations=evaluations,
                desertion_threshold=desertion_threshold) for _ in range(repeats)])
            total_time = time.time() - time1
            total_time = time.time() - time1
            print("R: {}\tDesertion threshold: {}".format(r, desertion_threshold))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")
