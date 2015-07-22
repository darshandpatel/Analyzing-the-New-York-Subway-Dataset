import pandas as pd
import numpy as np
from ggplot import *


'''
#construct dataframe
test_data = pd.DataFrame({'random_1':pd.Series(np.random.randn(10)), 'category': pd.Series([2,2,1,1,4,4,3,3,5,5])})

print(test_data)
#group data by category, avoiding turning the category into the index (though that could be OK in some circumstances?)
grouped_data = test_data.groupby('category', as_index = False).sum()
#take a look - is that what we want to plot?
print(grouped_data)
#plot a bar chart with the category on the x axis and the sum of 'random_1' as the height, using stat = 'identity' to do this.
plot = ggplot(grouped_data,aes(x = 'category', y= 'random_1')) + geom_point(stat = 'identity')
print(plot)
'''

test_date = pd.DataFrame({'Alpha' : pd.Series(['A','B','C','D','E','F']),'value' : pd.Series([1,2,3,4,5,6])})
print(test_date)
print(test_date - test_date.mean())