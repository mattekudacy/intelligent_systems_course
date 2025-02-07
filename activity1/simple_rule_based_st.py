import streamlit as st

def diagnose_computer_issue_streamlit():
    st.title("Computer Issue Diagnostic System")
    st.write("Answer the following questions:")
    
    slow = st.text_input("Is your computer slow? (yes/no)").strip().lower()
    internet = st.text_input("Is the internet not working? (yes/no)").strip().lower()
    
    if st.button("Diagnose"): 
        solutions = []
        
        if slow == "yes":
            solutions.append("Try closing unused programs, clearing temporary files, or upgrading your RAM.")
        if internet == "yes":
            solutions.append("Restart your router, check your network settings, or contact your ISP.")
        if not solutions:
            solutions.append("No issues detected based on the given answers.")
        
        st.subheader("Potential Solutions:")
        for solution in solutions:
            st.write(f"- {solution}")

if __name__ == "__main__":
    diagnose_computer_issue_streamlit()
