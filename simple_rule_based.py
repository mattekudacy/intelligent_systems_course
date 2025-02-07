# expert_system.py
def diagnose_computer_issue():
    print("Computer Issue Diagnostic System")
    print("Answer the following questions with 'yes' or 'no'.")
    
    slow = input("Is your computer slow? ").strip().lower()
    internet = input("Is the internet not working? ").strip().lower()
    
    if slow == "yes":
        print("Potential solution: Try closing unused programs, clearing temporary files, or upgrading your RAM.")
    if internet == "yes":
        print("Potential solution: Restart your router, check your network settings, or contact your ISP.")
    if slow == "no" and internet == "no":
        print("No issues detected based on the given answers.")
    
if __name__ == "__main__":
    diagnose_computer_issue()