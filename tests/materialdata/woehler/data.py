from io import StringIO
import numpy as np
import pandas as pd

data = pd.DataFrame(np.array([
        [4.50e+02, 3.40e+04],
        [4.50e+02, 5.40e+04],
        [4.50e+02, 6.00e+04],
        [4.50e+02, 7.60e+04],
        [4.00e+02, 5.30e+04],
        [4.00e+02, 9.40e+04],
        [4.00e+02, 2.07e+05],
        [4.00e+02, 2.27e+05],
        [3.75e+02, 6.80e+04],
        [3.75e+02, 2.34e+05],
        [3.75e+02, 3.96e+05],
        [3.75e+02, 5.00e+05],
        [3.75e+02, 6.00e+05],
        [3.75e+02, 7.09e+05],
        [3.50e+02, 1.70e+05],
        [3.50e+02, 1.87e+05],
        [3.50e+02, 2.20e+05],
        [3.50e+02, 2.89e+05],
        [3.50e+02, 3.09e+05],
        [3.50e+02, 1.00e+07],
        [3.25e+02, 6.75e+05],
        [3.25e+02, 7.51e+05],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.00e+02, 8.95e+05],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07]
]), columns=['load', 'cycles']).sample(frac=1)

data_no_mixed_horizons = pd.DataFrame(np.array([
        [4.50e+02, 3.40e+04],
        [4.50e+02, 5.40e+04],
        [4.50e+02, 6.00e+04],
        [4.50e+02, 7.60e+04],
        [4.00e+02, 5.30e+04],
        [4.00e+02, 9.40e+04],
        [4.00e+02, 2.07e+05],
        [4.00e+02, 2.27e+05],
        [3.75e+02, 6.80e+04],
        [3.75e+02, 2.34e+05],
        [3.75e+02, 3.96e+05],
        [3.75e+02, 5.00e+05],
        [3.75e+02, 6.00e+05],
        [3.75e+02, 7.09e+05],
        [3.50e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07]
]), columns=['load', 'cycles']).sample(frac=1)

no_mixed_horizons_finite_expected = pd.DataFrame(np.array([
        [4.50e+02, 3.40e+04],
        [4.50e+02, 5.40e+04],
        [4.50e+02, 6.00e+04],
        [4.50e+02, 7.60e+04],
        [4.00e+02, 5.30e+04],
        [4.00e+02, 9.40e+04],
        [4.00e+02, 2.07e+05],
        [4.00e+02, 2.27e+05],
        [3.75e+02, 6.80e+04],
        [3.75e+02, 2.34e+05],
        [3.75e+02, 3.96e+05],
        [3.75e+02, 5.00e+05],
        [3.75e+02, 6.00e+05],
        [3.75e+02, 7.09e+05],
]), columns=['load', 'cycles'])

no_mixed_horizons_infinite_expected = pd.DataFrame(np.array([
        [3.50e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07]
]), columns=['load', 'cycles'])

data_pure_runout_horizon_and_mixed_horizons = pd.DataFrame(np.array([
        [4.50e+02, 3.40e+04],
        [4.50e+02, 5.40e+04],
        [4.50e+02, 6.00e+04],
        [4.50e+02, 7.60e+04],
        [4.00e+02, 5.30e+04],
        [4.00e+02, 9.40e+04],
        [4.00e+02, 2.07e+05],
        [4.00e+02, 2.27e+05],
        [3.75e+02, 6.80e+04],
        [3.75e+02, 2.34e+05],
        [3.75e+02, 3.96e+05],
        [3.75e+02, 5.00e+05],
        [3.75e+02, 6.00e+05],
        [3.75e+02, 7.09e+05],
        [3.50e+02, 1.70e+05],
        [3.50e+02, 1.87e+05],
        [3.50e+02, 2.20e+05],
        [3.50e+02, 2.89e+05],
        [3.50e+02, 3.09e+05],
        [3.50e+02, 1.00e+07],
        [3.25e+02, 6.75e+05],
        [3.25e+02, 7.51e+05],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07]
]), columns=['load', 'cycles']).sample(frac=1)

