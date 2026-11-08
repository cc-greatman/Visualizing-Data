import kagglehub
import matplotlib.pyplot as plt
import os
import pandas as pd
pd.plotting.register_matplotlib_converters()
import seaborn as sns

filelink = kagglehub.dataset_download("alexisbcook/data-for-datavis")
filepath = os.path.join(filelink, "spotify.csv")
filedata = pd.read_csv(filepath, index_col='Date', parse_dates=True)

# Set the width and height of the figure
plt.figure(figsize=(16, 6))

# Set a title for the figure
plt.title("Daily global streams of popular songs in 2017-2018")

# Line chart showing daily global screen of each song
sns.lineplot(data=filedata)

# Displaying the figure
plt.show()
