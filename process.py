import pandas as pd
import os

def process_csv(file_path):
    df = pd.read_csv(file_path)
    df['string_value'] = df['string_value'].apply(lambda x: f'"{x}"' if pd.notna(x) and x != '' else x)
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    file_path = os.getenv('CSV_FILE_PATH', 'tempfile.csv')
    process_csv(file_path)
