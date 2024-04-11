import pandas as pd

etl_Jose = "21zpallagi.csv"
etl_Hasmig = "../../GroupProjects/21zpallagi.csv"


def start(path):

    df = pd.read_csv(path)
    df.head()
    columns_to_keep = [
        'STATE', 'zipcode', 'agi_stub', 'N1', 'mars1', 'MARS2',
        'A00100', 'A02650', 'N01000', 'A01000', 'N02910', 'A02910',
        'N04470', 'A04470', 'N17000', 'A17000', 'N18300', 'A18300',
        'N19700', 'A19700', 'N20950', 'A20950', 'N85775', 'A85300'
    ]

    df_filtered = df[columns_to_keep]
    return df_filtered


def step2(df_filtered):
    
    df_AL = df_filtered.loc[df_filtered['STATE'] == "AL"]
    df_AL
    # Dictionary mapping original column names to shorter names
    short_column_names = {
        'STATE': 'State',
        'zipcode': 'Zip',
        'agi_stub': 'AGI',
        'N1': 'Returns',
        'mars1': 'Single',
        'MARS2': 'Joint',
        'A00100': 'AGI',
        'A02650': 'Total_Income',
        'N01000': 'Cap_Gain_Returns',
        'A01000': 'Cap_Gain_Amt',
        'N02910': 'Std_Ded_Charity_Returns',
        'A02910': 'Std_Ded_Charity_Amt',
        'N04470': 'Itemized_Ded_Returns',
        'A04470': 'Itemized_Ded_Amt',
        'N17000': 'Med_Dental_Returns',
        'A17000': 'Med_Dental_Amt',
        'N18300': 'Total_Taxes_Returns',
        'A18300': 'Total_Taxes_Amt',
        'N19700': 'Charitable_Returns',
        'A19700': 'Charitable_Amt',
        'N20950': 'Misc_Ded_Returns',
        'A20950': 'Misc_Ded_Amt',
        'N85775': 'Advance_Premium_Returns',
        'A85300': 'Net_Investment_Tax_Amt'
    }

    # Rename columns
    df_short_names = df_AL.rename(columns=short_column_names)

    # Now df_short_names contains columns with shorter names
    df_short_names.head(10)
    return df_short_names