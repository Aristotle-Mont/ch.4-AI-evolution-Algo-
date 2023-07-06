# Genetic Algorithm for Knapsack Problem

This repository contains a Python implementation of a genetic algorithm to solve the Knapsack Problem. The Knapsack Problem is a classic optimization problem where a set of items with certain weights and values must be selected to maximize the total value while not exceeding a maximum weight constraint.

## Prerequisites

To run this code, make sure you have Python installed on your system. The code is written in Python 3.

## Dependencies

The code relies on the following Python libraries:
- `random`
- `string`

You can install these dependencies using pip:

```
pip install random string
```

## Usage

To use the genetic algorithm for the Knapsack Problem, follow these steps:

1. Set the parameters in the `main()` function:
   - `psize`: The population size, i.e., the number of individuals in each generation.
   - `indiv_size`: The size of each individual, i.e., the number of genes in the chromosome.
   - `knapsack_max_weight`: The maximum weight constraint for the Knapsack Problem.
   - `number_of_generations`: The number of generations for which the algorithm will run.

2. Define the `knapsack_items` list: This list contains dictionaries representing the items in the Knapsack Problem. Each dictionary should have the keys `'weight'` and `'value'` representing the weight and value of the item, respectively.

3. Run the `main()` function: This function initializes the population, performs the genetic algorithm iterations, and prints the best global fitness achieved.

You can execute the code by running the script from the command line or an integrated development environment (IDE).

```
python genetic_algorithm.py
```

## Algorithm Overview

The genetic algorithm for the Knapsack Problem follows these steps:

1. Generate an initial population of random individuals, where each gene represents the inclusion (1) or exclusion (0) of an item in the Knapsack.

2. Calculate the fitness of each individual by summing the values of the included items and checking if the total weight exceeds the maximum weight constraint.

3. Select individuals for reproduction using a roulette wheel selection method, where the probability of selection is proportional to the individual's fitness.

4. Create children from the selected individuals using one-point crossover, which combines genes from two parents to produce two offspring.

5. Mutate the children by randomly flipping a gene in their chromosomes.

6. Merge the population with the new children.

7. Repeat steps 2-6 for a specified number of generations.

8. Return the best fitness achieved after all generations.


