import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import seaborn as sns


def plot_inflation_adjusted_gdp(
    input_filename_one: str = "../inputs/cpi_inflation_data.csv",
    input_filename_two: str = "../inputs/Gross domestic product per capita in Argentina.csv",
    output_file_path: str = "../outputs/gross_domestic_weighted_inflation_lineplot.png",
) -> None:
    df_cpi = pd.read_csv(input_filename_one)

    df_gdp = pd.read_csv(input_filename_two)[
        ["Variable observation date", "Variable observation value"]
    ].rename(columns={
        "Variable observation date": "Year",
        "Variable observation value": "Nominal GDP",
    })

    df_gdp["Year"] = df_gdp["Year"].astype(
        int
    )

    df_cpi["USA Yearly Inflation"] = 1 + (df_cpi["USA"] / 100)

    df_cpi["USA Future Value"] = 1 / df_cpi["USA Yearly Inflation"][
        ::-1
    ].cumprod()[::-1]

    df_gdp = df_gdp.merge(df_cpi, on="Year", how="inner")

    df_gdp["Inflation Adjusted GDP"] = (
        df_gdp["Nominal GDP"] * df_gdp["USA Future Value"]
    )

    years = df_gdp["Year"]
    argentina_inflation_gdp = df_gdp["Inflation Adjusted GDP"]
    argentina_nominal_gdp = df_gdp["Nominal GDP"]

    # Plotting the df_cpi
    plt.figure(figsize=(16, 8))

    plt.plot(years, argentina_inflation_gdp, label="Inflation Adjusted Argentina GDP", marker="o")
    plt.plot(years, argentina_nominal_gdp, label="Nominal Argentina GDP", marker="o")

    # Customizing the y-axis to avoid scientific notation
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.gca().yaxis.get_major_formatter().set_scientific(False)

    plt.title("Argentina Gross Domestic Product per Capita by Year (USD)", fontsize=20, fontweight='bold')
    plt.xlabel("Year", fontsize=20, fontweight='bold')
    plt.ylabel("USD", fontsize=20, fontweight='bold')
    plt.legend()

    plt.grid(True, which="both", ls="--")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_file_path)

if __name__ == "__main__":
    plot_inflation_adjusted_gdp()