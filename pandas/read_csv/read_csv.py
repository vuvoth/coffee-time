import pandas as pd

path_to_file = "./example.csv"

if __name__ == "__main__":
    csv_data = pd.read_csv(path_to_file)
    print(csv_data)
