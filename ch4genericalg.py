import random
import string

#below is the correct format 
# generate initial population
def generate_population(psize, indiv_size):
    #let population be an empty string
    population = []
    #for individual in range 0 to population_size in here known as psize
    for i in range(psize):
        #let current_individual be an empty array
        current_indiv = []
        #for gene in range 0 to individual_size known as indiv_size
        for g in range(indiv_size):
            #let random_gene be 0 or 1 randomly
            random_gene = random.randint(0, 1)
            #append random_gene to current_individual 
            current_indiv.append(random_gene)
        #append current_individual to population
        population.append(current_indiv)
    return population

#measuring fitness of individuals in a population
def calculate_individual_fitness(individual, knapsack_items, knapsack_max_weight):
    total_weight = 0
    total_value = 0
    # for gene_index in range 0 to length of the individual
    for gene_index in range(len(individual)):
        #let current bit equal individual gene_index
        current_bit = individual[gene_index]
        if current_bit == 1:
            #add weight of kanpsack_items [gene_iindex] to total_weight
            total_weight += knapsack_items[gene_index]['weight']
            #add value of knapsack_items[gene_index] to total_value
            total_value += knapsack_items[gene_index]['value']

        elif total_weight > knapsack_max_weight:
            #return 0 since it exceeds the weight constraint  
            return 0
    #return total_value as individual fitness
    return total_value

# SLECTING PARENTS BASED ON THEIR FITNESS
def set_probabilities_of_population(population, knapsack_items, knapsack_max_weight):
    # Calculate fitness for each individual in the population
    fitnesses = [calculate_individual_fitness(individual, knapsack_items, knapsack_max_weight) for individual in population]
    # Calculate total fitness of the population
    total_fitness = sum(fitnesses)
    # Calculate probability of selection for each individual
    probabilities_of_selection = [fitness / total_fitness for fitness in fitnesses]
    
    return probabilities_of_selection

def roulette_wheel_selection(population, number_of_selections, knapsack_items, knapsack_max_weight):
    probabilities = set_probabilities_of_population(population, knapsack_items, knapsack_max_weight)
    selected = []
    for _ in range(number_of_selections):
        spin = random.uniform(0, 1)
        total = 0
        for i, probability in enumerate(probabilities):
            total += probability
            if spin <= total:
                selected.append(population[i])
                break
    return selected

#REPRODUCING INDIVIDUALS FROM PARENTS
def one_point_crossOver(parentA, parentB, xover_point):
    # Initialize an empty list to store the children
    children = []

    # Generate the first child by taking the first xover_point genes from parentA 
    # and the genes from position xover_point till the end from parentB
    child_one = parentA[:xover_point] + parentB[xover_point:]
    # Append the first child to the children list
    children.append(child_one)

    # Generate the second child by taking the first xover_point genes from parentB 
    # and the genes from position xover_point till the end from parentA
    child_two = parentB[:xover_point] + parentA[xover_point:]
    # Append the second child to the children list
    children.append(child_two)

    # Return the list of children
    return children

def mutate_individual(individual, chromosome_length):
    # Choose a random index in the individual's genes
    random_index = random.randint(0, chromosome_length-1)
    # If the gene at the random_index is 1, flip it to 0
    if individual[random_index] == 1:
        individual[random_index] = 0
    # Otherwise, flip it to 1
    else:
        individual[random_index] = 1
    # Return the mutated individual
    return individual

  
#     return best_global_fitness
def calculate_population_fitness(population, knapsack_items, knapsack_max_weight):
    # Calculate the fitness of the population
    fitnesses = [calculate_individual_fitness(individual, knapsack_items, knapsack_max_weight) for individual in population]
    # Return the highest fitness found
    return max(fitnesses)

def reproduce_children(chosen, indiv_size):
    # Create empty list for children
    children = []
    # For each pair of parents
    for i in range(0, len(chosen), 2):
        # Select a random crossover point
        xover_point = random.randint(1, indiv_size - 1)
        # Create children
        child_pair = one_point_crossOver(chosen[i], chosen[i+1], xover_point)
        children.extend(child_pair)
    return children

def mutate_children(children, chromosome_length):
    # Mutate each child
    for i in range(len(children)):
        children[i] = mutate_individual(children[i], chromosome_length)
    return children

def merge_population_and_children(population, children):
    # Combine the population and children
    return population + children

def run_ga(psize, number_of_generations, knapsack_items, knapsack_max_weight, indiv_size):
    # Initialize the best global fitness
    best_global_fitness = 0
    # Generate the initial population
    global_population = generate_population(psize, indiv_size)

    # For each generation
    for generation in range(number_of_generations):
        # Calculate the fitness of the current population
        current_best_fitness = calculate_population_fitness(global_population, knapsack_items, knapsack_max_weight)
        # If the current fitness is better than the best global fitness, update the best global fitness
        if current_best_fitness > best_global_fitness:
            best_global_fitness = current_best_fitness
        # Select individuals for reproduction
        the_chosen = roulette_wheel_selection(global_population, psize, knapsack_items, knapsack_max_weight)
        # Create children from the chosen individuals
        the_children = reproduce_children(the_chosen, indiv_size)
        # Mutate the children
        the_children = mutate_children(the_children, indiv_size)
        # Merge the population with the new children
        global_population = merge_population_and_children(global_population, the_children)
        
    # After all generations have passed, return the best fitness achieved
    return best_global_fitness


def main():
    psize = 50
    indiv_size = 2
    knapsack_max_weight = 60
    number_of_generations = 500  # you can adjust this value to your needs

    knapsack_items = [{'weight': 10, 'value': 60}, {'weight': 20, 'value': 100}, 
                      {'weight': 30, 'value': 120}, {'weight': 40, 'value': 130}]


    # Running the Genetic Algorithm
    best_global_fitness = run_ga(psize, number_of_generations, knapsack_items, knapsack_max_weight, indiv_size)
    print(f"The best global fitness achieved after {number_of_generations} generations is: {best_global_fitness}")


if __name__ == "__main__":
    main()



