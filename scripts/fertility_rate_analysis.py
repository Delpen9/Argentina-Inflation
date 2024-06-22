import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import seaborn as sns

import warnings

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Attempt to set non-positive ylim on a log-scaled axis will be ignored.")
warnings.filterwarnings("ignore", category=pd.errors.SettingWithCopyWarning)

def plot_fertility_rate_over_time(
    input_filename: str = "../inputs/fertility_rate_data_worldwide.csv",
    output_file_path: str = "../outputs/fertility_rate_over_time.png",
) -> None:
    df_fertility_rates = pd.read_csv(input_filename)

    df_argentina_fertility_rates = df_fertility_rates.loc[
        df_fertility_rates["Country Name"] == "Argentina"
    ]
    df_usa_fertility_rates = df_fertility_rates.loc[
        df_fertility_rates["Country Name"] == "United States"
    ]
    df_south_africa_fertility_rates = df_fertility_rates.loc[
        df_fertility_rates["Country Name"] == "South Africa"
    ]

    df_argentina_fertility_rates.drop(
        ["Country Name", "Country Code", "Indicator Name", "Indicator Code", "Unnamed: 68"],
        axis=1,
        inplace=True,
    )

    df_usa_fertility_rates.drop(
        ["Country Name", "Country Code", "Indicator Name", "Indicator Code", "Unnamed: 68"],
        axis=1,
        inplace=True,
    )

    df_south_africa_fertility_rates.drop(
        ["Country Name", "Country Code", "Indicator Name", "Indicator Code", "Unnamed: 68"],
        axis=1,
        inplace=True,
    )

    years = df_argentina_fertility_rates.columns.values.astype(float).tolist()

    row_index = 0
    argentina = df_argentina_fertility_rates.iloc[row_index].tolist()
    united_states = df_usa_fertility_rates.iloc[row_index].tolist()
    south_africa = df_south_africa_fertility_rates.iloc[row_index].tolist()

    # Plotting the df_cpi
    plt.figure(figsize=(16, 8))

    plt.plot(years, argentina, label="Argentina", marker="o")
    plt.plot(years, united_states, label="United States", marker="o")
    plt.plot(years, south_africa, label="South Africa", marker="o")

    # Customizing the y-axis to avoid scientific notation
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.gca().yaxis.get_major_formatter().set_scientific(False)

    plt.title("Fertility Rate Over Time", fontsize=20, fontweight='bold')
    plt.xlabel("Year", fontsize=20, fontweight='bold')
    plt.ylabel("Fertility Rate", fontsize=20, fontweight='bold')
    plt.legend()

    plt.grid(True, which="both", ls="--")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_file_path)


if __name__ == "__main__":
    plot_fertility_rate_over_time()
