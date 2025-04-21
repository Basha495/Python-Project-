import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Updated_Game_Sales_2018_2024.csv")

top_games = df.groupby("Game_Name")["Units_Sold"].sum().nlargest(10)

plt.figure(figsize=(12, 6))
sns.barplot(y=top_games.index, x=top_games.values, palette="viridis")
plt.title("Top 10 Best-Selling Games (2018-2024)")
plt.xlabel("Units Sold (millions)")
plt.ylabel("Game Name")
plt.show()
