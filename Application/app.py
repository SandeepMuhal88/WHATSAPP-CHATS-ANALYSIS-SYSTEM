import streamlit as st

import preprocesor
import helper


st.sidebar.title("Whatapp chat analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df = preprocesor.Preprocessing(data)
    st.write(df)
    # Featch Usernames

    User_list=df['user'].unique().tolist()
    User_list.insert(0, "All Users")
    selected_user =st.sidebar.selectbox("Show analysis with respect to", User_list)
    
    if st.sidebar.button("Show Analysis"):
        num_message,word=helper.print_data(selected_user, df)
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_message)
        with col2:
            st.header("Total Words")
            st.title(word)