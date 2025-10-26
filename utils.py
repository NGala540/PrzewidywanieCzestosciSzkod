from tabulate import tabulate
import numpy as np
import pandas as pd

# eksploracja wartości odstających
def find_outliers(df: pd.DataFrame, threshold=1.5, method="IQR"):
    '''
    Wykrywa wartości odstające w danych liczbowych DataFrame przy użyciu metody rozstępu międzykwartylowego (IQR) lub z-score.
    Wyświetla podsumowanie wykrytych wartości odstających dla każdej kolumny numerycznej.

    df (pd.DataFrame): DataFrame, w którym wykrywane są wartości odstające
    threshold (float, domyślnie=1.5): Mnożnik dla IQR lub liczba odchyleń standardowych dla z-score.
    method (str, domyślnie="IQR"): Metoda wykrywania wartości odstających ("IQR" lub "z_score").
    '''

    # select only numerical columns
    numeric_df = df.select_dtypes(include=[np.number])

    # deklaracja wierszy do podsumowania
    results = {
        "Granice (Min / Max)": [],
        "Liczba odstających": [],
        "Udział odstających [%]": [],
        "Powyżej górnej granicy": [],
        "Poniżej dolnej granicy": []
    }

    # caluculating otliers based on choosen method
    if method == "IQR":
        q1s = numeric_df.quantile(0.25)
        q3s = numeric_df.quantile(0.75)
        IQRs = q3s - q1s

        min_bounds = q1s - threshold * IQRs
        max_bounds = q3s + threshold * IQRs
    elif method == "z_score":
        means = numeric_df.mean()
        stds = numeric_df.std()
        
        min_bounds = means - threshold * stds
        max_bounds = means + threshold * stds
    else:
        raise ValueError("valid method values are: [IQR, z_score]")

    # wypełnianie ramki podsumowania
    column_names = []
    for col in numeric_df.columns:
        min_bond = min_bounds[col]
        max_bond = max_bounds[col]

        outliers = numeric_df[col]
        outliers_mask = (outliers < min_bond) | (outliers > max_bond)
        outliers_count = outliers_mask.sum()

        column_names.append(col)
        results["Granice (Min / Max)"].append(f"{min_bond:.3f} / {max_bond:.3f}")
        results["Liczba odstających"].append(outliers_count)
        results["Udział odstających [%]"].append(round(100*outliers_count/df.shape[0],2))
        results["Powyżej górnej granicy"].append((outliers > max_bond).sum())
        results["Poniżej dolnej granicy"].append((outliers < min_bond).sum())

    # wyświetlanie podsumowania wartości odstających, jeśli występują
    if results["Liczba odstających"]:
        df_results = pd.DataFrame(results, index=column_names).T
        print(f"Wartości odstające wykryte metodą {method} z parametrem {threshold}:\n")
        print(tabulate(df_results, headers="keys"))
        print("\n")
    else:
        print("Nie znaleziono wartości odstających.")