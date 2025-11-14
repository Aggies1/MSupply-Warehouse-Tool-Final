import streamlit as st
# Import the function(s) from your other file
from marconeapp import marcone_warehouse_analysis_app.py

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
