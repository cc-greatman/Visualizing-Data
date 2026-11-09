from utils import *

filelink = kagglehub.dataset_download("alexisbcook/data-for-datavis")
filepath = os.path.join(filelink, "iris.csv")
filedata = pd.read_csv(filepath, index_col='Id')

plt.figure(figsize=(10, 6))

# Using histograms to understand how petal length varies in iris flowers
#sns.histplot(filedata['Petal Length (cm)'])

# using a KDE graph to represent the data
#sns.kdeplot(data=filedata['Petal Length (cm)'], fill=True)

# We are not restricted to a single column when creating a KDE plot.
# We can create a 2-dimensional(2D) plot
#sns.jointplot(x=filedata['Petal Length (cm)'], y=filedata['Sepal Width (cm)'], kind='kde')

# Histrogram for each species(using colors to seperate/identify them)
#sns.histplot(data=filedata, x=filedata['Petal Length (cm)'], hue='Species')

# We can also use a KDE graph to represent the data while using colors to separate them
sns.kdeplot(data=filedata, x='Petal Length (cm)', hue='Species', fill=True)

plt.title("Distribution of Petal Lengths, by Species")

plt.show()