# PyPoll with Python

## Overview

This project is a Python script that will perform an election audit of votes for the Colorado Board of Elections. It takes an input csv file with columns for Ballot ID, County, and Candidate and performs basic analysis on it. The script outputs to `stdout` and to a text file. The output contains the total number of votes cast, a list of candidates, the number of votes each candidate received, the percentage of votes each candidate won, and the winner of the election based on popular vote.

### Purpose

The purpose of this project is to automate what would normally be a tedious counting process. While this dataset is still small enough that it could be analyzed using a tool like Excel, it can be applied to larger elections and still run just as well. 

## Election-Audit Results

The election audit script ran successfully, and our results are summarized below.
* Total Votes: 369,711
* County Votes:
	- Jefferson: 10.5% (38,855)
	- Denver: 82.8% (306,055)
	- Arapahoe: 6.7% (24,801)
* Largest County Turnout: Denver
* Percentage and Total Votes for Each Candidate
	- Charles Casper Stockham: 23.0% (85,213)
	- Diana DeGette: 73.8% (272,892)
	- Raymon Anthony Doane: 3.1% (11,606)
* Percentage and Total Votes for Winning Candidate
	- Winner: Diana DeGette
	- Winning Vote Count: 272,892
	- Winning Percentage: 73.8%


## Election-Audit Summary

This script can currently be used for any election in which the results are saved in a csv file with headers for BallotID, County, and Candidate. The following block of code limits the script to csv files in that format.
```
        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
```
To allow more flexibility we could use a for loop to go through each row list and create a list and dictionary for each unique option, just as we hard coded for the candidate and county. The csv file would still need to have the ballot ID first so that we don't count votes by that, but otherwise it should allow the script to be used for more elections. 

Another change that would be helpful would be to allow the user to choose what input and output file they would like to use, that way they don't have to go into the script and change it by hand for each different election.
