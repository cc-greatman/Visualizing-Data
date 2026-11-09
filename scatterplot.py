import kagglehub
import os
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

filelink = kagglehub.dataset_download("alexisbcook/data-for-datavis")
filepath = os.path.join(filelink, "insurance.csv")
filedata = pd.read_csv(filepath)

plt.figure(figsize=(16, 8))

# x = the horizontal x-axis
# y = the vertical y-axis
#sns.scatterplot(x=filedata['bmi'], y=filedata['charges'])

# To double-check the strength of this relationship, 
# we might to add a regression line
sns.regplot(x=filedata['bmi'], y=filedata['charges'])

plt.title("BMI against charges in scatter plot graphs")
plt.show()