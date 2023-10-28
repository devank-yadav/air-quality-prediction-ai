import pandas as pd

new_df = pd.DataFrame()

for i in range(2016,2023):
    df = pd.read_excel("Data\extracted_data" + str(i) + ".xlsx")
    new_df = pd.concat([df, new_df])

new_df.to_excel("final_data.xlsx", index=None, header=True) 	