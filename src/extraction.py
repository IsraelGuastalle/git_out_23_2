import pandas as pd
import numpy as np
import streamlit as st

def load_data():
    return pd.read_csv('C:/Users/israelguastalle-sao/repos_cds/git_para_ds_out_23/projeto/data/bikes_completed.csv')