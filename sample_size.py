import math
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

BASELINE = 0.03     #existing: 30 out 1000 visitors buy
TARGET = 0.036      #expected smallest improvement : 36 out 1000 visitors buy which is extra 6
ALPHA = 0.05
POWER = 0.80

effect = proportion_effectsize(TARGET, BASELINE)
n = NormalIndPower().solve_power(effect, alpha=ALPHA, power=POWER, ratio=1)
print(f"Visitors needed in EACH group: {math.ceil(n):,}")
print(f"Total visitors (A + B): {2 * math.ceil(n):,}")