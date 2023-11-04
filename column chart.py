# Dataframe of previous code is used here 
# Plot the bar chart for numeric values 
# a comparison will be shown between 
# all 3 age, income, sales 
df.plot.bar() 
# plot between 2 attributes 
plt.bar(df['Age'], df['Sales']) 
plt.xlabel("Age") 
plt.ylabel("Sales") 
plt.show()