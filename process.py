import pandas as pd

def process_csv(file_path):
    df = pd.read_csv(file_path)
    df['string_value'] = df['string_value'].apply(lambda x: f'"{x}"' if pd.notna(x) and x != '' else x)
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    file_path = 'input.csv'
    process_csv(file_path)
