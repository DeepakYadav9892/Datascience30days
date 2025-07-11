import random

# 🎯 TARGET: We want a binary string like "111111"
TARGET = "111111"
GENE_LENGTH = len(TARGET)      # Number of bits
POPULATION_SIZE = 6            # Number of individuals per generation
MAX_GENERATIONS = 100          # Maximum iterations allowed

# ✅ Generate a random binary string
def create_individual():
    return ''.join(random.choice(['0', '1']) for _ in range(GENE_LENGTH))

# ✅ Calculate fitness: How many bits match the target
def calculate_fitness(individual):
    return sum(individual[i] == TARGET[i] for i in range(GENE_LENGTH))

# ✅ Select top 2 fittest individuals
def select_parents(population):
    return sorted(population, key=calculate_fitness, reverse=True)[:2]

# ✅ Crossover: Mix parts of two parents to create a child
def crossover(parent1, parent2):
    point = random.randint(1, GENE_LENGTH - 1)
    return parent1[:point] + parent2[point:]

# ✅ Mutation: Randomly flip one bit in the child
def mutate(individual):
    index = random.randint(0, GENE_LENGTH - 1)
    mutated = list(individual)
    mutated[index] = '1' if mutated[index] == '0' else '0'
    return ''.join(mutated)

# ✅ Main Genetic Algorithm
def genetic_algorithm():
    # Step 1: Initial random population
    population = [create_individual() for _ in range(POPULATION_SIZE)]

    for generation in range(MAX_GENERATIONS):
        # Step 2: Evaluate fitness
        population = sorted(population, key=calculate_fitness, reverse=True)
        best = population[0]

        # Step 3: Show best solution
        print(f"Generation {generation}: {best} | Fitness: {calculate_fitness(best)}")

        # Step 4: Check if target reached
        if best == TARGET:
            print("🎉 Target matched! Solution found!")
            return best

        # Step 5: Select best 2 parents
        parent1, parent2 = select_parents(population)

        # Step 6: Create new generation
        new_population = []
        for _ in range(POPULATION_SIZE):
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    print("❌ Maximum generations reached. No perfect match found.")
    return population[0]

# ✅ Run it
final_result = genetic_algorithm()
print("\nFinal Result:", final_result)
