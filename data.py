import numpy as np
import pandas as pd
rng = np.random.default_rng(42)
data = []

n = 1_000_000
# 5 DÃY FLOAT:
# Float tăng dần:
arr1 = np.sort(rng.uniform(-1_000_000_000, 1_000_000_000, n))
data.append(arr1)
# Float giảm dần:
arr2 = np.sort(rng.uniform(-1_000_000_000, 1_000_000_000, n))[::-1]
data.append(arr2)
# 3 dãy ngẫu nhiên:
for _ in range(3):
    data.append(rng.uniform(-1_000_000_000, 1_000_000_000, n))
# 5 DÃY SỐ NGUYÊN:
for _ in range(5):
    data.append(rng.integers(-1_000_000_000, 1_000_000_000, n))
df = pd.DataFrame({f"col_{i}": data[i] for i in range(len(data))})

# Xuất CSV
df.to_csv("data.csv", index=False)