pure_runout_horizon_and_mixed_horizons_finite_expected = pd.DataFrame(np.array([
        [4.50e+02, 3.40e+04],
        [4.50e+02, 5.40e+04],
        [4.50e+02, 6.00e+04],
        [4.50e+02, 7.60e+04],
        [4.00e+02, 5.30e+04],
        [4.00e+02, 9.40e+04],
        [4.00e+02, 2.07e+05],
        [4.00e+02, 2.27e+05],
        [3.75e+02, 6.80e+04],
        [3.75e+02, 2.34e+05],
        [3.75e+02, 3.96e+05],
        [3.75e+02, 5.00e+05],
        [3.75e+02, 6.00e+05],
        [3.75e+02, 7.09e+05]
    ]), columns=['load', 'cycles'])

pure_runout_horizon_and_mixed_horizons_infinite_expected = pd.DataFrame(np.array([
        [3.50e+02, 1.70e+05],
        [3.50e+02, 1.87e+05],
        [3.50e+02, 2.20e+05],
        [3.50e+02, 2.89e+05],
        [3.50e+02, 3.09e+05],
        [3.50e+02, 1.00e+07],
        [3.25e+02, 6.75e+05],
        [3.25e+02, 7.51e+05],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07]
]), columns=['load', 'cycles'])

pure_runout_horizon_and_mixed_horizons_finite_expected_conservative = pd.DataFrame(np.array([
        [4.50e+02, 3.40e+04],
        [4.50e+02, 5.40e+04],
        [4.50e+02, 6.00e+04],
        [4.50e+02, 7.60e+04],
        [4.00e+02, 5.30e+04],
        [4.00e+02, 9.40e+04],
        [4.00e+02, 2.07e+05],
        [4.00e+02, 2.27e+05],
        [3.75e+02, 6.80e+04],
        [3.75e+02, 2.34e+05],
        [3.75e+02, 3.96e+05],
        [3.75e+02, 5.00e+05],
        [3.75e+02, 6.00e+05],
        [3.75e+02, 7.09e+05],
    ]), columns=['load', 'cycles'])

pure_runout_horizon_and_mixed_horizons_infinite_expected_conservative = pd.DataFrame(np.array([
        [3.50e+02, 1.70e+05],
        [3.50e+02, 1.87e+05],
        [3.50e+02, 2.20e+05],
        [3.50e+02, 2.89e+05],
        [3.50e+02, 3.09e+05],
        [3.50e+02, 1.00e+07],
        [3.25e+02, 6.75e+05],
        [3.25e+02, 7.51e+05],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07],
        [2.90e+02, 1.00e+07]
]), columns=['load', 'cycles'])

data_no_runouts = pd.DataFrame(np.array([
        [4.50e+02, 3.40e+04],
        [4.50e+02, 5.40e+04],
        [4.50e+02, 6.00e+04],
        [4.50e+02, 7.60e+04],
        [4.00e+02, 5.30e+04],
        [4.00e+02, 9.40e+04],
        [4.00e+02, 2.07e+05],
        [4.00e+02, 2.27e+05],
        [3.75e+02, 6.80e+04],
        [3.75e+02, 2.34e+05],
        [3.75e+02, 3.96e+05],
        [3.75e+02, 5.00e+05],
        [3.75e+02, 6.00e+05],
        [3.75e+02, 7.09e+05],
        [3.50e+02, 1.70e+05],
        [3.50e+02, 1.87e+05],
        [3.50e+02, 2.20e+05],
        [3.50e+02, 2.89e+05],
        [3.50e+02, 3.09e+05],
        [3.25e+02, 6.75e+05],
        [3.25e+02, 7.51e+05],
]), columns=['load', 'cycles']).sample(frac=1)

no_runouts_infinite_expected = data_no_runouts[:0]
no_runouts_finite_expected = data_no_runouts

