Data Structure:
  we will use a dictionary to store the rules for quick lookup. Each question (Qx) points to another dictionary that maps answers (Cx) to the next question (Qy).

Initialization:
  Parse the rules to fill the dictionary.

User Interaction Loop:
  Start at question Q1.
  Print the current question and ask the user for their answer.
  Use the dictionary to find the next question based on the user's answer.
  If no more questions are available, print "Thank You!" and end.

Complexity Analysis:
  Time Complexity: Parsing the rules takes 𝑂(𝐿), where L is the number of rules. Each user input involves an 𝑂(1)  dictionary lookup, making it efficient.
  Space Complexity: Storing the rules in the dictionary takes 𝑂(𝐿)  
