import pandas as pd

def extract_mean_bhai(day, month, year):

    if(month<10):
        month = '0' + str(month)

    new_df = pd.read_csv('ad_viz_plotval_data.csv')
    date_entered = str(month) + '/' + str(day) + '/' + str(year)
    new_df = new_df[(new_df["Date"] == date_entered)][['Date', 'Daily Max 8-hour Ozone Concentration']]
    return(new_df["Daily Max 8-hour Ozone Concentration"].mean())