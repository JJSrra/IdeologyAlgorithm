import optproblems.cec2005
import numpy as np
import time
from IA import *

if __name__ == "__main__":
    dim = 10
    repeats = 10
    evaluations = 10000*dim
    parties = 5
    politicians = 30
    r_values = [0.05,0.1,0.2,0.3]
    desertion_thresholds = [10,15,20,25]

    f1 = optproblems.cec2005.F1(dim)
    print("F1: Shifted Sphere Function\n")

    for r in r_values:
        for desertion_threshold in desertion_thresholds:
            time1 = time.time()
            IA = IdeologyAlgorithm(n_parties=parties, politicians=politicians, R=r, function=f1,
                function_index=1, max_evaluations=evaluations, desertion_threshold=desertion_threshold)
            results = np.array([IA.ideology_algorithm() for _ in range(repeats)])
            total_time = time.time() - time1
            print("R: {}\tDesertion threshold: {}".format(r, desertion_threshold))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")
    
    f6 = optproblems.cec2005.F6(dim)
    print("F6: Shifted Rosenbrock’s Function\n")

    for r in r_values:
        for desertion_threshold in desertion_thresholds:
            time1 = time.time()
            IA = IdeologyAlgorithm(n_parties=parties, politicians=politicians, R=r, function=f6,
                function_index=6, max_evaluations=evaluations, desertion_threshold=desertion_threshold)
            results = np.array([IA.ideology_algorithm() for _ in range(repeats)])
            total_time = time.time() - time1
            print("R: {}\tDesertion threshold: {}".format(r, desertion_threshold))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    f14 = optproblems.cec2005.F14(dim)
    print("F14: Shifted Rotated Expanded Scaffer’s F6\n")

    for r in r_values:
        for desertion_threshold in desertion_thresholds:
            time1 = time.time()
            IA = IdeologyAlgorithm(n_parties=parties, politicians=politicians, R=r, function=f14,
                function_index=14, max_evaluations=evaluations, desertion_threshold=desertion_threshold)
            results = np.array([IA.ideology_algorithm() for _ in range(repeats)])
            total_time = time.time() - time1
            print("R: {}\tDesertion threshold: {}".format(r, desertion_threshold))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")

    print("###############################################")

    f15 = optproblems.cec2005.F15(dim)
    print("F15: Hybrid Composition Function\n")

    for r in r_values:
        for desertion_threshold in desertion_thresholds:
            time1 = time.time()
            IA = IdeologyAlgorithm(n_parties=parties, politicians=politicians, R=r, function=f15,
                function_index=15, max_evaluations=evaluations, desertion_threshold=desertion_threshold)
            results = np.array([IA.ideology_algorithm() for _ in range(repeats)])
            total_time = time.time() - time1
            print("R: {}\tDesertion threshold: {}".format(r, desertion_threshold))
            print("Min: {:e}\nMax: {:e}\nMean: {:e}\nMean time: {:5f} sec".format(np.min(results), np.max(results), np.mean(results), total_time / repeats))
            print("_______________________________________________")
