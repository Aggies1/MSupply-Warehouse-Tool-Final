import streamlit as st
# Import the function(s) from your other file
from my_complex_program.core_logic import run_main_process 

# --- Start of your website UI ---
st.title("My Program Shell")

user_text = st.text_input("Enter some data to process:", "Hello World")

if st.button("Run Program"):
    with st.spinner("Processing..."):
        # Call your complex program
        output = run_main_process(user_text)
        
        # Display the result on the website
        st.success("Done!")
        st.write(output)
