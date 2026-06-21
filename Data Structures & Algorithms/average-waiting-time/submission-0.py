class Solution:
    def averageWaitingTime(self, customers):

        currentTime = 0
        totalWait = 0

        for arrival, cookTime in customers:

            currentTime = max(currentTime, arrival)

            currentTime += cookTime

            totalWait += currentTime - arrival

        return totalWait / len(customers)