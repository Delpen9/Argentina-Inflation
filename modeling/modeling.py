import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import itertools

import warnings

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


def adf_test(series, title=""):
    """
    Perform Augmented Dickey-Fuller test
    """
    print(f"Augmented Dickey-Fuller Test: {title}")
    result = adfuller(series.dropna(), autolag="AIC")
    labels = ["ADF test statistic", "p-value", "# lags used", "# observations"]
    out = dict(zip(labels, result))
    for key, val in out.items():
        print(f"{key}: {val}")
    if result[1] <= 0.05:
        print(
            "Strong evidence against the null hypothesis, reject the null hypothesis. Data has no unit root and is stationary."
        )
    else:
        print(
            "Weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary."
        )


def find_best_arima_order(series):
    """
    Find the best ARIMA order (p, d, q) based on AIC
    """
    p = d = q = range(0, 3)
    pdq = list(itertools.product(p, d, q))
    best_aic = np.inf
    best_order = None
    for order in pdq:
        try:
            model = ARIMA(series, order=order)
            model_fit = model.fit()
            if model_fit.aic < best_aic:
                best_aic = model_fit.aic
                best_order = order
        except:
            continue
    return best_order


def forecast_poverty_levels(
    data_path, target_column, forecast_years=10, confidence_interval=0.95
):
    # Load your data into a DataFrame
    data = pd.read_csv(data_path)

    # Ensure 'Years' is treated as integers and not dates
    data["Years"] = pd.to_numeric(data["Years"], errors="coerce")

    # Set 'Years' as the index
    data.set_index("Years", inplace=True)

    # Ensure all data is numeric
    data = data.apply(pd.to_numeric, errors="coerce")

    # Define target variable for prediction
    target = target_column

    # Use all available data to fit the model
    train = data[target]

    # Perform Augmented Dickey-Fuller test to check stationarity
    adf_test(train, title="Original Series")

    # Find the best ARIMA order
    best_order = find_best_arima_order(train)
    print(f"Best ARIMA order: {best_order}")

    # Fit the ARIMA model
    model = ARIMA(train, order=best_order)
    model_fit = model.fit()

    # Forecast future values
    forecast = model_fit.forecast(steps=forecast_years)

    # Create bootstrapped confidence intervals
    bootstraps = 1000
    boot_samples = np.random.choice(forecast, (bootstraps, len(forecast)))
    boot_conf_int = np.percentile(
        boot_samples,
        [(1 - confidence_interval) / 2 * 100, (1 + confidence_interval) / 2 * 100],
        axis=0,
    )

    # Generate future years
    last_year = data.index[-1]
    future_years = pd.date_range(
        start=f"{last_year}", periods=forecast_years + 1, freq="Y"
    )[1:].year

    # Plot the results
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data[target], label="Historical Poverty Levels")
    plt.plot(future_years, forecast, label="Forecasted Poverty Levels")
    plt.fill_between(
        future_years,
        boot_conf_int[0],
        boot_conf_int[1],
        color="gray",
        alpha=0.2,
        label=f"{int(confidence_interval*100)}% Confidence Interval",
    )
    plt.xlabel("Years")
    plt.ylabel(target)
    plt.legend()
    plt.savefig("modeling_prediction.png")

    # Save the results to CSV
    forecast_df = pd.DataFrame(
        {
            "Years": future_years,
            "Forecast": forecast,
            "Lower CI": boot_conf_int[0],
            "Upper CI": boot_conf_int[1],
        }
    )
    forecast_df.to_csv("forecasted_poverty_levels.csv", index=False)


if __name__ == "__main__":
    data_path = "training_data.csv"
    target_column = "% Under US $5.50 Per Day"
    forecast_poverty_levels(data_path, target_column)
