import os
import pandas as pd

class CSVFileHandler:
    def __init__(self):
        self.script_dir = self.get_script_dir()

    def get_script_dir(self) -> str:
        """Return the directory where the script is located."""
        return os.path.dirname(os.path.abspath(__file__))

    def read_csv_file(self, filename: str) -> pd.DataFrame:
        """Read a CSV file from the 'inputs' directory and return a DataFrame.

        Args:
            filename (str): Name of the input CSV file.

        Returns:
            pd.DataFrame: DataFrame containing the CSV data.
        """
        input_file_path = os.path.join(self.script_dir, "inputs", filename)
        if not os.path.isfile(input_file_path):
            raise FileNotFoundError(f"File not found: {input_file_path}")
        return pd.read_csv(input_file_path)

# Example usage
if __name__ == "__main__":
    handler = CSVFileHandler()
    try:
        df_cpi = handler.read_csv_file("cpi_inflation_data.csv")
        print("File read successfully")
    except FileNotFoundError as e:
        print(e)
