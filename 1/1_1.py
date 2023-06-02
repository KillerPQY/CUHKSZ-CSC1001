final = float(input('Please enter the final account value:')) #Input the final account value
rate = float(input('Please enter the annual interest rate in percent:')) #Input the annual interest rate in percent
rate = rate/100 #Change percent into float
year = int(input('Please enter the number of years:')) #Input the years
initial = final/((1+rate)**year) #Calculate the initial account value
print('The initial value is: %s'%initial) #print the initial account value