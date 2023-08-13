import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib
# Initialize OpenAI and PandasAI
# Set your OpenAI API token
openAi = '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'
llm = OpenAI(api_token=openAi)
pandas_ai = PandasAI(llm)
matplotlib.use("TkAgg")
def CSVreader1():
        st.title("AI Reader")

        # Prompt the user to choose files to read (CSV)
        st.write("Choose files to read (CSV)")

        # File uploader for CSV files
        uploadedfiles = st.file_uploader("Upload CSV", type=['csv'], accept_multiple_files=True)
        dfs = []

        # If files are uploaded
        if uploadedfiles is not None:
            # Read each uploaded file as a DataFrame and append to dfs list
            for uploadedfile in uploadedfiles:
                df = pd.read_csv(uploadedfile)
                dfs.append(df)

            # Display the uploaded tables
            num_tables = len(dfs)
            for i in range(num_tables):
                st.write(f"Table {i+1}")
                st.write(dfs[i].head(5))

            # Prompt input
            prompt = st.text_area("Enter your prompt")
            
            # Generate button
            if st.button("Generate"):
                if prompt:
                    # Run PandasAI on the uploaded tables with the provided prompt
                    with st.spinner('Generating response...'):
                        st.write(pandas_ai.run(dfs, prompt=prompt))
                else:
                    st.warning("Please enter a prompt")

            # Draw  button
            if st.button("Draw"):
                if prompt:  
                    # Run PandasAI on the uploaded tables with the provided prompt
                    with st.spinner('Generating response...'):
                        st.write(pandas_ai.run(dfs, prompt=prompt))
                else:
                    st.warning("Please enter a prompt")