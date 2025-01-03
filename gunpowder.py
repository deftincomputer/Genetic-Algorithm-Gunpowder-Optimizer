import random



def explosive_power(combination):
    potassium_nitrate, sulfur, charcoal = combination
    return (1.50 * potassium_nitrate) +  (0.60 * sulfur) + (0.68 * charcoal)


def generate_random_combination():
    potassium_nitrate = random.randrange(1, 100)
    sulfur = random.randrange(0, 100 - potassium_nitrate)
    charcoal = 100 - (potassium_nitrate + sulfur)
    return {"Potassium Nitrate": potassium_nitrate, "Sulfur": sulfur, "Charcoal": charcoal}


def genetic_algorithm():
    population_size = 100000
    generations = 100


    population = [generate_random_combination() for _ in range(population_size)]

    for _ in range(generations):

        

        fitness_scores = [explosive_power(combination.values()) for combination in population]


        parents = random.choices(population, weights=fitness_scores, k=2)


        children = {key: (parents[0][key] + parents[1][key]) / 2 for key in parents[0]}


        population[random.randrange(population_size)] = children


    best_combination = max(population, key=lambda x: explosive_power(x.values()))
    best_explosive_power = explosive_power(best_combination.values())
    return best_combination, best_explosive_power

best_combination, best_explosive_power = genetic_algorithm()
print("Best Mix:\n")
for material, percentage in best_combination.items():
    print(material + ":", percentage)
print("\nEnergey:", best_explosive_power)

