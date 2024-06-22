import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import seaborn as sns


def plot_fiscal_deficit_as_perc_of_gdp(
    input_filename: str = "../inputs/argentina_fiscal_deficit.csv",
    output_file_path: str = "../outputs/fiscal_deficit_lineplot.png",
) -> None:
    df_fiscal_deficit = pd.read_csv(input_filename)

    years = df_fiscal_deficit["Date"].astype(int)
    argentina = df_fiscal_deficit[r"Deficit (%GDP)"].str.replace("%", "").astype(float)

    # Plotting the df_cpi
    plt.figure(figsize=(16, 8))

    plt.plot(years, argentina, label=r"Fiscal Deficit as % of GDP", marker="o")

    # Customizing the y-axis to avoid scientific notation
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.gca().yaxis.get_major_formatter().set_scientific(False)

    plt.title(f"Argentina Fiscal Deficit by Year (% of GDP); Negative is BAD", fontsize=20, fontweight='bold')
    plt.xlabel("Year", fontsize=20, fontweight='bold')
    plt.ylabel("Fiscal Deficit (%)", fontsize=20, fontweight='bold')
    plt.legend()

    plt.grid(True, which="both", ls="--")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_file_path)

def plot_cumulative_fiscal_deficit(
    input_filename: str = "../inputs/argentina_fiscal_deficit.csv",
    output_file_path: str = "../outputs/cumulative_fiscal_deficit_lineplot.png",
) -> None:
    df_fiscal_deficit = pd.read_csv(input_filename)

    years = df_fiscal_deficit["Date"].astype(int)
    df_fiscal_deficit[r"Deficit ($M)"] = df_fiscal_deficit[r"Deficit ($M)"].astype(float)

    df_fiscal_deficit[r"Cumulative Deficit ($B)"] = df_fiscal_deficit[r"Deficit ($M)"][::-1].cumsum()[::-1] / 1000

    argentina = df_fiscal_deficit[r"Cumulative Deficit ($B)"]

    # Plotting the df_cpi
    plt.figure(figsize=(16, 8))

    plt.plot(years, argentina, label=r"Cumulative Fiscal Deficit ($B)", marker="o")

    # Customizing the y-axis to avoid scientific notation
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.gca().yaxis.get_major_formatter().set_scientific(False)

    plt.title("Argentina Cumulative Fiscal Deficit by Year ($B)", fontsize=20, fontweight='bold')
    plt.xlabel("Year", fontsize=20, fontweight='bold')
    plt.ylabel("Fiscal Deficit ($B)", fontsize=20, fontweight='bold')
    plt.legend()

    plt.grid(True, which="both", ls="--")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_file_path)

if __name__ == "__main__":
    plot_fiscal_deficit_as_perc_of_gdp()
    plot_cumulative_fiscal_deficit()
