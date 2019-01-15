#Michelle Loven
#Created: January 12, 2019
#Last edited: January 14, 2019
#Reading from CSV document

"""Analyses of data from CSV document"""

import csv

num_trials = 0
hour_index = 0
min_index = 1

#arrays with naming information
header_arr = []
participants_arr = []

information = []        # names_arr, settimes1_arr, intertimes1_arr, settimes2_arr, intertimes2_arr

diff_time = []          #comparing the hours and min
total_per_trial = []    #total minute difference per trial

diff_time_total = []    # diff_time_total = [a[1,2],b[1,2],c[1,2],d[1,2]]


def open_file():
    """ Open file from directory.
    """
    global num_trials, header_arr, participants_arr
    with open(r'/Users/Mishka/Desktop/coding_projects/python/python_time.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        row_num = 0
        for row in spamreader:
            if row_num == 0:
                header_arr = row
                for col in row:
                    num_trials += 1
            else:
                participants_arr.append(row)
            row_num += 1
        num_trials = int((num_trials - 1)/2)
        csvfile.close()

def create_information_arr():
    """Generates an array 'information' with (titles, participant's info)
    """
    global information
    for x in range(len(header_arr)):
        information.append([])

    for participant in participants_arr:
        for x in range(len(header_arr)):
            information[x].append(participant[x])

    print("Number of participants: %d" %(len(participants_arr)))

def create_seperated_time_arr():
    """Fills arrays with seperated numbers regarding the time information:
    hours vs. minutes.
    """
    #seperated values:
    set_hours = []
    set_min = []
    inter_hours = []
    inter_min = []
    #seperating time for set time
    for x in range(num_trials):
        set_hours.append([])
        set_min.append([])
        inter_hours.append([])
        inter_min.append([])

    #seperating time for set times
    for x in range(num_trials):
        for time in information[(x*2)+1]:
            set_hours[x].append(int(time[:time.find(":")]))
            set_min[x].append(int(time[time.find(":")+1:]))

    # print("Hours: %s and Mins: %s" %(set_hours, set_min))
    #seperating time for inter times
    for x in range(num_trials):
        for time in information[(x*2)+2]:
            inter_hours[x].append(int(time[:time.find(":")]))
            inter_min[x].append(int(time[time.find(":")+1:]))

    create_time_compare_arr(set_hours,set_min,inter_hours,inter_min)
    # print("IntHours: %s and IntMins: %s" %(inter_hours, inter_min))

def create_time_compare_arr(set_hours,set_min,inter_hours,inter_min):
    """Generates array diff_time (trial,hours/min) with the differences in hours and Minutesself.
    Takes time information from set_hours,set_min,inter_hours,inter_min.
    """
    global diff_time, hour_index, min_index

    for x in range(num_trials):
        diff_time.append([[],[]])
    # diff_time = [[diff time for trial 1], [diff time for trial 2]]
    # diff_time = [[[diff_hours1],[diff_mins1]],[[diff_hours1],[diff_mins1]]]
    for x in range(num_trials):
        for num in range(len(participants_arr)):
            diff_time[x][hour_index].append(abs(set_hours[x][num] - inter_hours[x][num]))
            diff_time[x][min_index].append(abs(set_min[x][num] - inter_min[x][num]))

def create_total_time_compare():
    """Generates array diff_time_total (participant, trial) with total time
    difference for each participant.
    """
    global diff_time_total
    for participant in range(len(participants_arr)):
        diff_time_total.append([])

    for participant in range(len(participants_arr)):
        for x in range(num_trials):
            diff_time_total[participant].append([])

    for participant in range(len(participants_arr)):
        for x in range(num_trials):
            diff_time_total[participant][x] = diff_time[x][hour_index][participant]* 60 \
            + diff_time[x][min_index][participant]

def create_total_trial_compare_array():
    """Generates an array total_per_trial (trial) with the total compared
    minutes from each trial
    """
    #total time off trial One = [t1,t2]
    global total_per_trial
    for x in range(num_trials):
        total_time = 0
        for participant in diff_time_total:
            total_time = total_time + participant[x]
        total_per_trial.append(total_time)

def create_arrs():
    """Runs methods
    """
    create_information_arr()
    create_seperated_time_arr()
    create_total_time_compare()
    create_total_trial_compare_array()

def display_data():
    """Displays data
    """
    for x in range(num_trials):
        print("Minutes off for trial %d: %d" %(x+1 ,total_per_trial[x]))

open_file()
create_arrs()
display_data()
