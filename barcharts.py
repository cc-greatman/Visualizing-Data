import kagglehub
import os
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

filelink = kagglehub.dataset_download("alexisbcook/data-for-datavis")
filepath = os.path.join(filelink, "flight_delays.csv")

filedata = pd.read_csv(filepath, index_col='Month')

plt.figure(figsize=(16, 8))
plt.title("Average arrival delay for Spirit Airlines flights, by month")

# Barchart showing the data for the column NK only
# x determines the horizontal axis, y determines the height of the bar
#sns.barplot(x=filedata.index, y=filedata['NK'])

# Heatmap showing average arrival delay for each airline by month
# annot ensures that the values appear for each cell
sns.heatmap(data=filedata, annot=True)

plt.ylabel("Arrival delay (in minutes)")
plt.show()