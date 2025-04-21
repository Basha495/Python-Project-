import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Updated_Game_Sales_2018_2024.csv")

plt.figure(figsize=(8, 5))
sns.histplot(df["Rating"], bins=10, kde=True, color="g")
plt.title("Distribution of Game Ratings (2018-2024)")
plt.xlabel("Rating (1-10)")
plt.ylabel("Count of Games")
plt.grid()
plt.show()