data_only_runout_levels = pd.DataFrame(np.array([
        [3.50e+02, 1.70e+05],
        [3.50e+02, 1.87e+05],
        [3.50e+02, 2.20e+05],
        [3.50e+02, 2.89e+05],
        [3.50e+02, 1.00e+07],
        [3.50e+02, 1.00e+07],
        [3.25e+02, 6.75e+05],
        [3.25e+02, 7.51e+05],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.00e+02, 8.95e+05],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07]
]), columns=['load', 'cycles']).sample(frac=1)

only_runout_levels_infinite_expected = data_only_runout_levels
only_runout_levels_finite_expected = data_only_runout_levels[:0]


data_one_runout_load_level = pd.DataFrame(np.array([
    [3.5000e+02, 8.5930e+05],
    [3.5000e+02, 6.5720e+05],
    [3.5000e+02, 5.8650e+05],
    [3.5000e+02, 1.3085e+06],
    [3.5000e+02, 1.4485e+06],
    [3.0000e+02, 1.0000e+07],
    [3.0000e+02, 1.0000e+07],
    [3.0000e+02, 1.0000e+07],
    [3.0000e+02, 1.0000e+07],
    [3.0000e+02, 1.0000e+07],
    [4.5000e+02, 3.2600e+05],
    [4.5000e+02, 2.6280e+05],
    [4.5000e+02, 1.3200e+05],
    [4.5000e+02, 1.9310e+05],
    [4.5000e+02, 2.5670e+05],
    [3.2500e+02, 2.2402e+06],
    [3.2500e+02, 1.1630e+06],
    [3.2500e+02, 1.2132e+06],
    [3.2500e+02, 1.0347e+06],
    [3.2500e+02, 2.2683e+06]
]), columns=['load', 'cycles']).sample(frac=1)


load_sorted = pd.Series(np.array([
        4.50e+02, 4.50e+02, 4.50e+02, 4.50e+02, 4.00e+02, 4.00e+02, 4.00e+02, 4.00e+02, 3.75e+02, 3.75e+02,
        3.75e+02, 3.75e+02, 3.75e+02, 3.75e+02, 3.50e+02, 3.50e+02, 3.50e+02, 3.50e+02, 3.50e+02, 3.50e+02,
        3.25e+02, 3.25e+02, 3.25e+02, 3.25e+02, 3.25e+02, 3.25e+02, 3.25e+02, 3.25e+02, 3.25e+02, 3.25e+02,
        3.00e+02, 3.00e+02, 3.00e+02, 3.00e+02, 3.00e+02, 3.00e+02, 3.00e+02, 3.00e+02, 3.00e+02, 3.00e+02]), name='load').sort_values()

cycles_sorted = pd.Series(np.array([
        3.40e+04, 5.40e+04, 6.00e+04, 7.60e+04, 5.30e+04, 9.40e+04, 2.07e+05, 2.27e+05, 6.80e+04, 2.34e+05,
        3.96e+05, 5.00e+05, 6.00e+05, 7.09e+05, 1.70e+05, 1.87e+05, 2.20e+05, 2.89e+05, 3.09e+05, 1.00e+07,
        6.75e+05, 7.51e+05, 1.00e+07, 1.00e+07, 1.00e+07, 1.00e+07, 1.00e+07, 1.00e+07, 1.00e+07, 1.00e+07,
        8.95e+05, 1.00e+07, 1.00e+07, 1.00e+07, 1.00e+07, 1.00e+07, 1.00e+07, 1.00e+07, 1.00e+07, 1.00e+07]), name='cycles').sort_values()

finite_expected = pd.DataFrame(np.array([
        [4.50e+02, 3.40e+04],
        [4.50e+02, 5.40e+04],
        [4.50e+02, 6.00e+04],
        [4.50e+02, 7.60e+04],
        [4.00e+02, 5.30e+04],
        [4.00e+02, 9.40e+04],
        [4.00e+02, 2.07e+05],
        [4.00e+02, 2.27e+05],
        [3.75e+02, 6.80e+04],
        [3.75e+02, 2.34e+05],
        [3.75e+02, 3.96e+05],
        [3.75e+02, 5.00e+05],
        [3.75e+02, 6.00e+05],
        [3.75e+02, 7.09e+05],
]), columns=['load', 'cycles']).sort_values(by='load').reset_index(drop=True)

