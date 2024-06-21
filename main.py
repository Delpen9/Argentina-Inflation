from scripts.cpi_analysis import (
    plot_cpi_inflation,
    get_currency_valuation_by_region,
    get_currency_valuation_by_region_excluding_argentina,
)

from scripts.household_income_analysis import (
    plot_household_income,
)

from scripts.poverty_levels_analysis import (
    plot_poverty_levels,
)

from scripts.gross_domestic_product_analysis import (
    plot_inflation_adjusted_gdp
)

from scripts.fiscal_deficit_analysis import (
    plot_fiscal_deficit_as_perc_of_gdp,
    plot_cumulative_fiscal_deficit,
)

if __name__ == "__main__":
    plot_cpi_inflation(
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

    plot_inflation_adjusted_gdp(
        input_filename_one="inputs/cpi_inflation_data.csv",
        input_filename_two="inputs/Gross domestic product per capita in Argentina.csv",
        output_file_path="outputs/gross_domestic_weighted_inflation_lineplot.png",
    )

    plot_fiscal_deficit_as_perc_of_gdp(
        input_filename="inputs/argentina_fiscal_deficit.csv",
        output_file_path="outputs/fiscal_deficit_lineplot.png",
    )

    plot_cumulative_fiscal_deficit(
        input_filename="inputs/argentina_fiscal_deficit.csv",
        output_file_path="outputs/cumulative_fiscal_deficit_lineplot.png",
    )