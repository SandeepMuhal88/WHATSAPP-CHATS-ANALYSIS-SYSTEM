import numpy as np
import pandas as pd
import streamlit as st

def print_data(selected_user,df):


    # if selected_user != 'All Users':
    #     df=df[df['user']==selected_user]
    # num_message=df.shape[0]
    # word=[]
    # for message in df['Message']:
    #     word.extend(message.split())
    # return num_message, len(word)    

    if selected_user=="All Users":
        # If "All Users" is selected, return the total number of messages
        num_message=df.shape[0]
        # For all users, we can also return the total number of words
        word=[]
        for message in df['Message']:
            # print(i)
            # print(i.split())
            word.extend(message.split())
        return num_message, len(word)
    else:
        new_df=df[df['user'] == selected_user]
        num_message=new_df.shape[0]
        # For a specific user, we can also return the total number of words
        word=[]
        for message in new_df['Message']:
            # print(i)
            # print(i.split())
            word.extend(message.split())
        return num_message, len(word)