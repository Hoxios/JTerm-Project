import datetime
import calendar
import random

def scheduling(raConflicts, year=2017, month=5):
    #this will take conflicts eventually
    daysInMonth = calendar.monthrange(2017,5)[1]
    days = [0,1,2,3,4,5,6]
    weekDays = [0,1,2,3,6]
    startDay = calendar.monthrange(year,month)[0]
    raNames = []
    schedule = {}
    conflictchecker = []
    pos = 0
    for key in raConflicts:
        raNames.append(key)
        schedule[key]=[]
    for day in range(1,daysInMonth-12):
        #checks to shcedule one RA vs two depending on weekday/weekend

        if startDay in weekDays:
            #checks to see if there is a conflict if there isn't we schedule
            if day not in raConflicts[raNames[pos]]:

                schedule[raNames[pos]].append(day)
                #next RA checks to see if we are at the end of the list of their names
                #uses accumulator pattern.
                if pos == len(raNames)-1:
                    random.shuffle(raNames)
                    pos = 0
                else:
                    pos = pos+1
                if startDay == 6:
                    startDay = 0
                else:
                    startDay = startDay+1
            #we have a conflict!  it adds the ra's name to a list of conflicts to keep track of ra's with conflicts on that date
            else:
                conflictchecker.append(raNames[pos])
                if pos == len(raNames)-1:
                    random.shuffle(raNames)
                    pos = 0
                else:
                    pos = pos+1
                while len(conflictchecker) != len(raNames):
                    if day not in raConflicts[raNames[pos]]:
                        schedule[raNames[pos]].append(day)
                        #next RA checks to see if we are at the end of the list of their names
                        #uses accumulator pattern.
                        if pos == len(raNames)-1:
                            random.shuffle(raNames)
                            pos = 0
                        else:
                            pos = pos+1
                        if startDay == 6:
                            startDay = 0
                        else:
                            startDay = startDay+1
                        #refresh the list to save for conflicts on a different day
                        conflictchecker = []
                        break
                    else:
                        conflictchecker.append(raNames[pos])
                        if pos == len(raNames)-1:
                            random.shuffle(raNames)
                            pos = 0
                        else:
                            pos = pos+1
                        continue
                #worst case scenario where everyone remaining has a conflict on this day we schedule someone at random and move on.
                if len(conflictchecker) == len(raNames):
                    random.shuffle(raNames)
                    schedule[raNames[pos]].append(day)
                    if pos == len(raNames)-1:
                        random.shuffle(raNames)
                        pos = 0
                    else:
                        pos = pos+1
                    if startDay == 6:
                        startDay = 0
                    else:
                        startDay = startDay+1
                    conflictchecker = []


        #we have a weekend so with most staff's we schedule 2
        else:
            if day not in raConflicts[raNames[pos]]:
                schedule[raNames[pos]].append(day)
                #next RA checks to see if we are at the end of the list of their names
                #uses accumulator pattern.
                if pos == len(raNames)-1:
                    random.shuffle(raNames)
                    pos = 0
                else:
                    pos = pos + 1
                if day not in raConflicts[raNames[pos]]:
                    schedule[raNames[pos]].append(day)
                    if pos == len(raNames)-1:
                        random.shuffle(raNames)
                        pos = 0
                    else:
                        pos = pos + 1
                    if startDay == 6:
                        startDay= 0
                    else:
                        startDay = startDay+1
                else:
                    conflictchecker.append(raNames[pos])
                    if pos == len(raNames)-1:
                        random.shuffle(raNames)
                        pos = 0
                    else:
                        pos = pos + 1
                    while len(conflictchecker) != len(raNames):
                        if day not in raConflicts[raNames[pos]]:
                            schedule[raNames[pos]].append(day)

                            if pos == len(raNames)-1:
                                random.shuffle(raNames)
                                pos = 0
                            else:
                                pos = pos+1

                            if startDay == 6:
                                startDay= 0
                            else:
                                startDay = startDay+1
                            conflictchecker = []
                            break
                        else:
                            conflictchecker.append(raNames[pos])
                            if pos == len(raNames) - 1:
                                random.shuffle(raNames)
                                pos = 0
                            else:
                                pos = pos + 1
                            continue
                    if len(conflictchecker) == len(raNames):
                        random.shuffle(raNames)
                        schedule[raNames[pos]].append(day)
                        if pos == len(raNames)-1:
                            random.shuffle(raNames)
                            pos = 0
                        else:
                            pos = pos+1
                        if startDay == 6:
                            startDay = 0
                        else:
                            startDay = startDay+1
                        conflictchecker = []

            else:
                conflictchecker.append(raNames[pos])
                if pos == len(raNames)-1:
                    random.shuffle(raNames)
                    pos = 0
                else:
                    pos = pos+1
                while len(conflictchecker) != len(raNames):
                    if day not in raConflicts[raNames[pos]]:
                        schedule[raNames[pos]].append(day)

                        if pos == len(raNames)-1:
                            random.shuffle(raNames)
                            pos = 0
                        else:
                            pos = pos+1

                        if startDay == 6:
                            startDay= 0
                        else:
                            startDay = startDay+1
                        conflictchecker = []
                        break
                    else:
                        conflictchecker.append(raNames[pos])
                        if pos == len(raNames) - 1:
                            random.shuffle(raNames)
                            pos = 0
                        else:
                            pos = pos + 1
                        continue
                if len(conflictchecker) == len(raNames):
                    random.shuffle(raNames)
                    schedule[raNames[pos]].append(day)
                    if pos == len(raNames)-1:
                        random.shuffle(raNames)
                        pos = 0
                    else:
                        pos = pos+1
                    if startDay == 6:
                        startDay = 0
                    else:
                        startDay = startDay+1
                    conflictchecker = []
    print(schedule)
    return schedule

scheduling({'Ryan': [2,3,7,9,10,14],'Hannah':[4,5,6,7,14],'Grace': [8,15,16,17], 'Maren': [5,6], 'Mareda': [5,7,11,14],'Katy':[],'Isaiah': [1,2,3,4,5,6], 'David': [7,9,10,14,16,17]})
