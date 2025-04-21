import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Updated_Game_Sales_2018_2024.csv")

yearly_sales = df.groupby("Year")["Units_Sold"].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=yearly_sales, x="Year", y="Units_Sold", marker="o", color="b")
plt.title("Yearly Game Sales Trend (2018-2024)")
plt.xlabel("Year")
plt.ylabel("Total Units Sold (millions)")
plt.grid()
plt.show()
