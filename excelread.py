import pandas as pd

ifile = 'df'
ofile = 'combined3'
qfile = 3

def eread(x):
    df = pd.read_excel(x)
    return df

a = []

mdf = eread(ifile + '1.xlsx')

for i in range(1,qfile-1):
    nd = eread(ifile + str(i+1) + '.xlsx')
    mdf = mdf.merge(nd, how='outer')

mdf.to_excel(ofile + '.xlsx', index=False)
