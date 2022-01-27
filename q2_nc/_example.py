import biom
import pandas as pd


def samples_of_interest(metadata: pd.DataFrame) -> pd.Series:
    column = 'host_tax_id'
    value = '9606'
    return (metadata[column] == value)
