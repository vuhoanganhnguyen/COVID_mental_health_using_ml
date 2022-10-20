" Import libraries "
import numpy as numpy
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2

" Get the data for Mental health impacts"
churn_df = pd.read_csv('Mental health impacts.csv')
churn_df.head()
print (churn_df)

" Chi-square Test for Mental health impacts"
X = churn_df.drop('MH_05',axis=1)
y = churn_df['MH_05']
chi_scores = chi2(X,y)
print (chi_scores)
p_values = pd.Series(chi_scores[1],index = X.columns)
p_values.sort_values(ascending = False , inplace = True)
p_values.plot.bar()

" Since MH_15E has higher the p-value " 
" it says that these variables is independent of the repsone "
" and can not be considered for model training "
