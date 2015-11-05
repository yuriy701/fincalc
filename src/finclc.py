import numpy as np

#hist_curs = np.zeros(240)
#hist_curs[:12] = 5.43 #  2000
#hist_curs[12:24] = 5.37 #2001
#hist_curs[24:72] = 5.33 #2002 - #2005
#hist_curs[72:96] = 5.05 #2006 - 2007
#hist_curs[96:108] = 5.5  #2008
#hist_curs[108:120] = 7.8 #2009
#hist_curs[120:168] = 8.0 #2010 - 2013
#hist_curs[168:180] = 15.0 #2014
#hist_curs[180:192] = 23.5 #2015
#hist_curs[192:] = np.linspace(23.5, 40.0, 240-192)


def date2index(year, month):
    c = year - 1997 
    if(c <0 or month <0 or month>12):
       return ValueError("Wrong input date")
    return c*12 + month -1

def index2date(index):
    y = (index+1)/12
    m = (index+1)%12
    return y, m


def grn_payment(x, i):
    return x

def dol_payment(x, i):
    return x

def fv(P, S, Pm, I):
    SS = S
    fsum = np.zeros(P)
    for i in range(P):
        SS = SS*(1+I) + Pm
        fsum[i] = SS
    return fsum 

def saving_comparer_grn(P, S, Pm, Ig, Id, curs):
    gd = np.zeros(P)
    dol = np.zeros(P)
    sg = S
    sd = S/curs[0]

    for i in range(P):
        sg = sg*(1+Ig) + Pm
        gd[i] = sg/curs[i]
        sd = sd*(1+Id)+Pm/curs[i]
        dol[i] = sd
    prc = (gd-dol)/gd*100
    return dol, gd, prc

def saving_comparer_dol(P,S,Pm,Ig,Id,curs):
    gd = np.zeros(P)        
    dol = np.zeros(P)
    sg = S*curs[0]
    sd = S
    for i in range(P):
        sg = sg*(1+Ig) +Pm*curs[i]
        gd[i] = sg/curs[i]
        sd = sd*(1+Id) + Pm
        dol[i] = sd
    prc = (gd-dol)/gd*100
    return dol, gd, prc


def grn2dol(grn, curs):
    P = grn.size
    dol = np.zeros(P)
    for i in range(P):
        dol[i] = grn[i]/curs[i]
    return dol


def compare180():
    g1 = fv(180, 10000, 0, 0.01)
    d1 = fv(180, 2000,  0, 0.005)
    dg1 = grn2dol(g1,hist_curs)
    return d1, dg1

def compare240():
    g1 = fv(240, 100, 0, 0.01)
    d1 = fv(240, 19,  0, 0.005)
    dg1 = grn2dol(g1,hist_curs)
    return d1, dg1

def compare_f60():
    g1 = fv(60, 0, 23000, 0.01)
    d1 = fv(60, 0,  1000, 0.005)
    dg1 = grn2dol(g1,hist_curs[180:240])
    return d1, dg1

def prc_sum(x):
    N = len(x)
    ret_60 = np.zeros(N)
    ret_all = np.zeros(N)
    for i in range(N):
         if (i<60):
             ret_60[i] = sum(x[:i])
         else: 
             ret_60[i] = sum(x[i-60:i])
         ret_all[i] = sum(x[:i])
    return ret_60, ret_all



