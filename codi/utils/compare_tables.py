import pandas as pd
import seaborn as sns
import matplotlib


def compare_csv_tables(path1, path2):
    """
    Computes the difference between the common columns and rows of two csv tables and colors them.
    It computes the gains and losses from path1 to path2, i.e. (path2 - path1)
    
    parameters:
        path1: absolute path of a csv file
        path2: absolute path of a csv file
    returns:
        Dataframe: Difference between columns of path2 and columns of path1 in a pandas table styled.
    """
    df1 = pd.read_csv(path1, index_col=0)
    df2 = pd.read_csv(path2, index_col=0)
    
    # Delete support row since it is not useful
    if 'support' in df1.index:
        df1 = df1.drop('support')
        
    if 'support' in df2.index:
        df2 = df2.drop('support')
    
    return compare_pd_tables(df1, df2)


def compare_pd_tables(df1, df2):
    """
    Computes the difference between the common columns and rows of two pandas tables and colors them.
    It computes the gains and losses from df1 to df2, i.e. (df2 - df1)
    
    parameters:
        df2: absolute path of a csv file
        df2: absolute path of a csv file
    returns:
        Dataframe: Difference between columns of df2 and columns of df1 in a pandas table styled.
    """    
    df = df2-df1
    df = df.fillna(0)
    
    # Delete support row since it is not useful
    if 'support' in df.index:
        df = df.drop('support')
    
    return df.style.background_gradient(cmap='RdYlGn', vmin=-0.2, vmax=0.2)
