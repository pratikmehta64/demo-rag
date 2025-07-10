import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import asyncio
from app.backend.api.routes.llms import get_llm_response
from app.backend.api.routes.docs import index_documents
from app.settings.constants import DATA_DIR

st.title("File QnA Demo with Gemma")
files = st.file_uploader(label="Upload file(s)", 
                        type=["txt", "pdf", "docx", "md"],
                        accept_multiple_files=True,
                        )
# Radio buttons for answer length
# answer_length = st.radio("Answer Length:", ["Short", "Long"], horizontal=True)

user_query = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not files,
)

if files and user_query and len(files) <= 3:
    # Call an API that indexes the files using llamaindex and then queries it
    st.write("Processing your query...")
    # Here you would typically call your backend API to handle the file processing and querying
    for file in files:
        save_path = Path(DATA_DIR, file.name)
        with open(save_path, mode='wb') as f:
            f.write(file.getvalue())
            
            if save_path.exists():
                st.success(f"File {file.name} saved successfully at {save_path}")
            else:
                st.error(f"Failed to save file {file.name} at {save_path}")
    # create an index from the uploaded files via llamaindex
    index = index_documents()
    
    # Call the LLM to get a response based on the user query
    llm_response = asyncio.run(get_llm_response(
        user_query=user_query,
        length="Long".lower()
    ))
    st.write(f"Response from LLM:\n {llm_response}")
    
    
else:
    if not files:
        st.warning("Please upload at least one and at most three files to ask a question.")
    if not user_query:
        st.warning("Please enter a query to get a response.")     
    if len(files) > 3:
        st.warning("You can only upload up to three files at a time.")