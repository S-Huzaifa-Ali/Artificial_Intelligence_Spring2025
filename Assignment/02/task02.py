import random

initial_population = [
    [1, 3, 1, 2, 3, 2, 1],
    [3, 2, 2, 1, 1, 3, 2],
    [3, 3, 2, 2, 1, 1, 3],
    [1, 1, 2, 3, 1, 2, 2],
    [1, 3, 3, 1, 1, 1, 2],
    [2, 2, 3, 2, 1, 1, 3]
]

task_times = [5, 8, 4, 7, 6, 3, 9]
facility_caps = [24, 30, 28]

cost_matrix = [
    [10, 12, 9],
    [15, 14, 16],
    [8, 9, 7],
    [12, 10, 13],
    [14, 13, 12],
    [9, 8, 10],
    [11, 12, 13]
]

POP_SIZE = 6
NUM_TASKS = len(task_times)
NUM_FACILITIES = len(facility_caps)
GENS = 50

def fitness(chrom):
    facility_load = [0] * NUM_FACILITIES
    total_cost = 0

    for i, facility in enumerate(chrom):
        task_time = task_times[i]
        facility = facility - 1
        facility_load[facility] += task_time
        total_cost += cost_matrix[i][facility] * task_time

    penalty = 0
    for i in range(NUM_FACILITIES):
        if facility_load[i] > facility_caps[i]:
            penalty += (facility_load[i] - facility_caps[i]) * 100

    return - (total_cost + penalty)

def roulette_selection(pop, fits):
    min_fit = min(fits)
    shifted_fits = [f - min_fit + 1 for f in fits]
    total_fit = sum(shifted_fits)
    pick = random.uniform(0, total_fit)
    current = 0
    for chrom, fit in zip(pop, shifted_fits):
        current += fit
        if current >= pick:
            return chrom
    return pop[0]

def one_point_crossover(p1, p2):
    point = random.randint(1, NUM_TASKS - 2)
    return p1[:point] + p2[point:], p2[:point] + p1[point:]

def mutate(chrom):
    i, j = random.sample(range(NUM_TASKS), 2)
    chrom[i], chrom[j] = chrom[j], chrom[i]
    return chrom

def genetic_algorithm():
    population = initial_population[:]

    for gen in range(1, GENS + 1):
        fitnesses = [fitness(c) for c in population]
        new_pop = []

        while len(new_pop) < POP_SIZE:
            p1 = roulette_selection(population, fitnesses)
            p2 = roulette_selection(population, fitnesses)

            if random.random() < 0.8:
                c1, c2 = one_point_crossover(p1, p2)
            else:
                c1, c2 = p1[:], p2[:]

            if random.random() < 0.2:
                c1 = mutate(c1)
            if random.random() < 0.2:
                c2 = mutate(c2)

            new_pop.extend([c1, c2])

        population = new_pop[:POP_SIZE]

        if gen % 5 == 0 or gen == GENS:
            best = max(population, key=fitness)
            print(f"🔁 Generation {gen}: Best = {best}, Cost = {-fitness(best)}")

    best_final = max(population, key=fitness)
    return best_final, -fitness(best_final)

if __name__ == "__main__":
    solution, cost = genetic_algorithm()
    print("\nFinal Best Solution:")
    print(f"Assignment (facility index per task): {solution}")
    print(f"Total Production Cost: {cost}")
