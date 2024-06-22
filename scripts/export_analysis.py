import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import seaborn as sns


def plot_export_percent_over_time(
    input_filename: str = "../inputs/historical-argentina-exports.csv",
    output_file_path: str = "../outputs/export_percentage_of_gdp_over_time.png",
) -> None:
    df_export_perc = pd.read_csv(input_filename)

    years = df_export_perc["Year"]
    argentina = df_export_perc[r" % of GDP"]

    # Plotting the df_cpi
    plt.figure(figsize=(16, 8))

    plt.plot(years, argentina, label="Argentina", marker="o")

    # Customizing the y-axis to avoid scientific notation
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.gca().yaxis.get_major_formatter().set_scientific(False)

    plt.title("Export as Percent of GDP Over Time", fontsize=20, fontweight='bold')
    plt.xlabel("Year", fontsize=20, fontweight='bold')
    plt.ylabel(r"% of GDP Being Exports", fontsize=20, fontweight='bold')
    plt.legend()

    plt.grid(True, which="both", ls="--")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_file_path)


if __name__ == "__main__":
    plot_export_percent_over_time()
