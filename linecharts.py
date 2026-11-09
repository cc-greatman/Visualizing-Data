from utils import *

filelink = kagglehub.dataset_download("alexisbcook/data-for-datavis")
filepath = os.path.join(filelink, "spotify.csv")
filedata = pd.read_csv(filepath, index_col='Date', parse_dates=True)

# Set the width and height of the figure
plt.figure(figsize=(16, 6))

# Set a title for the figure
plt.title("Daily global streams of popular songs in 2017-2018")

# Line chart showing daily global screen of each song
#sns.lineplot(data=filedata)

# We can also plot a subset of the columns
# Line chart showing daily global streams of a single column
sns.lineplot(data=filedata['Shape of You'], label="Shape of You")

# Line chart showing daily global streams of a single column
sns.lineplot(data=filedata['Despacito'], label="Despacito")

# Add a label for the horizontal axis
plt.xlabel("Date")

# Displaying the figure
plt.show()
