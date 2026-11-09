from utils import *

filelink = kagglehub.dataset_download("alexisbcook/data-for-datavis")
filepath = os.path.join(filelink, "insurance.csv")

filedata = pd.read_csv(filepath)

print(filedata.head())