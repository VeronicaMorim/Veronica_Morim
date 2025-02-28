import pytest
import pandas as pd
import numpy as np

def test_read_csv():
    df = pd.read_csv('data/world-data-2023.csv', encoding='ISO-8859-1', low_memory=False)
    df1 = pd.read_csv('data/globalterrorism.csv', encoding='ISO-8859-1', low_memory=False)
    assert not df.empty, "world-data-2023.csv should not be empty"
    assert not df1.empty, "globalterrorism.csv should not be empty"


def test_drop_columns_with_nulls():
    df1 = pd.read_csv('data/globalterrorism.csv', encoding='ISO-8859-1', low_memory=False)
    len_terrorism = len(df1)
    df1 = df1.replace('', np.nan).replace(0, np.nan)
    
    for column in df1.columns:
        if len(df1[df1[column].isna()]) / len_terrorism > 0.4:
            df1 = df1.drop(column, axis=1)
    
    assert 'some_column' not in df1.columns, "Column with more than 40% nulls should be dropped"


def test_replace_germany():
    df1 = pd.read_csv('data/globalterrorism.csv', encoding='ISO-8859-1', low_memory=False)
    df1['country_txt'] = df1['country_txt'].replace('East Germany (GDR)', 'Germany')
    df1['country_txt'] = df1['country_txt'].replace('West Germany (FRG)', 'Germany')
    
    assert 'East Germany (GDR)' not in df1['country_txt'].values, "East Germany (GDR) should be replaced by Germany"
    assert 'West Germany (FRG)' not in df1['country_txt'].values, "West Germany (FRG) should be replaced by Germany"

