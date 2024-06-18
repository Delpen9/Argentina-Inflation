import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import seaborn as sns

def plot_poverty_levels(
    filename: str = "../inputs/argentina-poverty-levels.csv",
    output_file_path: str = "../outputs/argentina_poverty_levels.png"
) -> None:
    df_cpi = pd.read_csv(filename)

    years = df_cpi["Year"]
    argentina = df_cpi["% Under US $5.50 Per Day"]

    plt.figure(figsize=(16, 8))

    plt.plot(years, argentina, label="% Under US $5.50 Per Day", marker="o", color='royalblue', linestyle='-', linewidth=2)

    # Customizing the y-axis to avoid scientific notation and add commas
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.gca().yaxis.get_major_formatter().set_scientific(False)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:,.0f}'.format(x)))

    # Enhancing plot aesthetics
    plt.title("Argentina Poverty Levels as % Under US $5.50 Per Day", fontsize=20, fontweight='bold')
    plt.xlabel("Year", fontsize=14, fontweight='bold')
    plt.ylabel("% Under US $5.50 Per Day (Adjusted for USD 2011)", fontsize=14, fontweight='bold')
    plt.legend(fontsize=12)
    plt.grid(True, which="both", ls="--", lw=0.5, color='gray')
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    # Adding background color for better contrast
    plt.gca().set_facecolor('whitesmoke')

    # Adding value annotations
    for x, y in zip(years, argentina):
        plt.text(x, y, f'{y:,.0f}', fontsize=10, ha='right', va='bottom', color='black', rotation=45)

    plt.tight_layout()

    plt.savefig(output_file_path)

if __name__ == "__main__":
    plot_poverty_levels()