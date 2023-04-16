# '''
# PyBank > main.py
# by Ryan Cornelius 4 / 15 / 2023

# Prompt:
#     In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
#     You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#         The total number of votes cast
#         A complete list of candidates who received votes
#         The percentage of votes each candidate won
#         The total number of votes each candidate won
#         The winner of the election based on popular vote

# Expected Results:
#     Election Results
#     -------------------------
#     Total Votes: 369711
#     -------------------------
#     Charles Casper Stockham: 23.049% (85213)
#     Diana DeGette: 73.812% (272892)
#     Raymon Anthony Doane: 3.139% (11606)
#     -------------------------
#     Winner: Diana DeGette
#     -------------------------
    
# Input Format: 
#     Ballot ID,County,Candidate
#     1323913,Jefferson,Charles Casper Stockham
#     1005842,Jefferson,Charles Casper Stockham
#     1880345,Jefferson,Charles Casper Stockham
#     1600337,Jefferson,Charles Casper Stockham
# '''


#%%       Modules

#A lot of the code needed is similar to PyBank. Copied over the previous code to use as a scaffold. (including comments)
import csv

#%%      DataCollection

BallotIDList = []
CountyList = []
CandidateList = []

csvpath = 'Resources/election_data.csv' #assume path is set from the project folder

#Create a list for each input vector
with open(csvpath, encoding='utf') as csvfile: #use in-class taught csv read method
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader = next(csvreader) #skipping and grabbing the header
    for entry in csvreader:
        [BallotID, County, Candidate]  = entry
        BallotIDList.append(BallotID)
        CountyList.append(County)
        CandidateList.append(Candidate)
        
#from https://favtutor.com/blogs/remove-duplicates-from-list-python, I learned about sets. Looks like most list comprehension works on them too.
CountySet = set(CountyList)
CandidateSet= set(CandidateList)   
NumBallots = len(BallotIDList)
NumUniqueBallots = len(set(BallotIDList)) #I had to check, it seems there were no repeat Ballot IDs

        
#%%     Data Analysis
ResultsData = []
VoteOutput = ''

for candidate in CandidateSet:
    NumVotes = CandidateList.count(candidate)
    PercentVotes = NumVotes / NumBallots
    ResultsData.append((candidate, NumVotes, PercentVotes))
    VoteOutput+=(f'{candidate}: {PercentVotes:.3%} ({NumVotes}) \n') #its easiest for me to write the string output block here. I could probably do a loop over the tuple later, but then my next code block doesn't look as pretty!
    

MostVotes = max([Tup[1] for Tup in ResultsData]) #checking for the candidate with the most votes
for Tup in ResultsData:
    if Tup[1] == MostVotes:
        ElectionWinner = Tup[0]




#%%     Output per directions - Again, why be unique when I've been given the desired structure!
results = f'Election Results \n\
------------------------- \n\
Total Votes: {NumBallots} \n\
------------------------- \n\
{VoteOutput}\
------------------------- \n\
Winner: {ElectionWinner} \n\
------------------------- \n'
#formatting from https://zetcode.com/python/fstring/


print(results)

fileout ='Analysis/Results.txt'           
with open(fileout, 'w') as out:     #from https://www.pythontutorial.net/python-basics/python-write-text-file/       
    out.write(results)            
print(f'\nResults written to {fileout}')     
            
            