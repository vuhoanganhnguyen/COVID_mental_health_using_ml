" Import libraries "
import numpy as numpy
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2

" Get the data for Food Security and Labour Market Impacts"
churn_df = pd.read_csv('Food Security & Labour Market.csv')
churn_df.head()
print (churn_df)

" Chi-square Test for Food Security and Labour Market Impacts"
X = churn_df.drop('MH_05',axis=1)
y = churn_df['MH_05']
chi_scores = chi2(X,y)
print (chi_scores)
p_values = pd.Series(chi_scores[1],index = X.columns)
p_values.sort_values(ascending = False , inplace = True)
p_values.plot.bar()

" Since LM_35G, LM_35A, LM35BCDE, LM_35F has higher the p-value " 
" it says that these variables is independent of the repsone "
" and can not be considered for model training "

