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

data = load_data(file_path)
if data is not None:
    print(data.head())
    print("Data loaded successfully:")     