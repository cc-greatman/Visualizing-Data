from utils import *

filelink = kagglehub.dataset_download("alexisbcook/data-for-datavis")
filepath = os.path.join(filelink, "insurance.csv")
filedata = pd.read_csv(filepath)

plt.figure(figsize=(16, 8))

# x = the horizontal x-axis
# y = the vertical y-axis
#sns.scatterplot(x=filedata['bmi'], y=filedata['charges'])

# To double-check the strength of this relationship, 
# we might to add a regression line
#sns.regplot(x=filedata['bmi'], y=filedata['charges'])

# We can use scatter plots to display the relationships between
# 3 variables. We can do this by color-coding the points
#sns.scatterplot(x=filedata['bmi'], y=filedata['charges'], hue=filedata['smoker'])

# We can use the line below to color-code and also add 2 regression lines, 
# coressponding to smokers and non-smokers
#sns.lmplot(x="bmi", y="charges", hue="smoker", data=filedata)

# We can also use swarmplots
sns.swarmplot(x=filedata['smoker'], y=filedata['charges'])

plt.title("BMI against charges in scatter plot graphs")
plt.show()