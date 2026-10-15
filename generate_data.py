import numpy as np
import pandas as pd

# 1. Settings
N_VISITORS = 28000        # total visitors in the test
RATE_A = 0.030            # Offer A (20% off above Rs 1,000): 3.0% of visitors buy
RATE_B = 0.036            # Offer B (Buy 2 Get 1 Free): 3.6% of visitors buy

rng = np.random.default_rng(42)  

#Randomly assigning each visitor to group A or B 
group = rng.choice(["A", "B"], size=N_VISITORS)

#Decide who(each visitor) buys in each group
buy_probability = np.where(group == "A", RATE_A, RATE_B)
purchased = (rng.random(N_VISITORS) < buy_probability).astype(int)


df = pd.DataFrame({
    "visitor_id": range(1, N_VISITORS + 1),
    "group": group,
    "purchased": purchased,
})
df.to_csv("visitors.csv", index=False)


print(df.head())
print()