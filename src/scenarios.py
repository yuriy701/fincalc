import curs
import finclc
import pylab
import numpy as np


def calc_grn_c5_rel(igrn, idol):
    d, gd, pc = finclc.saving_comparer_grn(60,180,50, igrn, idol, curs.c5)
    pylab.plot(d, color='g')    
    pylab.plot(gd, color = 'b')
#    pylab.plot(np.zeros(60))
    pylab.plot(pc)

def calc_grn_c5_op(igrn, idol):
    d, gd, pc = finclc.saving_comparer_grn(60,180,50, igrn, idol, curs.c5_op)
    pylab.plot(d, color = 'g')    
    pylab.plot(gd, color = 'y')
#    pylab.plot(np.zeros(60))
    pylab.plot(pc)

def calc_grn_c5_pes(igrn, idol):
    d, gd, pc = finclc.saving_comparer_grn(60,180,50, igrn, idol, curs.c5_pes)
    pylab.plot(d, color='g')    
    pylab.plot(gd, color = 'r')
#    pylab.plot(np.zeros(60))
    pylab.plot(pc)


def calc_grn_c5_upstart_pes(igrn, idol):
    d, gd, pc = finclc.saving_comparer_grn(60,180,50, igrn, idol, curs.c5_upstart_pes)
    pylab.plot(d)
    pylab.plot(gd)
    pylab.plot(np.zeros(60))
    pylab.plot(pc)



