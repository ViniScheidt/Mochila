import sys
import numpy as np
def fit(equation_points, equation_inputs):

    somar = np.sum(equation_inputs * equation_points, axis=1)

    fit = []

    for i in somar :
        if (i > 30 ) :
            i *= -9999999

        fit.append(i)

    return np.array(fit)

def selection(populacao, fit, nmr_parentes):
    parents = np.empty((nmr_parentes, populacao.shape[1])) # 4 x 6
    for idx in range(nmr_parentes):
        max_fit_idx = np.where(fit == np.max(fit))
        max_fit_idx = max_fit_idx[0][0]
        parents[idx, :] = populacao[max_fit_idx, :]
        fit[max_fit_idx] = -999999
    return parents

def crossover(parents, generation_size):
    offspring = np.empty(generation_size)
    crossover_point = np.uint8(generation_size[1]/2)
    for idx in range(generation_size[0]):
        p1_idx = idx % parents.shape[0]
        p2_idx = (idx + 1) % parents.shape[0]
        offspring[idx, 0:crossover_point] = parents[
            p1_idx, 0:crossover_point]
        offspring[idx, crossover_point:] = parents[
            p2_idx, crossover_point:
        ]
    return offspring

def mutation(offspring):
    for idx in range(offspring.shape[0]):


        random_idx = np.random.randint(offspring.shape[1])
        offspring[idx, random_idx] = (
            abs(offspring[idx, random_idx] - 1)
        )
    return offspring