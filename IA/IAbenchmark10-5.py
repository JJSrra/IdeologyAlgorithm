import optproblems.cec2005
import numpy as np
import time
from IA import *
import os

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
    r = 0.5
    desertion_threshold = 10

    if not os.path.exists('results'):
        os.makedirs('results')

    if not os.path.exists('convergence'):
        os.makedirs('convergence')

    np.random.seed(10)

    f5 = optproblems.cec2005.F5(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f5, function_index=5, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-10-5.txt", "w") as file:
        print("F5: Schwefel's Problem 2.6 with Global Optimum on Bounds", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)

    with open("convergence/IA-convergence-10-5.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)   
    
    f10 = optproblems.cec2005.F10(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f10, function_index=10, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-10-10.txt", "w") as file:
        print("F10: Shifted Rotated Rastrigin's Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-10-10.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f23 = optproblems.cec2005.F23(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f23, function_index=23, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-10-23.txt", "w") as file:
        print("F23: Non-Continuous Rotated Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-10-23.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f24 = optproblems.cec2005.F24(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f24, function_index=24, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-10-24.txt", "w") as file:
        print("F24: Rotated Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-10-24.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f25 = optproblems.cec2005.F25(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f25, function_index=25, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-10-25.txt", "w") as file:
        print("F25: Rotated Hybrid Composition Function without Bounds", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-10-25.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)
