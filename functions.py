import numpy as np
import pandas as pd

def lowercase_cols(df):
    
    df2 = df.copy()
    
    cols = df2.columns
    new_cols = []
    
    for col in cols:
        new_col = ""
        for letter in col:
            if letter == " ":
                letter = "_"
                new_col += letter
            else:
                new_col += letter
        new_cols.append(new_col.lower())
    df2.columns = new_cols
    
    return df2

def remove_na(df, threshold=25):    
    
    df2 = df.copy()
    
    cols = df2.columns
    rows = df.shape[0]
    
    for col in cols:
        na = df2[col].isna().sum()
        if na > (threshold*rows/100):
            df2 = df2.drop([col], axis=1)
        else: 
            df2 = df2[df2[col].isna()==False]
    
    return df2

def starless(x):
    
    x = x.replace(' ★', "")
    x = x.replace('★', "")
    x = int(x)

    return x

def show_me_the_money(x):

    x = x.replace('€', "")
        
    if "." in x:
        split = x.split(".")
        x = split[0] + split[1]
        x = x.replace("M", "00000")
        x = x.replace("K", "00")

    else:       
        x = x.replace("M", "000000")
        x = x.replace("K", "000")
            
    x = int(x)
    
    return x

def inches_to_cm(x):
    
    x = x.replace('"', "")
    split = x.split("'")
    split[0] = float(split[0])
    split[1] = float(split[1])
    split[0] = split[0]*30.48
    split[1] = split[1]*2.54
    x = split[0]+split[1]
    
    return x

def never_positive(df):
    
    cols = df.columns
    
    for col in cols:
        new_col = []
        for value in df[col]:
            
            if "+" in value:
                split = value.split("+")
                split[0] = int(split[0])
                split[1] = int(split[1])
                value = split[0]+split[1]
            else: value = int(value)
            
            new_col.append(value)
        df[col] = new_col
        
    return df

def master_func(df):
    
    df2 = df.copy()
    
    df2 = lowercase_cols(df2)
    df2 = remove_na(df2)
    
    df2["w/f"] = df2["w/f"].apply(starless)
    df2["sm"] = df2["sm"].apply(starless)
    df2["ir"] = df2["ir"].apply(starless)
    
    df2["value"] = list(map(show_me_the_money,df2["value"]))
    df2["wage"] = list(map(show_me_the_money,df2["wage"]))
    df2["release_clause"] = list(map(show_me_the_money,df2["release_clause"]))
    df2["hits"] = list(map(show_me_the_money,df2["hits"]))

    df2["height"] = df2["height"].apply(inches_to_cm)
    
    df2["joined"] = pd.to_datetime(df2["joined"], errors="coerce")
    
    df2["weight"] = df2["weight"].map(lambda x: x.rstrip('lbs'))
    df2["weight"] = pd.to_numeric(df2["weight"], errors='coerce')
    
    positions_stats = df2[['ls', 'st', 'rs',
       'lw', 'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram', 'lm', 'lcm', 'cm',
       'rcm', 'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb', 'lcb', 'cb',
       'rcb', 'rb', 'gk']].copy()
    positions_stats = never_positive(positions_stats)
    df2 = df2.drop(['ls', 'st', 'rs',
       'lw', 'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram', 'lm', 'lcm', 'cm',
       'rcm', 'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb', 'lcb', 'cb',
       'rcb', 'rb', 'gk'], axis=1)
    df2 = pd.concat([df2, positions_stats], axis=1)
    
    return df2

def lowercase_cols(df):
    
    df2 = df.copy()
    
    cols = df2.columns
    new_cols = []
    
    for col in cols:
        new_col = ""
        for letter in col:
            if letter == " ":
                letter = "_"
                new_col += letter
            else:
                new_col += letter
        new_cols.append(new_col.lower())
    df2.columns = new_cols
    
    return df2

def remove_na(df, threshold=25):    
    
    df2 = df.copy()
    
    cols = df2.columns
    rows = df.shape[0]
    
    for col in cols:
        na = df2[col].isna().sum()
        if na > (threshold*rows/100):
            df2 = df2.drop([col], axis=1)
        else: 
            df2 = df2[df2[col].isna()==False]
    
    return df2

def starless(x):
    
    x = x.replace(' ★', "")
    x = x.replace('★', "")
    x = int(x)

    return x

def show_me_the_money(x):

    x = x.replace('€', "")
        
    if "." in x:
        split = x.split(".")
        x = split[0] + split[1]
        x = x.replace("M", "00000")
        x = x.replace("K", "00")

    else:       
        x = x.replace("M", "000000")
        x = x.replace("K", "000")
            
    x = int(x)
    
    return x

def inches_to_cm(x):
    
    x = x.replace('"', "")
    split = x.split("'")
    split[0] = float(split[0])
    split[1] = float(split[1])
    split[0] = split[0]*30.48
    split[1] = split[1]*2.54
    x = split[0]+split[1]
    
    return x

def never_positive(df):
    
    cols = df.columns
    
    for col in cols:
        new_col = []
        for value in df[col]:
            
            if "+" in value:
                split = value.split("+")
                split[0] = int(split[0])
                split[1] = int(split[1])
                value = split[0]+split[1]
            else: value = int(value)
            
            new_col.append(value)
        df[col] = new_col
        
    return df

def master_func(df):
    
    
    df2 = df.copy()
    
    df2 = lowercase_cols(df2)
    df2 = remove_na(df2)
    
    df2["w/f"] = df2["w/f"].apply(starless)
    df2["sm"] = df2["sm"].apply(starless)
    df2["ir"] = df2["ir"].apply(starless)
    
    df2["value"] = list(map(show_me_the_money,df2["value"]))
    df2["wage"] = list(map(show_me_the_money,df2["wage"]))
    df2["release_clause"] = list(map(show_me_the_money,df2["release_clause"]))
    df2["hits"] = list(map(show_me_the_money,df2["hits"]))

    df2["height"] = df2["height"].apply(inches_to_cm)
    
    df2["joined"] = pd.to_datetime(df2["joined"], errors="coerce")
    
    df2["weight"] = df2["weight"].map(lambda x: x.rstrip('lbs'))
    df2["weight"] = pd.to_numeric(df2["weight"], errors='coerce')
    
    positions_stats = df2[['ls', 'st', 'rs',
       'lw', 'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram', 'lm', 'lcm', 'cm',
       'rcm', 'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb', 'lcb', 'cb',
       'rcb', 'rb', 'gk']].copy()
    positions_stats = never_positive(positions_stats)
    df2 = df2.drop(['ls', 'st', 'rs',
       'lw', 'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram', 'lm', 'lcm', 'cm',
       'rcm', 'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb', 'lcb', 'cb',
       'rcb', 'rb', 'gk'], axis=1)
    df2 = pd.concat([df2, positions_stats], axis=1)
    
    return df2
