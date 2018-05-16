# Create Starting pop
# Evualte fitness (correct chars / total chars * 100)
# Keep Most Fit
# Have Most Fit Reproduce
# Mutatations
# GOTO Step 2

# TODO: Print the alleles that were passed on

import random,time

startTime = time.time()
targetString = "Hello World"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,./<>?`~!@#$%^&*()_+|-=\* "
startingPopulation = []
startingPopSize = 100  # The size of the starting popoulation
newGen = []
randomlyGenerated = []
mutationRate = 36 #Mutation rate in percent

def randChar():
    return letters[random.randint(0,len(letters)-1)]

def generatePop(size):  # Generates a population of size
    length = len(targetString)
    pop = []
    characters = len(letters) - 1
    for i in range(size):  # Generates a new individual until population = size
        tempList = ""
        for x in range(length):
            tempList += (letters[random.randint(0, characters)])
        pop.append(tempList)
    return pop


def evalfitness(population):  # Evaluates the fittness of list population
    # print(population)
    fitnessList = []  # Resets fittnessList
    for individual in population:  # Iterates through each individual in the population list
        simChars = 0

        for x in range(len(individual)):
            if individual[x] == targetString[x]:
                simChars += 1

        fitness = simChars / len(
            individual
        ) * 100  # Calculates the fittness by dividing the number of similar characters by the length of the individual and multiplying by 100 to convert to a percentage
        fitnessList.append(int(fitness))
    return fitnessList


def findMostFit(population, fitnessList):  # Finds the most fit individuals in the population
    intermediatePop = []
    randomlyGenerated = []
    elite = ""
    mostFit = max(fitnessList)  # Sets variable mostFit to equal the largest fittness integer in the fittnessList
    elite = population[fitnessList.index(mostFit)]
    # print("ELITE: " + elite)
    for x in range(
            len(fitnessList)):  # Iterates through each index in the fittnessList
        if len(intermediatePop) < startingPopSize:
            if fitnessList[x] == mostFit:  # Adds the most fit individuals to an intermediate population
                intermediatePop.append(population[x])

    while len(intermediatePop) < startingPopSize:  # If the intermidiate population is smaller than the starting population, it will generate new individuals until the population reaches the same size TODO: Change this to increace efficiancy
        newIndividual = population[random.randint(0, len(population) - 1)]
        intermediatePop.append(newIndividual)
        randomlyGenerated.append(newIndividual)
    # print(randomlyGenerated)
    return intermediatePop


def breed(elite):  # Breeds new offspring from the intermidiate population
    toBreed = intermediatePop
    children = []  # Resets children list

    while len(toBreed) > 0:  # While the toBreed list contains individuals
        matingPair = toBreed[:2]  # Creates a mating pair of the first two individuals in the toBreed list
        del toBreed[:2]  # Deletes first two individuals
        offspring = ""

        for allele in range(len(matingPair[
                                    0])):  # Iterates through the indexes characters (alleles) in the first individual in the mating pair
            prob = random.randint(0, 100)  # Generates a random number
            if prob > 50:  # Expresses the allele from matingPair[0] in the offspring if the prob is > 50
                offspring += matingPair[0][allele]
            else:  # Expresses the allele from matingPair[0] in the offspring if the prob is < 50
                offspring += matingPair[1][allele]
        #print(matingPair[0] + " + " + matingPair[1] + " = " + offspring)
        for parent in toBreed[:2]:
            children.append(parent)

        children.append(offspring)  # Adds offspring to the children list

    children.append(elite)
    return children


def findElite(population):
    elite = ""
    mostFit = max(fitnessList)  # Sets variable mostFit to equal the largest fittness integer in the fittnessList
    elite = population[fitnessList.index(mostFit)]
    return elite

def mutate(population):
    tempList = []
    for individual in population:
        rand = random.randint(0,100)
        if rand <= mutationRate:
            randAllele = individual[random.randint(0,len(individual)-1)]
            mutatedIndividual = individual.replace(randAllele, randChar())
            tempList.append(mutatedIndividual)
            #print(individual + " mutated to " + mutatedIndividual)
        else:
            tempList.append(individual)
    return tempList

startingPopulation = generatePop(startingPopSize)
fitnessList = evalfitness(startingPopulation)
intermediatePop = findMostFit(startingPopulation, fitnessList)
elite = findElite(startingPopulation)

generations = 0

while targetString not in newGen:  # Main loop
    newGen = breed(elite)
    fitnessList = evalfitness(newGen)
    intermediatePop = findMostFit(newGen, fitnessList)
    # x = random.randint(0,len(newGen)-1)
    x = fitnessList.index(max(fitnessList))
    elite = findElite(newGen)
    intermediatePop = mutate(intermediatePop)
    #print(newGen)
    print(newGen[x] + " | " + str(fitnessList[x]))
    generations += 1
endTime = time.time()
elapsedTime = endTime - startTime
# print(newGen)
# print(fitnessList)
print("Took " + str(generations) + " generations and " + str(elapsedTime) + " seconds")

# print(startingPopulation)
# print(fitnessList)
# print(max(fitnessList))
# print(newGen)