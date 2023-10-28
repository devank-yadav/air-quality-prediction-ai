import pandas as pd

for i in range(2022, 2023):

    df = pd.read_csv("https://aqs.epa.gov/aqsweb/airdata/daily_44201_" + str(i) + ".zip")

    df1 = pd.read_csv("https://aqs.epa.gov/aqsweb/airdata/daily_42401_" + str(i) + ".zip")

    df2 = pd.read_csv("https://aqs.epa.gov/aqsweb/airdata/daily_42101_" + str(i) + ".zip")

    df3 = pd.read_csv("https://aqs.epa.gov/aqsweb/airdata/daily_42602_" + str(i) + ".zip")

    df = pd.concat([df, df1, df2, df3])

    new_df = df[(df["State Code"] == 9) | (df["State Code"] == 23) | (df["State Code"] == 25) | (df["State Code"] == 33) | (df["State Code"] == 34) | (df["State Code"] == 36) | (
        df["State Code"] == 42) | (df["State Code"] == 44) | (df["State Code"] == 50) | (df["State Code"] == "50")][['State Code', 'Parameter Name', 'Arithmetic Mean', 'Date Local']]

    new_df.to_excel('Data\extracted_data' + str(i) + '.xlsx', index=None, header=True)