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

    f4 = optproblems.cec2005.F4(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f4, function_index=4, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-10-4.txt", "w") as file:
        print("F4: Shifted Schwefel's Problem 1.2 with Noise in Fitness", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)

    with open("convergence/IA-convergence-10-4.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)   
    
    f9 = optproblems.cec2005.F9(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f9, function_index=9, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-10-9.txt", "w") as file:
        print("F9: Shifted Rastrigin's Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-10-9.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f12 = optproblems.cec2005.F12(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f12, function_index=12, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-10-12.txt", "w") as file:
        print("F12: Schwefel's Problem 2.13", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-10-12.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f21 = optproblems.cec2005.F21(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f21, function_index=21, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-10-21.txt", "w") as file:
        print("F21: Rotated Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-10-21.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f22 = optproblems.cec2005.F22(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f22, function_index=22, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-10-22.txt", "w") as file:
        print("F22: Rotated Hybrid Composition Function with High Condition Number Matrix", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-10-22.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)
