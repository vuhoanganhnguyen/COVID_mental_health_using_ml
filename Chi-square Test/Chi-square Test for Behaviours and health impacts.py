" Import libraries "
import numpy as numpy
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2

" Get the data for Behaviours and health impacts"
churn_df = pd.read_csv('Behaviours and health impacts.csv')
churn_df.head()
print (churn_df)

" Chi-square Test for Behaviours and health impacts"
X = churn_df.drop('MH_05',axis=1)
y = churn_df['MH_05']
chi_scores = chi2(X,y)
print (chi_scores)
p_values = pd.Series(chi_scores[1],index = X.columns)
p_values.sort_values(ascending = False , inplace = True)
p_values.plot.bar()

" Since BH_20N, BH-20M, BH_20I, BH_20K, BH_20D, BH_20H, BH_20B, BH_20J,BH-35C, BH-35D, "
" BH_20F, BH_20C, BH_20G, BH_20A, BH_20E, BH_110, BH_20L, BH_115 has higher the p-value " 
" it says that these variables is independent of the repsone "
" and can not be considered for model training "
