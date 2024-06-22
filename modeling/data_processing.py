import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import seaborn as sns

from functools import reduce


def construct_training_data() -> None:
    ############################################################################
    ## File One
    ############################################################################
    argentina_age_filename = "../inputs/argentina_age_demographic.csv"

    # Read the CSV file
    df_argentina_ages = pd.read_csv(argentina_age_filename)

    # Convert percentages to floats
    age_columns = df_argentina_ages.columns[3:]
    for col in age_columns:
        df_argentina_ages[col] = (
            df_argentina_ages[col].str.rstrip("%").astype("float") / 100.0
        )

    df_argentina_ages["Years"] = df_argentina_ages["Years"].astype(int)
    ############################################################################
    ############################################################################

    ############################################################################
    ## File Two
    ############################################################################
    argentina_cpi_filename = "../inputs/cpi_inflation_data.csv"

    df_cpi = pd.read_csv(argentina_cpi_filename)

    df_cpi["USA Yearly Inflation"] = 1 + (df_cpi["USA"] / 100)

    df_cpi["USA Future Value"] = (
        1 / df_cpi["USA Yearly Inflation"][::-1].cumprod()[::-1]
    )

    df_cpi = df_cpi.rename(
        columns={
            "Year": "Years",
        }
    )
    df_cpi["Years"] = df_cpi["Years"].astype(int)
    ############################################################################
    ############################################################################

    ############################################################################
    ## File Three
    ############################################################################
    argentina_exchange_filename = "../inputs/argentine_peso_to_usd_exchange_rate.csv"

    df_exchange_rate = pd.read_csv(argentina_exchange_filename)

    df_exchange_rate["Yearly Avg Exchange Rate"] = (
        df_exchange_rate.iloc[:, 1:].astype(float).mean(axis=1)
    )

    df_exchange_rate = df_exchange_rate.rename(
        columns={
            "Year": "Years",
        }
    )[["Years", "Yearly Avg Exchange Rate"]]

    df_exchange_rate["Years"] = df_exchange_rate["Years"].astype(int)
    ############################################################################
    ############################################################################

    ############################################################################
    ## File Four
    ############################################################################
    argentina_exports_filename = "../inputs/historical-argentina-exports.csv"

    df_export_perc = pd.read_csv(argentina_exports_filename)

    df_export_perc = df_export_perc.rename(
        columns={
            "Year": "Years",
        }
    )
    df_export_perc["Years"] = df_export_perc["Years"].astype(int)
    ############################################################################
    ############################################################################

    ############################################################################
    ## File Five
    ############################################################################
    # Step 1: Read the CSV file
    argentina_fertility_filename = "../inputs/fertility_rate_data_worldwide.csv"
    df_fertility_rates = pd.read_csv(argentina_fertility_filename)

    # Step 2: Filter the data for Argentina
    df_argentina_fertility_rates = df_fertility_rates.loc[
        df_fertility_rates["Country Name"] == "Argentina"
    ]

    # Step 3: Drop unnecessary columns
    df_argentina_fertility_rates.drop(
        [
            "Country Name",
            "Country Code",
            "Indicator Name",
            "Indicator Code",
            "Unnamed: 68",
        ],
        axis=1,
        inplace=True,
    )

    # Step 4: Extract the years and fertility rates
    years = df_argentina_fertility_rates.columns.values.astype(int).tolist()
    row_index = 0
    argentina_fertility_rates = df_argentina_fertility_rates.iloc[row_index].tolist()

    # Step 5: Create a new DataFrame from the extracted data
    df_fertility = pd.DataFrame(
        {"Years": years, "Fertility Rate": argentina_fertility_rates}
    )
    ############################################################################
    ############################################################################

    ############################################################################
    ## File Six
    ############################################################################
    argentina_fiscal_deficit_filename = "../inputs/argentina_fiscal_deficit.csv"

    df_fiscal_deficit = pd.read_csv(argentina_fiscal_deficit_filename)

    df_fiscal_deficit[r"Deficit (%GDP)"] = (
        df_fiscal_deficit[r"Deficit (%GDP)"].str.replace("%", "").astype(float)
    )

    df_fiscal_deficit = df_fiscal_deficit.rename(columns={"Date": "Years"})
    df_fiscal_deficit["Years"] = df_fiscal_deficit["Years"].astype(int)
    ############################################################################
    ############################################################################

    ############################################################################
    ## File Seven
    ############################################################################
    argentina_gdp_filename = (
        "../inputs/Gross domestic product per capita in Argentina.csv"
    )

    df_gdp = pd.read_csv(argentina_gdp_filename)[
        ["Variable observation date", "Variable observation value"]
    ].rename(
        columns={
            "Variable observation date": "Years",
            "Variable observation value": "Nominal GDP",
        }
    )

    df_gdp = df_gdp.merge(df_cpi, on="Years", how="inner")

    df_gdp["Inflation Adjusted GDP"] = (
        df_gdp["Nominal GDP"] * df_gdp["USA Future Value"]
    )

    df_gdp["Years"] = df_gdp["Years"].astype(int)
    ############################################################################
    ############################################################################

    ############################################################################
    ## File Eight
    ############################################################################
    argentina_per_capita_filename = "../inputs/per_capita_income_in_argentina.csv"

    df_per_capita_income = pd.read_csv(argentina_per_capita_filename)

    df_per_capita_income = df_per_capita_income.rename(
        columns={
            "Year": "Years",
        }
    )

    df_per_capita_income["Years"] = df_per_capita_income["Years"].astype(int)
    ############################################################################
    ############################################################################

    ############################################################################
    ## File Nine
    ############################################################################
    argentina_poverty_levels = "../inputs/argentina-poverty-levels.csv"

    df_argentina_poverty = pd.read_csv(argentina_poverty_levels)

    df_argentina_poverty = df_argentina_poverty.rename(
        columns={
            "Year": "Years",
        }
    )

    df_argentina_poverty["Years"] = df_argentina_poverty["Years"].astype(int)
    ############################################################################
    ############################################################################

    ############################################################################
    ## Combine Data
    ############################################################################
    # List of dataframes to be merged
    dfs = [
        df_argentina_ages,
        df_exchange_rate,
        df_export_perc,
        df_fertility,
        df_fiscal_deficit,
        df_gdp,
        df_per_capita_income,
        df_argentina_poverty,
    ]

    # Initialize the final dataframe with the first dataframe in the list
    df_final = dfs[0]

    # Loop through the remaining dataframes and merge them
    for df in dfs[1:]:
        df_final = pd.merge(df_final, df, on="Years", how="outer")

    # Filter the rows and reset the index
    df_final = df_final.loc[
        (df_final["Years"] >= 1980) & (df_final["Years"] <= 2022)
    ].reset_index(drop=True)

    df_final = df_final.ffill().bfill()

    # Save the final dataframe to a CSV file
    df_final.to_csv("training_data.csv", index=False)
    ############################################################################
    ############################################################################


if __name__ == "__main__":
    construct_training_data()
