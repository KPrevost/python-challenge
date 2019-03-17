import os
import csv
import collections

pyPollCSV= os.path.join('Input/election_data.csv')

rows = 0
c = collections.Counter()
TotalVotes = 0
KhanVote = 0
CorreyVote = 0
LiVote = 0
OTooleyVote = 0
Winner = ["Candidate",0]

with open (pyPollCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        rows = rows + 1 
        if rows>1:
            TotalVotes = TotalVotes + 1
            c[row[2]] +=1
            if row[2] == "Khan":
                KhanVote = KhanVote + 1
            if row[2] == "Correy":
                CorreyVote = CorreyVote + 1
            if row[2] == "Li":
                LiVote = LiVote + 1
            if row[2] == "O'Tooley":
                OTooleyVote = OTooleyVote + 1
    Winner = ["Khan", KhanVote]
    if CorreyVote > Winner[1]:
        Winner = ["Correy", CorreyVote]
    if LiVote > Winner[1]:
        Winner = ["Li", LiVote]
    if OTooleyVote>Winner[1]:
        Winner = ["O'Tooley", OTooleyVote]
    
    print("Total Votes: " + str(TotalVotes))
    print(c)
    print("Khan: " + "Total: " +str(KhanVote) +"/Percent: " + str(KhanVote/TotalVotes))
    print("Correy: " + str(CorreyVote)+"/Percent: " + str(CorreyVote/TotalVotes))
    print("Li: " + str(LiVote) +"/Percent: " + str(LiVote/TotalVotes))
    print("O'Tooley: " + str(OTooleyVote) +"/Percent: " + str(OTooleyVote/TotalVotes))
    print("Winner: " + str(Winner))

output = os.path.join('Output/pyPollPREVOST.txt')
with open(output, 'w', newline='') as txtfile:

    # Write the first row
    txtfile.write("Total Votes: " + str(TotalVotes)+"\n")
    # Write the second row
    txtfile.write(str(c) + "\n")
    #Write third row
    txtfile.write("Khan: " + "Total: " +str(KhanVote) +"/Percent: " + str(KhanVote/TotalVotes)+"\n")
    #Write fourth row
    txtfile.write("Li: " + str(LiVote) +"/Percent: " + str(LiVote/TotalVotes)+"\n")
    #Write fifth row
    txtfile.write("Correy: " + str(CorreyVote)+"/Percent: " + str(CorreyVote/TotalVotes) +"\n")
    #Write sixth row
    txtfile.write("O'Tooley: " + str(OTooleyVote) +"/Percent: " + str(OTooleyVote/TotalVotes) +"\n")
    #Write seventh row
    txtfile.write("Winner: " + str(Winner))