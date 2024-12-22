
import pandas as pd

# pandas series is like a column
data = {"numbers": [1, 7, 4, 0]}
myvar = pd.DataFrame(data)

print(myvar)
# dtype is int64
print(myvar.dtypes)

mean = myvar['numbers'].mean()
# IMPORTANT - 0 is counted in the mean - answer is 3.0
print("Mean with 0 is: ", mean)

myvar['numbers'] = myvar['numbers'].replace(0, pd.NA)
print(myvar)
# dtype is now object
print(myvar.dtypes)
mean = myvar['numbers'].mean()
# IMPORTANT - <NA> is ignored in the mean - answer is 4.0
print("Mean with NA is: ", mean)


mean = myvar['numbers'].dropna().mean()
# IMPORTANT - dropna causes the row to be ignored - answer is 4.0
print("Mean with dropna() is: ", mean)

myvar.iloc[2] = pd.isnull
print(myvar)
print(myvar.dtypes)

# dropna(), skilna() don't work here - isnull and isna have the same result 
# mean = myvar['numbers'].dropna().mean()

