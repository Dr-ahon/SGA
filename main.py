import random
import pprint
import matplotlib.pyplot as plt
import numpy as np

POP_SIZE = 100
IND_LEN = 25
CX_PROB = 0.8
MUT_PROB = 0.05
MUT_FLIP_PROB = 0.1


# creates a single individual of lenght `lenght`
def create_individual(length):
    return [random.randint(0, 1) for _ in range(length)]


# creates a population of `size` individuals
def create_population(size):
    return [create_individual(IND_LEN) for _ in range(size)]

#
# # tournament selection
# def tournament_selection(population, fits):
#     selected = []
#     for _ in range(len(population)):
#         i1, i2 = random.randrange(0, len(population)), random.randrange(0, len(population))
#         if fits[i1] > fits[i2]:
#             selected.append(population[i1])
#         else:
#             selected.append(population[i2])
#     return selected


# roulette wheel selection
def roulette_selection(population, fits):
    return random.choices(population, fits, k=POP_SIZE)


# one point crossover
def cross(p1, p2):
    point = random.randint(0, len(p1))
    o1 = p1[:point] + p2[point:]
    o2 = p2[:point] + p1[point:]
    return o1, o2


# applies crossover to all individuals
def crossover(population):
    off = []
    for p1, p2 in zip(population[0::2], population[1::2]):
        o1, o2 = p1[:], p2[:]
        if random.random() < CX_PROB:
            o1, o2 = cross(p1[:], p2[:])
        off.append(o1)
        off.append(o2)
    return off


# bit-flip mutation
def mutate(p):
    if random.random() < MUT_PROB:
        return [1 - i if random.random() < MUT_FLIP_PROB else i for i in p]
    return p[:]


# applies mutation to the whole population
def mutation(population):
    return list(map(mutate, population))


# applies crossover and mutation
def reproduce(population):
    co_population = crossover(population)
    return mutation(co_population)


# evaluates the fitness of the individual
def get_fitness(ind):
    return sum(ind)


# implements the whole EA
def evolutionary_algorithm(fitness):
    population = create_population(POP_SIZE)
    log = []
    for G in range(100):
        fits = list(map(fitness, population))
        log.append((G, max(fits), sum(fits) / 100, G * POP_SIZE))
        # print(G, sum(fits), max(fits)) # prints fitness to console
        mating_pool = roulette_selection(population, fits)
        offspring = reproduce(mating_pool)
        # population = offspring[:-1]+[max(pop, key=fitness)] #SGA + elitism
        population = offspring[:]  # SGA

    return population, log


# run the EA 10 times and aggregate the logs, show the last gen in last run
logs = []
population = []
for i in range(10):
    random.seed(i)
    population, log = evolutionary_algorithm(get_fitness)
    logs.append(log)
fits = list(map(get_fitness, population))

# extract fitness evaluations and best fitnesses from logs
evals = []
best_fit = []
for log in logs:
    evals.append([l[3] for l in log])
    best_fit.append([l[1] for l in log])

evals = np.array(evals)
best_fit = np.array(best_fit)

# plot the converegence graph and quartiles

plt.plot(evals[0, :], np.median(best_fit, axis=0))
plt.fill_between(evals[0, :], np.percentile(best_fit, q=25, axis=0),
                 np.percentile(best_fit, q=75, axis=0), alpha=0.2)
plt.show()
