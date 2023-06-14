import random

interval = (77, 140)
population_size = 40
mutation_rate = 0.01
num_generations = 10


def function(x):
    return 16 + 9*x + 33*pow(x, 2) - 2*pow(x, 3)


def generate_population():
    return [random.uniform(interval[0], interval[1]) for _ in range(population_size)]


def evaluate_fitness(individual):
    return function(individual)


def mutate(individual):
    mutated_individual = individual + \
        random.uniform(-mutation_rate, mutation_rate)
    return max(min(mutated_individual, interval[1]), interval[0])


population = generate_population()
for generation in range(num_generations):
    fitness_scores = [evaluate_fitness(individual)
                      for individual in population]

    parents = []
    for _ in range(population_size):
        tournament = random.sample(range(population_size), 5)
        winner = min(tournament, key=lambda x: fitness_scores[x])
        parents.append(population[winner])

    offspring = []
    for i in range(population_size):
        parent1 = parents[i]
        parent2 = parents[random.randint(0, population_size - 1)]
        child = (parent1 + parent2) / 2.0
        offspring.append(child)

    mutated_offspring = [mutate(child) for child in offspring]

    population = mutated_offspring

best_individual = min(population, key=lambda x: evaluate_fitness(x))

minimum_value = evaluate_fitness(best_individual)

print("Minimum:", minimum_value)
print("X:", best_individual)
