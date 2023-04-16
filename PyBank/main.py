# '''
# PyBank > main.py
# by Ryan Cornelius 4 / 15 / 2023

# Prompt:
# Your task is to create a Python script that analyzes the records to calculate each of the following values:
#     The total number of months included in the dataset
#     The net total amount of "Profit/Losses" over the entire period
#     The changes in "Profit/Losses" over the entire period, and then the average of those changes
#     The greatest increase in profits (date and amount) over the entire period
#     The greatest decrease in profits (date and amount) over the entire period
#     Your analysis should align with the following results:
    
# Expected Results:
#     Total Months: 86
#     Total: $22564198
#     Average Change: $-8311.11
#     Greatest Increase in Profits: Aug-16 ($1862002)
#     Greatest Decrease in Profits: Feb-14 ($-1825558)
        
# Input format:
#     Date,Profit/Losses
#     Jan-10,1088983
#     Feb-10,-354534
#     Mar-10,276622
    
# '''

#%%      Modules
import csv
import statistics

#%%      DataCollection
counter = 0
NetGain = 0
PrevMonthNet = 0 #purely to remove the "not defined" error. 
ProfitChanges = []

csvpath = 'Resources/budget_data.csv' #assume path is set from the project folder

with open(csvpath, encoding='utf') as csvfile: #use in-class taught csv read method
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader = next(csvreader) #skipping and grabbing the header
    for entry in csvreader:
        MonthDate, MonthNet  = entry[0], float(entry[1])
        counter+=1
        NetGain = NetGain + MonthNet
        if counter > 1: # using this method to do i1-i0 math, as no previous month will exist for the first loop.
            ChangeNet = MonthNet - PrevMonthNet
            ProfitChanges.append((MonthDate,ChangeNet)) #I used a tuple just to have a complete list
        PrevMonthNet = float(entry[1])
        
#%%     Data Analysis
AvgNet = statistics.mean([Tup[1] for Tup in ProfitChanges]) #decided not to define the list outside the calculation due to only using this 3 times
MaxProfitInc = max([Tup[1] for Tup in ProfitChanges])
MinProfitInc = min([Tup[1] for Tup in ProfitChanges])
for Tup in ProfitChanges: #collecting the relative dates to my min and max
    if Tup[1] == MaxProfitInc:
        MaxProfitIncDate = Tup[0]
    elif Tup[1] == MinProfitInc:
        MinProfitIncDate = Tup[0]
        


#%%     Output per directions
results = f'Financial Results \n \
---------------------------- \n \
Total Months: {counter}  \n \
Total: ${NetGain:.0f} \n \
Average Change: ${AvgNet:.2f} \n \
Greatest Increase in Profits: {MaxProfitIncDate} (${MaxProfitInc:.0f}) \n \
Greatest Decrease in Profits: {MinProfitIncDate} (${MinProfitInc:.0f})'

print(results)
#formatting from https://zetcode.com/python/fstring/

fileout ='Analysis/Results.txt'           
with open(fileout, 'w') as out:     #from https://www.pythontutorial.net/python-basics/python-write-text-file/       
    out.write(results)            
print(f'\nResults written to {fileout}')     
            
            