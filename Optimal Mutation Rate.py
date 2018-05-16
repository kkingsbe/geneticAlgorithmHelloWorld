import helloWorldGA,time
from twilio.rest import Client
import matplotlib.pyplot as plt
mutationRates = [0,100]
rates = []
times = []
numTimes = 1

for rate in range(mutationRates[0],mutationRates[1]):
    x = 0
    tempGenerations = []

    while x < numTimes:
        startTime = time.time()
        generations = helloWorldGA.main(rate,100)
        endTime = time.time()
        Time = endTime - startTime
        print("With a mutation rate of " + str(rate) + " it took " + str(generations) + " generations and "+ str(Time) + " seconds")
        tempGenerations.append(generations)
        x += 1

    meanGenerations = sum(tempGenerations) / len(tempGenerations)

    rates.append(rate)
    times.append(meanGenerations)

x = rates
y = meanGenerations

plt.plot(x, y, label='Generations to create "Hello World"', color = 'b')

plt.xlabel('Mutation Rate')
plt.ylabel;('Generations to evolve to print "Hello World"')
plt.title('How mutation rate effects evolution')
plt.legend()
plt.show()

