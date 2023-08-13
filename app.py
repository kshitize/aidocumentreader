import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from CSVreader import CSVreader1
from PDFreader import PDFreader



def main():
   # Set the title of the Streamlit app

    
    # Create a sidebar menu
    menu_selection = st.sidebar.radio("Menu", ["CSV Reader", "PDF Reader"])
    
    # Display different content based on the selected menu item
    if menu_selection == "CSV Reader":
        CSVreader1()
        
      
    elif menu_selection == "PDF Reader":
        PDFreader()
        
        
    elif menu_selection == "Settings":
        st.write("Here you can configure the settings.")  # Set the title of the Streamlit app
    
        

if __name__ == "__main__":
    main()
