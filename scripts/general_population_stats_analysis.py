import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import seaborn as sns


def plot_general_population_statistics(
    input_filename: str = "../inputs/general_population_data.csv",
    output_file_path: str = "../outputs/argentina_general_population_data.png",
) -> None:
    df_pop_stats = pd.read_csv(input_filename)

    years = df_pop_stats["Year"]
    argentina_birth_count = df_pop_stats["Births"]
    argentina_death_count = df_pop_stats["Deaths"]
    argentina_pop_count = df_pop_stats["Population"]
    argentina_pop_growth = df_pop_stats["Births"] - df_pop_stats["Deaths"]
    

    # Plotting the df_pop_stats
    plt.figure(figsize=(16, 8))

    plt.plot(
        years, argentina_birth_count, label="Argentina Yearly Birth Count", marker="o"
    )
    plt.plot(
        years, argentina_death_count, label="Argentina Yearly Death Count", marker="o"
    )
    plt.plot(
        years,
        argentina_pop_count,
        label="Argentina Yearly Population Count",
        marker="o",
    )
    plt.plot(
        years,
        argentina_pop_growth,
        label="Argentina Yearly Population Growth",
        marker="o",
    )

    plt.yscale("log", base=10)

    # Customizing the y-axis to avoid scientific notation
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.gca().yaxis.get_major_formatter().set_scientific(False)

    plt.title(
        "Birth, Death, and Population Counts by Year", fontsize=20, fontweight='bold'
    )
    plt.xlabel("Year", fontsize=20, fontweight='bold')
    plt.ylabel("Count", fontsize=20, fontweight='bold')
    plt.legend()

    plt.grid(True, which="both", ls="--")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_file_path)


if __name__ == "__main__":
    plot_general_population_statistics()
