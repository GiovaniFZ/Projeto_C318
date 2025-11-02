import pandas

file_path = 'datatran2024.csv'

def load_data(file_path):
    """Load data from a CSV file into a pandas DataFrame."""
    try:
        data = pandas.read_csv(file_path, encoding='ANSI', sep=';', decimal=',')
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pandas.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pandas.errors.ParserError:
        print("Error: There was a parsing error while reading the file.")
        return None

df = load_data(file_path)
if df is not None:
    print(df.info())
    df_describe = df.describe()
    