import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import seaborn as sns


def plot_age_demographics_over_time(
    input_filename: str = "../inputs/argentina_age_demographic.csv",
    output_file_path: str = "../outputs/argentina_age_demographics_over_time.png",
) -> None:
    # Read the CSV file
    df_argentina_ages = pd.read_csv(input_filename)

    # Convert percentages to floats
    age_columns = df_argentina_ages.columns[3:]
    for col in age_columns:
        df_argentina_ages[col] = df_argentina_ages[col].str.rstrip('%').astype('float') / 100.0

    # Set the positions and width for the bars
    bar_width = 0.1
    positions = np.arange(len(df_argentina_ages))

    # Plotting the data
    plt.figure(figsize=(16, 8))

    for i, col in enumerate(age_columns):
        plt.bar(positions + i * bar_width, df_argentina_ages[col], bar_width, label=col)

    plt.xlabel("Year")
    plt.ylabel(r"% of Population")
    plt.title("Argentina Age Demographics Over Time")
    plt.xticks(positions + bar_width * (len(age_columns) / 2), df_argentina_ages['Years'])
    plt.legend()

    plt.grid(True, which="both", ls="--")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_file_path)
    plt.show()


if __name__ == "__main__":
    plot_age_demographics_over_time()
