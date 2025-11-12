mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
amount_missions = len(mission_names) #Count the amount of missions
sucessful_mission = 0 
for true in mission_success: #Use a for loop to count sucessful missions
    if true:
        sucessful_mission += 1
success_percentage = 100*sucessful_mission/amount_missions #Calculate the true percentage of success for missions
success_rounded= round(success_percentage,2) #Round the true percentage to 2
missions_before2000 = []
for i in range(len(mission_years)): #Find all the missions before the year 2000
    if mission_years[i] < 2000:
        missions_before2000.append(mission_names[i]) #add the missions too the new list of all the missions before 2000

print("Total number of missions: " + str(amount_missions))
print("Number of successful missions: " + str(sucessful_mission))
print("Success rate: " + str(success_rounded) + "%")
print("Missions launched before the year 2000: ")
print("-",missions_before2000[0])
print("-",missions_before2000[1])
print("-",missions_before2000[2])
print("-",missions_before2000[3])
print("-",missions_before2000[4])
print("-",missions_before2000[5])