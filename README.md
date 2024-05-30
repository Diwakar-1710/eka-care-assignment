## Data Structure

We will use a dictionary to store the rules for quick lookup. Each question (Qx) points to another dictionary that maps answers (Cx) to the next question (Qy).

## Initialization

Parse the rules to fill the dictionary.

## User Interaction Loop

1. Start at question Q1.
2. Print the current question and ask the user for their answer.
3. Use the dictionary to find the next question based on the user's answer.
4. If no more questions are available, print "Thank You!" and end.

## Complexity Analysis

- **Time Complexity:** Parsing the rules takes \( O(L) \), where \( L \) is the number of rules. Each user input involves an \( O(1) \) dictionary lookup, making it efficient.
- **Space Complexity:** Storing the rules in the dictionary takes \( O(L) \).

## Installation

Step-by-step instructions on how to install and get the project running.
