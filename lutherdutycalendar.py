#Ryan Ehrhardt
#Janurary Term 2017 Independent Study Project
#Luther College Resident Assistant Scheduler
#Take input of conflicts from a text file and from that information create a calendar that schedules people around their conflicts
import calendar
class RA:
    def __init__(self, name):
        self.name = name
    def get_conflicts(self):
        return Conflicts(self.name)


def make_conflicts():
    f = open("conflicts.txt", "r")
    # makes a dictionary for each RA
    # ex.) Ryan: 1 3 5
    C_List = []

    ########Works however if there is enter between names it produces a KeyError not sure why.
    for aline in f.readlines():
        count = -1
        temp = 0
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        values = aline.split()
        #Loop goes through file and looks for conflicts
        for conflicts in values:
            #If the conflict is a day
            if conflicts in numbers:
                C_List[count][temp].append(int(conflicts))
            else:
            #otherwise it is a name and needs to be made into a new dictionary
                C_List.append({conflicts: []})
                count = count + 1
                temp = conflicts
    return C_List


def scheduling():
    make_conflicts()
    #determine how many days are in the month from there assign points(I know a basic way to do this however eventually it'll need to do this on its own).
    #numbers pulled from current month for testing purposes
    ######POINT CODING#######
    #weekday_points = 23 *1
    #weekdays * 1

    #weekend_points = 8 * 2

    #points = weekday_points + weekend_points


    #determine a max point value for staff
    #max_points = len(RA_dict)/points
    # iterate through RA_dict and schedule people one at a time

    #######SCHEDULING#######
    C_List = [{'Ryan': [1, 3, 5]}, {'Bob': [2, 4, 8]}]
    days_remaining = []
    days_scheduled = []
    # fills list up with days of month (temp)
    for days in range(1, 32):
        days_remaining.append(days)

    Schedule_List = []
    pos = 0
    RAs = C_List[pos].keys()  # not working trying to make a list of the keys in the list.
    conflicts = C_List[pos].items()
    repeat = 0
    while len(days_remaining) != 0 and repeat < 100:

        # scheduling code goes here
        # thinking of for loop of the dictionary from there getting the conflicts of the RA and then scheduling the RA
        # only if the conflicts are seperated by seven days ideally
        for days in days_remaining:

            if days not in conflicts:
                if key not in Schedule_List:
                    # if the RA isn't in the Schedule list already  add them
                    Schedule_List.append({key: int(days)})
                else:
                    Schedule_List[pos][name].append(int(days))
            else:
                if pos + 1 <= len(C_List):  # double check to see
                    pos = pos + 1
                else:
                    pos = 0
                    repeat = repeat + 1

    if len(days_remaining) != 0:
        print("There were too many conflicts for this month!")
        ######Scheduling code for worst case here
    else:
        print(Schedule_List)
        # Schedule the RA if that isn't an issue
        # testchanges










def make_calendar:
    #use information from scheduling to then make output of a calendar.. may or may not be necessary.


def main():

