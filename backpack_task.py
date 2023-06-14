import random

items = [
 ("Карта", 9, 150),
 ("Компас", 13, 35),
 ("Вода", 153, 200),
 ("Сэндвич", 50, 160),
 ("Глюкоза", 15, 60),
 ("Кружка", 68, 45),
 ("Банан", 27, 60),
 ("Яблоко", 39, 40),
 ("Сыр", 23, 30),
 ("Пиво", 52, 10),
 ("Крем от загара", 11, 70),
 ("Камера", 32, 30),
 ("Футболка", 24, 15),
 ("Брюки", 48, 10),
 ("Зонтик", 73, 40),
 ("Непромокаемые штаны", 42, 70),
 ("Непромокаемый плащ", 43, 75),
 ("Бумажник", 22, 80),
 ("Солнечные очки", 7, 20),
 ("Полотенце", 18, 12),
 ("Носки", 4, 50),
 ("Книга", 30, 10),
]

population_size = 100
generations = 100
crossover_rate = 0.8
mutation_rate = 0.2
max_weight = 400

def generate_random_backpack():
    return [random.randint(0, 1) for _ in range(len(items))]

def evaluate_backpack(backpack):
    total_weight = 0
    total_value = 0
    for i in range(len(backpack)):
        if backpack[i] == 1:
            total_weight += items[i][1]
            total_value += items[i][2]
    if total_weight > max_weight:
        total_value = 0
    return total_value

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(backpack):
    mutation_point = random.randint(0, len(backpack) - 1)
    backpack[mutation_point] = 1 - backpack[mutation_point]
    return backpack

def select_parent(population):
    total_fitness = sum(evaluate_backpack(backpack) for backpack in population)
    rand_value = random.uniform(0, total_fitness)
    current_sum = 0
    for backpack in population:
        current_sum += evaluate_backpack(backpack)
        if current_sum >= rand_value:
            return backpack

population = [generate_random_backpack() for _ in range(population_size)]

for _ in range(generations):
    new_population = []
    for _ in range(population_size // 2):
        parent1 = select_parent(population)
        parent2 = select_parent(population)
        if random.random() < crossover_rate:
            child1, child2 = crossover(parent1, parent2)
        else:
            child1, child2 = parent1, parent2
        if random.random() < mutation_rate:
            child1 = mutate(child1)
        if random.random() < mutation_rate:
            child2 = mutate(child2)
        new_population.append(child1)
        new_population.append(child2)
    population = new_population

best_backpack = max(population, key=evaluate_backpack)

print("Selected items:")
for i in range(len(best_backpack)):
    if best_backpack[i] == 1:
        print(items[i][0])
print("Total:", evaluate_backpack(best_backpack))
