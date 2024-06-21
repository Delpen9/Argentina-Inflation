import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import seaborn as sns


def plot_exchange_rate_over_time(
    input_filename: str = "../inputs/argentine_peso_to_usd_exchange_rate.csv",
    output_file_path: str = "../outputs/exchange_rate_over_time.png",
) -> None:
    df_exchange_rate = pd.read_csv(input_filename)

    df_exchange_rate["Yearly Avg Exchange Rate"] = (
        df_exchange_rate.iloc[:, 1:].astype(float).mean(axis=1)
    )

    years = df_exchange_rate["Year"].astype(int)
    argentina = df_exchange_rate["Yearly Avg Exchange Rate"].astype(float)

    # Plotting the df_cpi
    plt.figure(figsize=(16, 8))

    plt.plot(years, argentina, label="Argentina", marker="o")

    plt.yscale("log", base=10)

    # Customizing the y-axis to avoid scientific notation
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.gca().yaxis.get_major_formatter().set_scientific(False)

    plt.title("Argentine Peso to USD Exchange Rate Over Time")
    plt.xlabel("Year")
    plt.ylabel(r"% of GDP Being Exports")
    plt.legend()

    plt.grid(True, which="both", ls="--")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_file_path)


if __name__ == "__main__":
    plot_exchange_rate_over_time()
