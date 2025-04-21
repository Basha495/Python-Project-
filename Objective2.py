import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Updated_Game_Sales_2018_2024.csv")

platform_sales = df.groupby("Platform")["Units_Sold"].sum()

plt.figure(figsize=(8, 8))
platform_sales.plot(kind="pie", autopct="%1.1f%%", startangle=140, colormap="tab10")
plt.title("Platform Market Share (2018-2024)")
plt.ylabel("")  
plt.show()
