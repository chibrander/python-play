import pandas as pd
import os

ifile = 'lingerie'
ofile = 'combined-' + ifile
sfile = 23
qfile = 49

infolder = 'Excel'
folder = 'Combined Excel'

def eread(x):
    df = pd.read_excel(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/' +  infolder + '/' + x)
    return df

a = []

mdf = eread(ifile + str(sfile) + '.xlsx')

for i in range(sfile+1,qfile):
    nd = eread(ifile + str(i+1) + '.xlsx')
    mdf = mdf.merge(nd, how='outer')

mdf.to_excel(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/' +  folder + '/' + ofile + '.xlsx', index=False)
