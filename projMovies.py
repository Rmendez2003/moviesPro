#Rafael Mendez
#projMovies FINAL
#05/02/2022


#Bubble Sort Algorith that I will use later
def bubbleSort(theIndexList,theDataList):
    
    for n in range(0,len(theIndexList)): 
        temp = 0
        for i in range(1, len(theIndexList)):
            temp = theIndexList[i]
           
	    # comparison
            if theDataList[theIndexList[i]] <= theDataList[theIndexList[i-1]]:
	        # swap
                theIndexList[i] = theIndexList[i-1]
                theIndexList[i-1] = temp
                
    return theIndexList 
    


#Funtion that will open file and ensure that user is inputting a valid file
def checkFile():
    goodFile = False
    #Will ask user for input of file to search for data
    while goodFile == False:
        try:
            fileName = input('Please enter a file name: ')
            inFile = open(fileName, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name try again...")
    return inFile


#Funtion that will separate data into lists from the main file containing the data.
def getData():
    inFile = checkFile()
    #Creating empty lists that will store data
    titleList = []
    genreList = []
    directorList = []
    yearList = []
    runtimeList = []
    revenueList = []
    #Calling Function that will check that user input file name is valid
    inFile.readline()
    
    for line in inFile:
        line = line.strip()
        title, genre, director, year, runTime, revenue = line.split(',')
        titleList.append(title)
        genreList.append(genre)
        directorList.append(director)
        yearList.append(int(year))
        runtimeList.append(int(runTime))
        revenueList.append(float(revenue))

  

    inFile.close()
    return titleList, genreList, directorList, yearList,runtimeList, revenueList

#Function that will get the user's chice from the menu with exception handling
def getChoice():
    goodChoice = False
    # This function displays the menu of choices for the user
    # It reads in the user's choice and returns it as an integer
    print("")
    print("Please choose one of the following options:")
    print("1 -- Find all films made by a specified director")
    print("2 -- Find the highest grossing film made in a specific year")
    print("3 -- Find all films made in a given year range in a specified genre")
    print("4 -- Search for a film by title")
    print("5 -- Find average runtime of films with higher revenue than specified value")
    print("6 -- Sort all lists by revenue and write the results to a new file")
    print("7 -- Quit")
    #Exception Handling
    while goodChoice == False:
        try:
            choice = int(input("Choice ==> "))
            if 7 < choice or choice < 1:
                print("Choice must be between 1 and 7")
                goodChoice = False    
            else:
                goodChoice = True
        except ValueError:
            print("Invalid entry - Try again")        
    print("")
    return choice


#Function that willl allow fpr finding of film by inputting the director's name
def findByDirector(directorList):
    directorIndexList =[]
    goodName = False
    #Conditional to check if user input a valid name
    #Exception Handling
    while goodName == False:
        dirName = input("Enter director: ")
        if dirName in directorList:
            goodName = True
        elif dirName not in directorList:
            print("Invalid entry - Try again")
    for i in range (len(directorList)):
        if directorList[i] == dirName:
            directorIndexList.append(i)
    return directorIndexList

#Function for when user wants to find highest grossing film in a specific year
def highestGross(yearList,revenueList ):
    grossYearList = []
    finalGrossYear = []
    highestGross = 0
    goodYear = False
    #Checking for valid input
    #Exception Handling
    while goodYear == False:
        try:
            yearNum = int(input("Enter year: "))
            if yearNum < 2006 or yearNum > 2016:
                print("Year out of range, must be between 2006 and 2016")
            else:
                goodYear = True
        except ValueError:
            print("Invalid entry - Try again")
    for i in range(len(yearList)):
        if yearList[i] == yearNum:
            grossYearList.append(i)
    for t in range(len(grossYearList)):
        if revenueList[grossYearList[t]] > highestGross:
            highestGross = grossYearList[t] 
    finalGrossYear.append(highestGross)
    return (finalGrossYear)

#Function to check validity of year input
#Exception Handling Function
def checkYear(yearStr):
        goodYear = False
        while goodYear == False:
            try:
                yearNum = int(input(yearStr))
                if yearNum< 2006 or yearNum > 2016:
                    print("Year out of range, must be between 2006 and 2016")
                else:
                    goodYear = True
            except (ValueError):
                print("Invalid entry - Try again")
        return yearNum
#Function to find all films in a given year range by a specified genre
def yearGen(yearList,genreList):
    rangeGenreList = []
    finalRangeGenreList = []
    goodGenre = False
    print("Enter year range to search(oldest year first)")
    year1 = 2
    year2 = 1
    while year2<year1:
        
        yearStr = "Year1: "
        year1 = checkYear(yearStr)
        yearNum2 = "Year2: "
        year2 = checkYear(yearNum2)
        if year2 < year1:
            print("Second year should be after first year - try again")
    #Loop that will create a list of all movies within the user innputted year period
    for r in range(len(yearList)):
        if yearList[r] >= year1 and yearList[r]<= year2:
            rangeGenreList.append(r)
       
    #Asking for user input on what genre they would like
    while goodGenre == False:
        try:
            yearGenre = input("Enter genre: ")
            if yearGenre not in genreList:
                print("Invalid entry - Try again")
            else:
                goodGenre = True
        except ValueError:
            print("Invalid Entry")
    #Loop will trverse the rangeGenreList to check which movies have the inputted Genre
    o = 0
    for o in range(len(rangeGenreList)):
        if yearGenre in genreList[rangeGenreList[o]]:
            finalRangeGenreList.append(rangeGenreList[o])
            
    return (finalRangeGenreList)

#Binary search function
def binarySearch(titleList,userTitle):
    # left side of list    
    left = 0    
    # right side of the list                
    right = len(titleList) - 1        
    found = 0

    while right >= left and found == 0:
        # find the middle of the list
        m = (left + right) // 2
        if titleList[m] == userTitle:
            found = 1
        elif titleList[m]<userTitle:
            left = m + 1
        else: 
            right = m-1
    if found == 0:
        return ""
    else:
        return m
    
#Function that will find a movie by user inputted name of movie
def findByTitle(titleList):
    titleIndexList = []
    userTitle = input("Enter title: ")
    movieTitleIndex = binarySearch(titleList,userTitle)
    titleIndexList.append(movieTitleIndex)  
    return titleIndexList

#Function that will find film wth higher revenue than the inputted one
def findAvgRunTime(revenueList,runtimeList):
    totalMinLength = 0
    totalMinutes = 0
    goodT = False
    while goodT == False:
        try:
            threshhold = int(input("Enter revenue limit (millions): $"))
            goodT = True
        except ValueError:
            print("Invalid Entry")
        
                    
    for i in range(len(revenueList)):
        if float(revenueList[i]) > threshhold:
            totalMinLength += 1
            totalMinutes = totalMinutes + float(runtimeList[i])
    
    if totalMinLength == 0:
        print("No films have revenue higher than ${:.2f}".format(threshhold),"million.")
    else:
        averageMinutes = round(float(totalMinutes/totalMinLength),2)
        ####ASK HOW TO ROUND THRESHOLD TO TWO DECIMAL PLACES###
        print ("The average runtime for films with revenue higher than ${:.2f}".format(threshhold), ' million is ',  averageMinutes, ' minutes.')

    return

#Function to sort movies by revenue and then write them to a new file
def sortByRevenue(revenueList):
    unsortedIndex =[]
    sortedIndex = []
    for i in range(len(revenueList)):
        unsortedIndex.append(i)
    #Using Bubble sort algorith to sort the revenue
    sortedIndex = bubbleSort(unsortedIndex, revenueList)
    
    return sortedIndex

#Print Function
def printResult(indexList, titleList, genreList, directorList, yearList,runtimeList, revenueList):
    print("")
    if(len(indexList)) == 1:
        print("The film that meets your criteria is:")
        print("")
        print("TITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12))
        
    elif(len(indexList))>1:
        print("The films that meet your criteria are:")
        print("")
        print("TITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12))
        
    for r in range(len(indexList)):
        i = int(indexList[r])
        print(titleList[i].ljust(45), genreList[i].ljust(35), directorList[i].ljust(24), str(yearList[i]).ljust(8), str(runtimeList[i]).ljust(8), ("$"+str(revenueList[i])).rjust(12))
    return
   
    
# Function to get the new file created with the correct information
def printMoviesFile(sortByRevenueIndex, titleList, genreList, directorList, yearList,runtimeList, revenueList):
    outName = "movies-sorted-rev.csv"
    outFile = open(outName, 'w')
    for i in range(len(sortByRevenueIndex)):
        outFile.write(titleList[sortByRevenueIndex[i]] + "," + genreList[sortByRevenueIndex[i]] + "," + directorList[sortByRevenueIndex[i]] + "," + str(yearList[sortByRevenueIndex[i]]) + "," + str(runtimeList[sortByRevenueIndex[i]]) + "," + str(revenueList[sortByRevenueIndex[i]]) + '\n')
    outFile.close()
    return      
    

def main():
    titleList, genreList, directorList, yearList,runtimeList, revenueList = getData()
    choice = getChoice()
    while choice != 7:
            if choice == 1:
                dirIndex = findByDirector(directorList)
                printResult(dirIndex, titleList, genreList, directorList, yearList,runtimeList, revenueList)
                choice = getChoice()
                
            elif choice == 2:
                highestGrossIndex = highestGross(yearList, revenueList)
                printResult(highestGrossIndex, titleList, genreList, directorList, yearList,runtimeList, revenueList)
                choice = getChoice()
                
            elif choice == 3:
                yearGenIndex = yearGen(yearList,genreList)
                printResult(yearGenIndex, titleList, genreList, directorList, yearList,runtimeList, revenueList)
                choice = getChoice()
                
            elif choice == 4:
                findByTitleIndex = findByTitle(titleList)
                if (findByTitleIndex[0]) == "":
                    print("")
                    print("No such film exists.")
                    choice = getChoice()
                else:
                    printResult(findByTitleIndex, titleList, genreList, directorList, yearList,runtimeList, revenueList)
                    choice = getChoice()
                    
            elif choice == 5:
                test = findAvgRunTime(revenueList,runtimeList)
                choice = getChoice()
            elif choice == 6:
                sortByRevenueIndex = sortByRevenue(revenueList)
                printMoviesFile(sortByRevenueIndex, titleList, genreList, directorList, yearList,runtimeList, revenueList)
                print("")
                print("Sorted data has been written to the file: movies-sorted-rev.csv.")
                choice = getChoice()
    print("Good-bye")
   
