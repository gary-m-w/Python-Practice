# Using the squirrel dataset, create a dataframe in pandas to output the count of each color squirrel and export
# to a new csv

import pandas

df = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
df_gray = df[df['Primary Fur Color'] == 'Gray']
df_black = df[df['Primary Fur Color'] == 'Black']
df_cinnamon = df[df['Primary Fur Color'] == 'Cinnamon']

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [len(df_gray), len(df_black), len(df_cinnamon)]
}

pandas.DataFrame(data_dict).to_csv("squirrel_count.csv")