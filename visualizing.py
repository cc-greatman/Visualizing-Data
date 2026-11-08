import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import os
import kagglehub

filelink = kagglehub.dataset_download("alexisbcook/data-for-datavis")
filepath = os.path.join(filelink, "fifa.csv")
df = pd.read_csv(filepath, index_col='Date', parse_dates=True)

plt.figure(figsize=(16, 6))
sns.lineplot(data=df)
plt.show()