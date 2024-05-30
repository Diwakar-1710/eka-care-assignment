def main():
    N = 6
    rules = [
        "Q1-C2-Q3", "Q1-C1-Q2", "Q1-C3-Q4", "Q1-C4-Q5",
        "Q2-C2-Q4", "Q2-C4-Q5", "Q2-C3-Q6", "Q3-C1-Q2",
        "Q3-C2-Q5", "Q3-C4-Q6", "Q4-C2-Q6", "Q4-C4-Q5",
        "Q5-C3-Q6"
    ]
    
    #parse the rules for efficient retrival
    rule_dict = {}
    for rule in rules:
        start, choice, end = rule.split('-')
        if start not in rule_dict:
            rule_dict[start] = {}
        rule_dict[start][choice] = end
    

    current_question = "Q1"
    
    while True:
        #takes input from the user
        print(f"This is question {current_question}, enter your answer")
        user_choice = input().strip()
        
        #check if the user_choice is nt rule_dict
        if user_choice in rule_dict[current_question]:
            current_question = rule_dict[current_question][user_choice]
        else:
            print("Invalid choice. Please try again.")
            continue
        #if it curr_question is not in rule take input from user and print Thank your
        if current_question not in rule_dict:
            print(f"This is question {current_question}, enter your answer")
            input().strip()  # Take any input
            print("Thank You!")
            break


if __name__ == "__main__":
    main()
