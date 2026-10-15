import pandas as pd
from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep

data = pd.read_csv("visitors.csv")

# split into the two groups
group_a = data[data["group"] == "A"]
group_b = data[data["group"] == "B"]

visitors = [len(group_a), len(group_b)]
buyers = [group_a["purchased"].sum(), group_b["purchased"].sum()]

# conversion rate = buyers / visitors, shown as a percentage
rate_a = round(buyers[0] / visitors[0] * 100, 2)
rate_b = round(buyers[1] / visitors[1] * 100, 2)
print("Offer A conversion rate:", rate_a, "%")
print("Offer B conversion rate:", rate_b, "%")

# is the difference real or just luck?
z_stat, p_value = proportions_ztest(buyers, visitors)
print("p-value:", round(p_value, 4))

# likely size of the improvement (B minus A)
low, high = confint_proportions_2indep(buyers[1], visitors[1], buyers[0], visitors[0])
print("Improvement range:", round(low * 100, 2), "to", round(high * 100, 2), "percentage points")

# conclusion
if p_value < 0.05 and rate_b > rate_a:
    print("Conclusion: Offer B (Buy 2 Get 1 Free) converts better than Offer A. Recommend Offer B.")
elif p_value < 0.05 and rate_a > rate_b:
    print("Conclusion: Offer A (20% off) converts better than Offer B. Keep Offer A.")
else:
    print("Conclusion: No clear winner. Keep Offer A unless other factors favour B.")