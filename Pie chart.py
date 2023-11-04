import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use(['unhcrpyplotstyle','pie'])

#load and reshape the data
df = pd.read_csv('https://raw.githubusercontent.com/GDS-ODSSS/unhcr-dataviz-platform/master/data/part_to_a_whole/pie.csv')

#compute data for plotting
labels = df['funding_type']
values = df['funding_value']

#plot the chart
fig, ax = plt.subplots()
pie=ax.pie(values, labels=labels, autopct='%1.1f%%', pctdistance = 0.75, counterclock=False, startangle=-270)
       
#set chart title
ax.set_title('UNHCR Funding (as of February 2022)')

#set chart source and copyright
plt.annotate('Source: UNHCR', (0,0), (0, -25), xycoords='axes fraction', textcoords='offset points', va='top', color = '#666666', fontsize=9)
plt.annotate('©UNHCR, The UN Refugee Agency', (0,0), (0, -35), xycoords='axes fraction', textcoords='offset points', va='top', color = '#666666', fontsize=9)

#adjust chart margin and layout
fig.tight_layout()

#show chart
plt.show()