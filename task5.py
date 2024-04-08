#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days
p = int(input("Enter the current population: "))
r = float(input("Enter the rate of growth in percent: "))
t = int(input("Enter the number of days: "))
GG = p*(1+(r/100))**(t/365)
G= round(GG)
print(f"There will be {G} people after {t} days")