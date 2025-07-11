# demo-rag
RAG++

# Installation instructions for unix

Pre-requisites:
1. uv (`pip install uv`)

Instructions:
1. `uv sync`

Run the frontend via streamlit
1. `cd demo-rag`
2. `streamlit run run_streamlit.py`

In a separate terminal, run the backend:
1. `cd demo-rag`
2. `fastapi dev app/main.py`

