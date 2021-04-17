import pandas as pd
import numpy as np
import textwrap
from contextlib import contextmanager

cpp_file = open("include/xbow/country.hpp", "w")

COUNTRIES = ["DE", "NL", "FR", "IT", "GB", "AT", "CH", "SE", "ES", "BE", "DK", "FI", "PL", "NO"]

asf_countries = (
    pd.Series(COUNTRIES, index=list(range(len(COUNTRIES))))
        .to_frame("country")
        .reset_index()
        .rename(columns=dict(index="ix"))
)

all_countries = (
    pd.read_csv('resources/iso_country_codes.csv')
        .rename(columns=dict(Code="country", Name="name"))
)
all_countries.country = all_countries.country.astype('str')
all_countries.name = all_countries.name.astype('str')

countries = (
    all_countries
        .merge(asf_countries, on="country", how='left')
        .sort_values(["ix", "country"])
        .drop(columns=["ix"])
        .set_index("country")
        .reset_index()
)
countries = countries.loc[countries.country.str.lower() != "nan"]
countries['sk_country'] = list(range(len(countries)))
countries.sk_country = countries.sk_country.astype(np.uint16)
countries.country = countries.country.astype(str)
countries.name = countries.name.astype(str)

countries = countries.set_index("sk_country")

margin = 0


def emit(src: str) -> None:
    global margin
    print("\n".join(" "*margin + line for line in textwrap.dedent(src).strip().splitlines()), file=cpp_file)


@contextmanager
def block(src: str, delimiters="{}", suffix=""):
    global margin
    try:
        emit(src + " " + delimiters[0])
        margin += 4
        yield
    finally:
        margin -= 4
        emit(delimiters[1] + suffix)


with block("namespace util"):
    with block("enum country: uint16_t", suffix=";"):
        for i, c in enumerate(countries.country.values):
            emit(f"{c} = {i},")
        emit("GLBL = 65'535")
