import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import seaborn as sns


def plot_cpi_df_cpi(
    filename: str = "cpi_inflation_data.csv",
    output_file_path: str = "outputs/cpi_display_lineplot.png",
) -> None:
    df_cpi = pd.read_csv(filename)

    # Calculate the rolling average over 5 years
    df_cpi["Argentina"] = df_cpi["Argentina"].rolling(window=5).mean()
    df_cpi["EU"] = df_cpi["EU"].rolling(window=5).mean()
    df_cpi["USA"] = df_cpi["USA"].rolling(window=5).mean()
    df_cpi["World"] = df_cpi["World"].rolling(window=5).mean()

    years = df_cpi["Year"]
    argentina = df_cpi["Argentina"]
    eu = df_cpi["EU"]
    usa = df_cpi["USA"]
    world = df_cpi["World"]

    # Plotting the df_cpi
    plt.figure(figsize=(16, 8))

    plt.plot(years, argentina, label="Argentina", marker="o")
    plt.plot(years, eu, label="EU", marker="o")
    plt.plot(years, usa, label="USA", marker="o")
    plt.plot(years, world, label="World", marker="o")

    plt.yscale("log")
    plt.ylim([0, 2e3])

    # Customizing the y-axis to avoid scientific notation
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.gca().yaxis.get_major_formatter().set_scientific(False)

    plt.title("Inflation Rates Over Time (5-Year Rolling Average)")
    plt.xlabel("Year")
    plt.ylabel("Inflation %")
    plt.legend()

    plt.grid(True, which="both", ls="--")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_file_path)


def get_currency_valuation_by_region(
    filename: str = "cpi_inflation_data.csv",
    output_file_path: str = "outputs/currency_valuation_over_time.png",
) -> None:
    df_cpi = pd.read_csv(filename)

    # Get inflation values for cumprod()
    df_cpi["Argentina Yearly Inflation"] = 1 + (df_cpi["Argentina"] / 100)
    df_cpi["EU Yearly Inflation"] = 1 + (df_cpi["EU"] / 100)
    df_cpi["USA Yearly Inflation"] = 1 + (df_cpi["USA"] / 100)
    df_cpi["World Yearly Inflation"] = 1 + (df_cpi["World"] / 100)

    # Get the cumulative product
    df_cpi["Argentina Currency Valuation"] = df_cpi["Argentina Yearly Inflation"][
        ::-1
    ].cumprod()[::-1]
    df_cpi["EU Currency Valuation"] = df_cpi["EU Yearly Inflation"][::-1].cumprod()[
        ::-1
    ]
    df_cpi["USA Currency Valuation"] = df_cpi["USA Yearly Inflation"][::-1].cumprod()[
        ::-1
    ]
    df_cpi["World Currency Valuation"] = df_cpi["World Yearly Inflation"][
        ::-1
    ].cumprod()[::-1]

    years = df_cpi["Year"]
    argentina = df_cpi["Argentina Currency Valuation"]
    eu = df_cpi["EU Currency Valuation"]
    usa = df_cpi["USA Currency Valuation"]
    world = df_cpi["World Currency Valuation"]

    # Plotting the df_cpi
    plt.figure(figsize=(16, 8))

    plt.plot(years, argentina, label="Argentina", marker="o")
    plt.plot(years, eu, label="EU", marker="o")
    plt.plot(years, usa, label="USA", marker="o")
    plt.plot(years, world, label="World", marker="o")

    plt.yscale("log", base=10)
    plt.ylim([0, 2e10])

    # Customizing the y-axis to avoid scientific notation
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.gca().yaxis.get_major_formatter().set_scientific(False)
    plt.gca().yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, pos: "{:,.0f}".format(x))
    )

    plt.title("Amount of Currency Needed to Equal 1 of the Currency in 1979")
    plt.xlabel("Year")
    plt.ylabel("Amount Needed")
    plt.legend()

    plt.grid(True, which="both", ls="--")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_file_path)


def get_currency_valuation_by_region_excluding_argentina(
    filename: str = "cpi_inflation_data.csv",
    output_file_path: str = "outputs/currency_valuation_over_time_excluding_argentina.png",
) -> None:
    df_cpi = pd.read_csv(filename)

    # Get inflation values for cumprod()
    # df_cpi["Argentina Yearly Inflation"] = 1 + (df_cpi["Argentina"] / 100)
    df_cpi["EU Yearly Inflation"] = 1 + (df_cpi["EU"] / 100)
    df_cpi["USA Yearly Inflation"] = 1 + (df_cpi["USA"] / 100)
    df_cpi["World Yearly Inflation"] = 1 + (df_cpi["World"] / 100)

    # Get the cumulative product
    # df_cpi["Argentina Currency Valuation"] = df_cpi["Argentina Yearly Inflation"][::-1].cumprod()[::-1]
    df_cpi["EU Currency Valuation"] = df_cpi["EU Yearly Inflation"][::-1].cumprod()[
        ::-1
    ]
    df_cpi["USA Currency Valuation"] = df_cpi["USA Yearly Inflation"][::-1].cumprod()[
        ::-1
    ]
    df_cpi["World Currency Valuation"] = df_cpi["World Yearly Inflation"][
        ::-1
    ].cumprod()[::-1]

    years = df_cpi["Year"]
    # argentina = df_cpi["Argentina Currency Valuation"]
    eu = df_cpi["EU Currency Valuation"]
    usa = df_cpi["USA Currency Valuation"]
    world = df_cpi["World Currency Valuation"]

    # Plotting the df_cpi
    plt.figure(figsize=(16, 8))

    # plt.plot(years, argentina, label='Argentina', marker='o')
    plt.plot(years, eu, label="EU", marker="o")
    plt.plot(years, usa, label="USA", marker="o")
    plt.plot(years, world, label="World", marker="o")

    plt.yscale("log", base=10)
    plt.ylim([0, 1e1])

    # Customizing the y-axis to avoid scientific notation
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.gca().yaxis.get_major_formatter().set_scientific(False)
    plt.gca().yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, pos: "{:,.0f}".format(x))
    )

    plt.title("Amount of Currency Needed to Equal 1 of the Currency in 1979")
    plt.xlabel("Year")
    plt.ylabel("Amount Needed")
    plt.legend()

    plt.grid(True, which="both", ls="--")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_file_path)


if __name__ == "__main__":
    plot_cpi_df_cpi()
    get_currency_valuation_by_region()
    get_currency_valuation_by_region_excluding_argentina()
