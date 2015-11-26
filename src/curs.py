import numpy as np

size = 288
hist_curs = np.zeros(size)  # from [1997  to 2019]

hist_curs[:6] = np.linspace(1.893, 1.86, 6) # 1997 [1-6]
hist_curs[6:12] = np.linspace(1.86, 1.896, 6) #1997 [7-12]

hist_curs[12:15] = np.linspace(1.899, 2.0381,3) #1998 [1-3]
hist_curs[15:18] = np.linspace(2.0383, 2.0578,3) #1998 [4-6]
hist_curs[18:21] = np.linspace(2.0591, 3.39, 3) #1998 [7-9]
hist_curs[21:24] = np.linspace(3.414, 3.427,3) #1998 [10-12]

hist_curs[24:27] = np.linspace(3.427, 3.9094,3) #1999 [1-3]
hist_curs[27:30] = np.linspace(3.9264, 3.9489,3) #1999 [4-6]
hist_curs[30:33] = np.linspace(3.9508, 4.4588,3) #1999 [7-9]
hist_curs[33:36] = np.linspace(4.4566, 5.466,3)  #199[10-12]

hist_curs[36:42] = np.linspace(5.5253, 5.447, 6) #2000 [1-6]
hist_curs[42:48] = np.linspace(5.448, 5.4355, 6) #2000 [7-12]

hist_curs[48:60] = np.linspace(5.3, 5.521, 12) #2001

#hist_curs[:] = np.linspace(,,) #200
#hist_curs[:] = np.linspace(,,) #200
x = 60
hist_curs[x:x+48] = 5.33 #2002 - #2005
hist_curs[x+48:x+72] = np.linspace(5.15, 5.07, 24) #2006 - 2007 

hist_curs[132:140] = np.linspace(5.07, 4.665, 8)  #2008 [1-8]
hist_curs[140:144] = np.linspace(5.182, 8.597, 4)

hist_curs[144:150] = np.linspace(8.702, 7.986, 6) #2009 [1:6]
hist_curs[150:153] = np.linspace(7.99, 8.86, 3) #2009 [7-9]
hist_curs[153:156] = np.linspace(8.35, 8.014,3)   #2009 [10-12]

x=156
hist_curs[x:x+48] = 8.1 #2010 - 2013

hist_curs[204:216] = np.linspace(8.422, 19.366, 12) #2014

hist_curs[216] = 20.9 #2015  [1]
hist_curs[217] = 29.3 #2015  [2]
hist_curs[218] = 26.21 #2015 [3]
hist_curs[219] = 23.6442 #2015[4]
hist_curs[220:223] = np.linspace(22.11, 24.83, 3) #2015 [5-7]
hist_curs[223] = 23.31  # 2015 [8]
hist_curs[224] = 23.122 # 2015[9]
hist_curs[225] = 23.57  # 2015 [10]  
hist_curs[226] = 25.11  # 2015 [11]

hist_curs[227:] = np.linspace(24.1, 41.0, size - 227)

def add_rand(x):
    N = len(x)
    y = np.zeros(N)
    for i in range(N):
        y[i] = x[i]*(1+(np.random.random_sample()-0.4)*0.15)
    return y

start = 24.5

c5 = np.linspace(start, 40.1, 60)
c5_op = np.linspace(start, 33.7, 60)
c5_pes = np.linspace(start, 50.125, 60)
c5_pes_exp = start * np.logspace(0, 0.31, 60)

c5r = add_rand(c5)
c5r[0] = 25.11

c5_opr = add_rand(c5_op)
c5_opr[0] = 25.33

c5_upend = np.zeros(60)
c5_upend[0:40] = np.linspace(start, 26.0, 40)
c5_upend[40:50] = np.linspace(26.0, 40.1, 10)
c5_upend[50:] = np.linspace(40.1, 41, 10)

c5_upend_pes = np.zeros(60)
c5_upend_pes[0:40] = np.linspace(start, 25.3, 40)
c5_upend_pes[40:52] = np.linspace(25.9, 49.7, 12)
c5_upend_pes[52:] = np.linspace(50.1, 51, 8)

c5_upstart = np.zeros(60)
c5_upstart[:12] = np.linspace(start, 40.1, 12)
c5_upstart[12:] = np.linspace(40.1, 41.0, 48)

c5_upstart_pes = np.zeros(60)
c5_upstart_pes[:12] = np.linspace(start, 51.1, 12)
c5_upstart_pes[12:] = np.linspace(51.1, 53.1, 48)

c5_USr = add_rand(c5_upstart)
c5_USPr = add_rand(c5_upstart_pes)

clog = np.zeros(60)

def log_curs():
    i = 1
    c = 24.5
    for i in range(60):
        if(i<10): clog[i] = c
        else: clog[i] = c*np.log10(i)
        i = i+1
    return clog



zero60 = np.zeros(60)

# some function for curs analysis

def curs_av_raise60(c):
    N = len(c)
    if(N <60):
        return ValueError('low curs history for calculation')
    cr=np.zeros(N)
    for i in range(N):
        if(i<60):
            cr[i] = 0.0
        else:
            cr[i] = (c[i] - c[i-60])/c[i-60]*100
    return cr
     

   


