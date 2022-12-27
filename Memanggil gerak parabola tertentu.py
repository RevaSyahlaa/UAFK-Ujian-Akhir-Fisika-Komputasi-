import numpy as np
import csv
import time

from sklearn import svm
import pandas as pd

#Database: Gerbang LOgika AND
#Membaca data dari file
FileDB = 'DatabaseGerakParabola.txt'
Database = pd.read_csv(FileDB, sep=",", header=0)

#x = Data, y=Target
X = Database[[u'a', u'b']]
y = Database.Target


clf = svm.SVC()
clf.fit(X.values,y)

print(clf.predict( [[1,9]] ))
print(clf.predict( [[1,2]] ))
print(clf.predict( [[7,5]] ))
print(clf.predict( [[6,4]] ))
print(clf.predict( [[4,6]] ))
