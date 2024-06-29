### CS 188 - Intro to Machine Learning (Spring 2023)

Garrett Baltz

## Project - Pac-Man

# Summary

Throughout the course, I was tasked with slowly creating a solver for the infamous Pac-Man game utilizing machine learning. 

First, I created search methods for a solver to follow such as BFS, A*, Uniform Cost, and more. This involved a bit of researching into which algorithms were the best and revealed that each has their positives:

- BFS is great for immediate searches such as finding the closest pellet
- DFS is best for finding the quickest path to a far pellet
- and more...

Second, I created logic planning methods to help the Pac-Man decide what state it was in, what needed to be done, and later on, how to do so.

Third, I designed evaluation functions to determine the best possible routes for Pac-Man to take to meet each of his criteria. This was the first true evidence of machine learning in application as we had to 
determine how to score each "search" based on features such as quickest time, most pellets, etc.

Fourth,
