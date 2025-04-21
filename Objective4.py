import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Updated_Game_Sales_2018_2024.csv")

genre_sales = df.groupby(["Year", "Genre"])["Units_Sold"].sum().unstack()

genre_sales.plot(kind="bar", stacked=True, figsize=(12, 6), colormap="tab20")
plt.title("Genre Popularity Over the Years (2018-2024)")
plt.xlabel("Year")
plt.ylabel("Total Units Sold (millions)")
plt.legend(title="Genre", bbox_to_anchor=(1, 1))
plt.show()
