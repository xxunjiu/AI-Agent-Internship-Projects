import os
from datetime import datetime
import pandas as pd
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent


st.title("Car Sales Data Analysis Agent")

if "logs" not in st.session_state:
    st.session_state.logs = []

st.write("Upload a CSV file and ask questions about the data.")


api_key = st.text_input("Enter your OpenAI API Key")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key


uploaded_files = st.file_uploader(
    "Upload CSV files",
    type="csv",
    accept_multiple_files=True
)

if uploaded_files:
    dfs = {}

    for file in uploaded_files:
        dfs[file.name] = pd.read_csv(file)

    for name, df in dfs.items():
        st.subheader(f"Data Preview: {name}")
        st.dataframe(df.head(10))

        st.subheader(f"Dataset Information: {name}")
        st.write("Rows and columns:", df.shape)
        st.write("Columns:", list(df.columns))

    st.subheader("Data Preview")
    st.dataframe(df.head(10))

    st.subheader("Dataset Information")
    st.write("Rows and columns:", df.shape)
    st.write("Columns:", list(df.columns))

    question = st.text_input("Ask a question about the data")

    if st.button("Analyze"):
        if not api_key:
            st.warning("Enter your OpenAI API key first.")
        elif question == "":
            st.warning("Please enter a question.")
        else:
            llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0
            )

            agent = create_pandas_dataframe_agent(
                llm,
                list(dfs.values()),     
                agent_type="openai-tools",
                allow_dangerous_code=True,
                verbose=True,
                max_iterations=20,
                max_execution_time=60,
                early_stopping_method="force",
                agent_executor_kwargs={
                    "handle_parsing_errors": True
                }
            )

            response = agent.invoke({"input": question})
            answer = response["output"]

            st.subheader("Answer")
            st.write(answer)

            log = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "question": question,
            "answer": answer,
            "tool_used": "Yes, Pandas DataFrame Agent",
            "analysis_process": "The agent used the uploaded DataFrame and Pandas tool to answer the question.",
            "human_check": "Not checked yet"
            }

            st.session_state.logs.append(log)

            st.subheader("Execution Log")

if len(st.session_state.logs) > 0:
    st.dataframe(pd.DataFrame(st.session_state.logs))
else:
    st.write("No logs yet.")