import os
import glob
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


dbfiles = glob.glob(os.getcwd() + '/raw/*.db')


def view(dbname):
    conn = sqlite3.connect(dbname)
    df = pd.read_sql_query("SELECT * FROM Photons",con=conn)
    conn.close()
    return df

serlist = []
for i in dbfiles:
    df=view(i)
    angle = int(os.path.split(i)[1][:-3])
    ser = df['surfaceID'].value_counts().rename(angle)
    serlist.append(ser)

hits = pd.concat(serlist,axis=1)

hits = hits.T # Transposes dataframe

hits['n'] = hits[3]/hits[1]

hits['n'].plot()
plt.xlabel('Incidence angle (°)')
plt.title('Flat absorber - unsegmented')
plt.ylabel('$n_j$')




# CountSurfID = df1['surfaceID'].value_counts()

# absorber = df1[df1['surfaceID']==3]
# absorber.plot(x='y',y='x',style='o')
