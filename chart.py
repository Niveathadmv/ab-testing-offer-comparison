import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("visitors.csv")

# conversion rate for each group, as a percentage
rates = data.groupby("group")["purchased"].mean() * 100

labels = ["Offer A\n20% off", "Offer B\nBuy 2 Get 1 Free"]
plt.bar(labels, rates.values, color=["grey", "green"])

# write the value on top of each bar
for i, value in enumerate(rates.values):
    plt.text(i, value + 0.05, str(round(value, 2)) + "%", ha="center")

plt.ylabel("Conversion rate (%)")
plt.title("Conversion rate by offer")
plt.ylim(0, 4.5)
plt.savefig("conversion_chart.png")
plt.show()