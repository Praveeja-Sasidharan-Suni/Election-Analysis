# Election-Analysis

## Overview of Election Audit
The purpose of this project was to provide an election audit for the Colorado Board of Elections. 

1. Calculate the total number of votes casted.
2. Get a complete list of candidates who received votes.
3. Get the county who had the highest voter turnout. 
4. Calculate the total number of votes each candidate received. 
5. Calculate the percentage of votes each candidate got. 
6. Determine the winner of the election based on popular vote. 

## Resources
Data Source: election_results.csv 
Software: Python 3.7.6, Visual Studio Code 

## Election Audit Results 
The analysis of the election shows that: 
  * There was 379,111 votes cast in the election.
    * The candidates were:
     * Charles Casper Stockham
     * Diana DeGette 
     * Raymon Anthony Doane
      
  * The candidate results were:
      * Charles Casper Stockham received 23% of the total vote with 85,213 votes.
      * Diana DeGette received 82.8% of the total vote with 272,892 votes.
      * Raymon Anthony Doane received 3.1% of the total vote with 11,606 votes. 
      * TOTAL VOTES= 369,711
      
  * The winner of the election was:
      * Candidate Diana DeGette, who recieved 82.8% of the total vote with 272,892 votes.
      
  * The counties results:
      * Jefferson county had 10.5% of the total vote with 38,855 votes. 
      * Denver county had 82.8% of the total vote with 306,055 votes. 
      * Arapahoe county had 6.7% of the total vote with 24,801 votes. 
      * TOTAL VOTES= 369,711

* The county with the highest turnout was Denver with 306,055 votes.
  
### The election results printed to the Command line:

![commandline_output.png](https://github.com/Praveeja-Sasidharan-Suni/Election-Analysis/blob/main/images/commandline_output.PNG?raw=true)

### The Election Results saved to a text file.
 
 ![Election_Results_text_file.png](https://github.com/Praveeja-Sasidharan-Suni/Election-Analysis/blob/main/images/Election_Results_text_file.PNG?raw=true)

 
## Election Audit Summary

The Election Results are printed to the Command Line and are saved to a Text File too.This code became very useful to determine the winning candidate and winning county in very less time.
This script can me modified for different future purposes by having it run multiple times to get a deeper understadning if someone was a campaign manager for a candidate. 
We can modify this code to find out the election winners in cities and states too.
 We can go into details to see which cities hold a significant position in determining if a candidate will be the winner of the election. 
Also we can modify this script for future use by adding more parameters like Age, sex, and ethnicity etc for deeper understanding about the campaign.
