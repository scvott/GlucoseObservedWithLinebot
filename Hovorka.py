# -*- coding: utf-8 -*-
"""
Hovorka_Meal
"""
def Hovorka_Meal(eat):
    #parameter for Meals
    step = 0.1
    tau_d = 40
    Ag = 0.8
    Dm1 = 0
    Dm2 = 0
    #Molecular weight of glouse
    Mwg = 180
    Ug = []
    G = []
    i = 0.0
    while i<=180.0:
        if i<=10:
            d_cho=eat
        else:
            d_cho=0
        D_meal = 1000*d_cho/Mwg        
        k11 = Ag*D_meal-Dm1/tau_d
        k21 = Dm1/tau_d-Dm2/tau_d		
        k12 = Ag*D_meal-(Dm1+step/2*k11)/tau_d
        k22 = (Dm1+step/2*k11)/tau_d-(Dm2+step/2*k21)/tau_d		
        k13= Ag*D_meal-(Dm1+step/2*k12)/tau_d
        k23= (Dm1+step/2*k12)/tau_d-(Dm2+step/2*k22)/tau_d		
        k14= Ag*D_meal-(Dm1+step*k13)/tau_d
        k24= (Dm1+step*k13)/tau_d-(Dm2+step*k23)/tau_d		
        Dm1 = Dm1+step*(k11+2*k12+2*k13+k14)/6
        Dm2 = Dm2+step*(k21+2*k22+2*k23+k24)/6		
        Ug.append(Dm2/tau_d)
        G.append(Dm2/tau_d+70)
        i = i+0.1
    return Ug
