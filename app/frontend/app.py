import streamlit as st

st.title("File QnA Demo with Gemma")
files = st.file_uploader(label="Upload file(s)", 
                        type=["txt", "pdf", "docx", "md"],
                        accept_multiple_files=True,
                        )
user_query = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not files,
)

if files and user_query:
    # Call an API that indexes the files using llamaindex and then queries it
    st.write("Processing your query...")
    # Here you would typically call your backend API to handle the file processing and querying
    # For demonstration, we will just simulate a response
    st.write("Simulated response: This is a summary of the uploaded files based on your query.")
else:
    if not files:
        st.warning("Please upload at least one and at most three files to ask a question.")
    if not user_query:
        st.warning("Please enter a query to get a response.")     
    if len(files) > 3:
        st.warning("You can only upload up to three files at a time.")