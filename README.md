## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Answer the questions

### 2.1 what refactoring signs (code smells) suggest this refactoring?

Feature Envy

### 2.2 what design principle suggests this refactoring? Why?

It is Single Responsibility Principle.

Single Responsibility: Each class should have one reason to change. In this context, the Movie class should only be responsible for managing movie-related information. While the Rental class should handle everything related to a rental (e.g., rental price, rental points, and pricing strategy).

Since price_code is only relevant in the context of a rental (not for the movie itself), moving it to Rental aligns will make that the Rental class is fully responsible for rental-related behavior.

## Rationale

### 5.1 Decide where price_code_for_movie should be implemented. It can be a class method or top-level function in an existing module. The choices are:

I chose the Rental class method because only Rental needs to use this method to set its price strategy. 

The design principles are Single Responsibility Principle and High Cohesion. 

(SRP) Explanation:

The main usage of Rental class is for get the price of the movie.  
Since the price is determined when a movie is rented, the responsibility of setting the price code logically fits into the Rental class.


(High Cohesion) Explanation: 

By placing the pricing strategy logic in the Rental class, I will maintain a high level of cohesion. 
The Rental class handles all operations related to renting, and determining the price code is naturally part of this responsibility.
This keeps the design modular and easy to modify if rental-specific rules change in the future.