infinite_expected = pd.DataFrame(np.array([
        [3.50e+02, 1.70e+05],
        [3.50e+02, 1.87e+05],
        [3.50e+02, 2.20e+05],
        [3.50e+02, 2.89e+05],
        [3.50e+02, 3.09e+05],
        [3.50e+02, 1.00e+07],
        [3.25e+02, 6.75e+05],
        [3.25e+02, 7.51e+05],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.00e+02, 8.95e+05],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07]
]), columns=['load', 'cycles']).sort_values(by='load').reset_index(drop=True)

finite_expected_conservative = pd.DataFrame(np.array([
        [4.50e+02, 3.40e+04],
        [4.50e+02, 5.40e+04],
        [4.50e+02, 6.00e+04],
        [4.50e+02, 7.60e+04],
        [4.00e+02, 5.30e+04],
        [4.00e+02, 9.40e+04],
        [4.00e+02, 2.07e+05],
        [4.00e+02, 2.27e+05],
        [3.75e+02, 6.80e+04],
        [3.75e+02, 2.34e+05],
        [3.75e+02, 3.96e+05],
        [3.75e+02, 5.00e+05],
        [3.75e+02, 6.00e+05],
        [3.75e+02, 7.09e+05],
]), columns=['load', 'cycles']).sort_values(by='load').reset_index(drop=True)

infinite_expected_conservative = pd.DataFrame(np.array([
        [3.50e+02, 1.70e+05],
        [3.50e+02, 1.87e+05],
        [3.50e+02, 2.20e+05],
        [3.50e+02, 2.89e+05],
        [3.50e+02, 3.09e+05],
        [3.50e+02, 1.00e+07],
        [3.25e+02, 6.75e+05],
        [3.25e+02, 7.51e+05],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.25e+02, 1.00e+07],
        [3.00e+02, 8.95e+05],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07],
        [3.00e+02, 1.00e+07]
]), columns=['load', 'cycles']).sort_values(by='load').reset_index(drop=True)


data_01 = pd.DataFrame({"load": np.array([620, 620, 620, 550, 550, 500, 500, 500, 500, 500, 480, 480]), "cycles": np.array(
    [65783, 89552, 115800, 141826, 190443, 293418, 383341, 525438, 967091, 99505992, 99524024, 199563776])})
data_01_no_pure_runout_horizon = data_01[data_01.load > 480]
data_01_two_fractures = pd.DataFrame({"load": np.array([620, 550,480]), "cycles": np.array([65783, 141826,199563776])})
data_01_one_fracture_level = data_01[data_01.load > 550]


def read_data(s, thres=1e6):
    d = pd.read_csv(StringIO(s), sep="\t", comment="#", names=['cycles', 'load'])
    d.N_threshold = thres
    return d


data_neg_res_1 = read_data("""
127700	450
108000	450
124000	450
127000	450
101000	450
199000	400
213600	400
166000	400
146000	400
140600	400
295000	350
264000	350
330000	350
352000	350
438000	350
645600	300
412000	300
772000	300
501200	300
593600	300
1856000	250
1989900	250
2114500	250
1121400	250
1233600	250
10000000	200
5131700	200
3857300	200
9620900	175
7634000	175
10000000	175
10000000	175
10000000	175""", 10000000)

data_neg_res_2 = read_data("""
109000	377.556025
51000	377.556025
75000	377.556025
111000	377.556025
140000	377.556025
128000	362.84605
75000	362.84605
109000	362.84605
83000	362.84605
68000	362.84605
132000	362.84605
253000	333.4261
987000	333.4261
246000	333.4261
224000	333.4261
159000	333.4261
10000000	304.00615
4576000	304.00615
2139000	304.00615
10000000	304.00615
4576000	304.00615
1191000	289.296175
10000000	289.296175
6337000	289.296175
10000000	289.296175
10000000	289.296175""", 10000000)

all_data = [
    data,
    data_neg_res_1,
    data_neg_res_2
]
