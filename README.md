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

Fourth, I implemented reinforcement learning through the given QLearningAgent. This is how Pac-Man gets the legal actions and values of its state, determines which action to choose, and repeats until finished. 
This is what was fed into the evaluation functions and resulted in a score.

Fifth, I created the implementation for the ghosts, utilizing inference in Bayes Nets and Discrete Distributions to govern their actions.

Finally, the full project (and course) was finished with creating a Perceptron model, a Regression model, and a DigitClassificationModel to take the core functionality of the Pac-Man solver and apply it to 
real-world data such as MNIST. 

# Takeaways

After having finished the course, I am now comfortable with concepts in machine learning such as Reinforcement Learning and Perceptrons as such concepts are what allowed me to create a Pac-Man solver. Since, 
I have applied these concepts in CS 189 to further my understanding of machine learning with Neural Networks and SVDs. 
