import random, math
import numpy as np
import matplotlib.pyplot as plt

# def randomDice(trial): #random dice value
#     dice = np.random.random_integers(1, 6, trial)
#     return dice
#
# def plotHisto(array, title, xlabel, step): #plots histogram
#     plt.hist(array, bins=np.arange(min(array), max(array) + 2, step), align="mid", color="orange")
#
#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel("frequency")
#
#     plt.show()
#
# x = [1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8]
# plotHisto(x, "histogram", "values", 1)

def plotBar(array, objects, y_pos, title, case): #plots bar graph
    plt.bar(y_pos, array, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)  # matches x labels to the matching array indices
    plt.ylabel('frequency')
    plt.title(title)

    if case is True: #only for deal or no deal simulation
        pos = list(range(0, len(array)))  # x positions of text
        for q in range(0, len(array)): #repeats number of values in array times
            plt.text(pos[q], array[q] + 4, str(round(array[q])), horizontalalignment="center")  # plots values of bars above the corresponding bars

    plt.show()

# performance = [10,8,6,4,2,1]
# objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
# y_pos = np.arange(len(objects)) #returns an array with evenly spaced elements ([0 1 2 3 4 5])
# print(y_pos)
#
# plotBar(performance, objects, y_pos, "bar graph", "values")
#
#
# def plotPoints(x, y, ticks, title, xlabel):
#     plt.plot(x, y, 'ro')
#     plt.xticks(np.arange(0, ticks, 100))
#
#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel("y value")
#     plt.show()
#
# plotPoints([1, 2, 3, 4], [1, 2, 3, 4], 10, "points", "values")
#
# def plotPie(x, labels, title):
#     colors = ["red", "orange", "yellow", "green", "blue", "purple", "indigo", "pink"]
#     plt.pie(x, explode=None, labels=labels, colors=colors)
#     plt.title(title)
#     plt.show()
#
# plotPie([10, 20, 30, 40], ["a", "b", "c", "d"], "pie chart")

#start here


number_of_trials = 100000

def monty_hall(trials):

    results = [0, 0, 0, 0] #results from the games (switch & win, switch & lost, don't switch & win, don't switch & lose)

    for z in range(trials):

        array = [1, 2, 3]  # all the doors
        prize = random.randint(1, 3)  # door with prize
        user = random.randint(1, 3)  # user choice

        array.remove(prize)  # removes the prize from all the doors so two doors are left

        if prize != user:  # if the user has the same door as the prize, then it has already been removed and no need to remove it again
            array.remove(user)  # removes the user door so only one door is left in array

        shownDoor = array[0]  # this is the door that has nothing behind it and is shown to the user

        switch = random.randint(0, 100)

        if switch < 50:#switch
            user = 6 - user - shownDoor #since 1+2+3 = 6, then the door the user will switch with is 6 - its door - shownDoor(revealed) which equals the remaining door


        switch = switch < 50

        if switch and prize == user:
            results[0] += 1
        elif switch and prize != user:
            results[1] += 1
        elif not switch and prize == user:
            results[2] += 1
        elif not switch and prize != user:
            results[3] += 1

    objects = ("Won and Switch", "Lost and Switch", "Won and Kept", "Lost and Kept")
    y_pos = np.arange(len(objects))
    plotBar(results, objects, y_pos, "Monty Hall", True)



monty_hall(number_of_trials)























