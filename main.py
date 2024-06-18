from scripts.cpi_analysis import (
    plot_cpi_df_cpi,
    get_currency_valuation_by_region,
    get_currency_valuation_by_region_excluding_argentina,
)

from scripts.household_income_analysis import (
    plot_household_income,
)

from scripts.poverty_levels_analysis import (
    plot_poverty_levels,
)

if __name__ == "__main__":
    plot_cpi_df_cpi(
        input_filename="inputs/cpi_inflation_data.csv",
        output_file_path="outputs/cpi_display_lineplot.png",
    )
    get_currency_valuation_by_region(
        input_filename="inputs/cpi_inflation_data.csv",
        output_file_path="outputs/currency_valuation_over_time.png",
    )
    get_currency_valuation_by_region_excluding_argentina(
        input_filename="inputs/cpi_inflation_data.csv",
        output_file_path="outputs/currency_valuation_over_time_excluding_argentina.png",
    )

    plot_household_income(
        input_filename="inputs/per_capita_income_in_argentina.csv",
        output_file_path="outputs/household_purchasing_power_in_argentina.png",
    )

    plot_poverty_levels(
        input_filename="inputs/argentina-poverty-levels.csv",
        output_file_path="outputs/argentina_poverty_levels.png",
    )
