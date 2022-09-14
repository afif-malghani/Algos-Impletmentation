import pandas as pd
from entropy import getEntropy

df = pd.read_csv('Social_Network_Ads.csv')

classes = df['Purchased']

print(classes)

numbClasses = classes.unique()
print(numbClasses)

getEntropy(classes, numbClasses)

