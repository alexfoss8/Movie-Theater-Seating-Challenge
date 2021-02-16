"""
Alex Foss - Movie Theater Seating Challenge 
""" 
import sys
import os
from collections import deque
from pathlib import Path

row_num_to_letter = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J'}

class Theater:

    def __init__(self):
        self.totalPeople = 0
        self.totalGroups = 0
        self.queue = deque()
        self.res_ID_to_group_size = {}
        self.seatsRemaining = [20 for x in range(10)]
        self.groupSizesInRow = [[] for x in range(10)]
        self.resIDInRow = [[] for x in range(10)]
        self.tooBig = None
        self.assignments = {}

    def fill_five_rows(self, rowRanking):
        if len(self.queue) > 0: front = self.queue[0]
        for i in range(5):
            if len(self.queue) == 0: return False
            key = self.queue[0]
            value = self.res_ID_to_group_size[key]
            rowNum = rowRanking[i]
            if (self.seatsRemaining[rowNum] >= value):
                self.seatsRemaining[rowNum] -= (value + 3)
                self.resIDInRow[rowNum].append(key)
                self.groupSizesInRow[rowNum].append(value)
                self.queue.popleft()
                self.totalGroups -= 1
                self.totalPeople -= value
        # cycle queue to fill rows
        if len(self.queue) == 0: return False
        if front == self.queue[0]:
            if front == self.tooBig or len(self.queue) == 1:
                return False
            self.tooBig = front if self.tooBig == None else self.tooBig
            tempFront = self.queue.popleft()
            self.queue.append(tempFront)
        return True
    
    def asssign_seats(self):
        for i in range(10): # rows
            numPeople = 20 - self.seatsRemaining[i]
            if numPeople == 0: continue # no one in row
            # remove trailing buffer in rows
            numPeople -= 3
            index = (20  - numPeople) // 2
            row = row_num_to_letter[i]
            for j in range(len(self.groupSizesInRow[i])): # groups in row
                tempOutput = self.resIDInRow[i][j] + " "
                for k in range(self.groupSizesInRow[i][j]): # individual group
                    tempOutput += row + str(index) + ','
                    index += 1
                self.assignments[self.resIDInRow[i][j]] = tempOutput[:-1]
                index += 3 #buffer
                

def main():
    theater = Theater()
    inputFile = sys.argv[1]
    # grab input and store into map (ID -> group size) 
    with open(Path(inputFile), 'r') as text:
        splitText = text.read().replace("\n", " ").split()
        for i in range(0, len(splitText), 2):
            groupSize = int(splitText[i+1])
            theater.totalPeople += groupSize
            theater.totalGroups += 1
            theater.queue.append(splitText[i])
            theater.assignments[splitText[i]] = None
            theater.res_ID_to_group_size[splitText[i]] = groupSize
    
    
    # Fill "best" 5 rows while they have seats available
    while True: 
        if not theater.fill_five_rows([7,6,5,8,9]): break

    # Assign remaining groups to rows
    while True: 
        if not theater.fill_five_rows([4,3,2,1,0]): break
    
    # try to rearrrange rows if group cannot fit
    if len(theater.queue) > 0:  
        for i in theater.queue:
            print("Cannot Fit Group: " + i)
    
    # Assign seats per row / format output
    theater.asssign_seats()

    # create output path and print assignments
    outputFile = "output" + inputFile[5:]
    with open(Path(outputFile), 'w') as f:
        sys.stdout = f # Change the standard output to the file we created
        for value in theater.assignments.values():
            print(value)
        sys.stdout = sys.__stdout__ # change back
    print(outputFile)

if __name__ == "__main__":
    main()