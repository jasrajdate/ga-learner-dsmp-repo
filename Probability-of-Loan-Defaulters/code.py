# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = len(df[df.fico>700])/len(df['fico'])
print(p_a)

df1 = df[df.purpose == 'debt_consolidation']

p_b = len(df1)/len(df)
print(p_b)
p_a_b = len(df1[df1['fico'].astype(float)>700])/len(df1['fico'])

result = (p_a_b == p_a)
print(result)

# code ends here


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df['paid.back.loan'])
print(prob_lp)

prob_cs = len(df[df['credit.policy'] == 'Yes'])/len(df['credit.policy'])
print(prob_cs)

new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = len(new_df[new_df['credit.policy']=='Yes'])/len(new_df)

bayes = prob_pd_cs*prob_lp/prob_cs

print(bayes)
# code ends here


# --------------
# code starts here
import matplotlib.pyplot as plt 
plt.bar(df.purpose, height = 100)

df1 = df[df['paid.back.loan']=='No']
plt.bar(df1.purpose, height = 100)

# code ends here


# --------------
# code starts here
import matplotlib.pyplot as plt

inst_median = df.installment.median()
inst_mean = df.installment.mean()

plt.hist(df.installment, bins=20)
plt.hist(df['log.annual.inc'], bins=20)

# code ends here


