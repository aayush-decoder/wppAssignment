import pandas as pd
import datetime as dt

a = pd.Timestamp('2012-01-15')
b = pd.Timestamp('2012-01-15 21:20:00')
c = pd.Timestamp.now()
d = pd.Timestamp('2023-04-15').date()
e = pd.to_datetime('today').date()
f = pd.Timestamp('2023-04-15 08:45:00').time()
g = dt.datetime.now().time()

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
