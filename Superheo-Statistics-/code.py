# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data.Gender.replace('-','Agender',inplace=True)
gender_count = data.Gender.value_counts()
plt.hist('gender_count', bins= 10)


# --------------
#Code starts here
import matplotlib.pyplot as plt
alignment = data.Alignment.value_counts()
plt.pie(alignment)


# --------------
#Code starts here

sc_df = data[['Strength','Combat']].copy()
sc_covariance = sc_df.cov().iloc[0,1]

sc_strength = sc_df.Strength.std()

sc_combat = sc_df.Combat.std()
sc_pearson = (sc_covariance/(sc_combat*sc_strength))

ic_df = data[['Intelligence','Combat']].copy()
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
ic_pearson = (ic_covariance/(ic_combat*ic_intelligence))



# --------------
#Code starts here

total_high = data['Total'].quantile(0.99)
super_best = data[data['Total']>total_high]
super_best_names = super_best['Name'].tolist()
print(super_best_names)


# --------------
#Code starts here
import matplotlib.pyplot as plt 
ax_1 = plt.subplot(111)
ax_1.boxplot(super_best['Intelligence'])
ax_2 = plt.subplot(222)
ax_2.boxplot(super_best['Speed'])
ax_3 = plt.subplot(333)
ax_3.boxplot(super_best['Power'])


