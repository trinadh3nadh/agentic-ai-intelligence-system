import pandas as pd


def analyze_dataset(file):

    if file.name.endswith(".csv"):

        df = pd.read_csv(file)

    elif file.name.endswith(".tsv"):

        df = pd.read_csv(file, sep="\t")

    elif file.name.endswith(".xlsx"):

        df = pd.read_excel(file)

    else:

        return None, "Unsupported file format"

    # prevent memory crashes
    if len(df) > 5000:

        df = df.sample(5000)

    insights = f"""
Dataset has {df.shape[0]} rows and {df.shape[1]} columns.

Main columns:
{list(df.columns[:10])}
"""

    return df, insights