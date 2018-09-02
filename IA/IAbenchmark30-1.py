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
    dim = 30
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

    f1 = optproblems.cec2005.F1(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f1, function_index=1, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-30-1.txt", "w") as file:
        print("F1: Shifted Sphere Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-30-1.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)


    np.random.seed(10)   
    
    f6 = optproblems.cec2005.F6(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f6, function_index=6, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-30-6.txt", "w") as file:
        print("F6: Shifted Rosenbrock's Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-30-6.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f14 = optproblems.cec2005.F14(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f14, function_index=14, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-30-14.txt", "w") as file:
        print("F14: Shifted Rotated Expanded Scaffer's F6", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-30-14.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f15 = optproblems.cec2005.F15(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f15, function_index=15, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-30-15.txt", "w") as file:
        print("F15: Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-30-15.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f16 = optproblems.cec2005.F16(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f16, function_index=16, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-30-16.txt", "w") as file:
        print("F16: Rotated Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-30-16.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)
