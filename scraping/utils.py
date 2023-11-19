import pandas as pd
import re
from datetime import datetime


def subs_col(df, col_index):
    regex = {
        r'muito insatisfeito': 1,
        r'muito satisfeito': 5,
        r'insatisfeito': 2,
        r'neutro': 3,
        r'satisfeito': 4
    }

    for i, row in df.iterrows():
        text = str(row.iloc[col_index])
        for old, new in regex.items():
            text = re.sub(old, str(new), text, flags=re.IGNORECASE)
        df.at[i, df.columns[col_index]] = int(text)
    return df

def convert_date_format(df, col_index):
    for i, row in df.iterrows():
        date_str = str(row.iloc[col_index])
        try:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y %H:%M')
        except ValueError:
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                print(f"Data inválida encontrada: {date_str}")
                continue

        new_date_str = date_obj.strftime('%d/%m/%Y %H:%M')
        df.at[i, df.columns[col_index]] = new_date_str

    return df

def sat_level(csv_path):
    df = pd.read_csv(csv_path)
    df = subs_col(df, 1)
    df.to_csv(csv_path, index=False)

def date_type(csv_path):
    df = pd.read_csv(csv_path)
    df = convert_date_format(df, 6)
    df.to_csv(csv_path, index=False)

