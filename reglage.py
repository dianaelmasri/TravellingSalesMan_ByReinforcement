import ACO
import time as tm
import matplotlib.pyplot as plt
ZZ = tm.time()
P_q0 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
P_beta = [1.1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
P_rho = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
P_phi = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
P_K = [1, 2, 5, 10, 15, 20, 25, 30]
N_iter = 250
#(0.8, 2.5, 0.05, 0.1, 15)

resPq0=[]
timePq0=[]
for p in P_q0:
    r=0
    t=0
    for i in range(5):
        aco = ACO.ACO(p, 2, 0.1, 0.1, 10, 'qatar')
        a = tm.clock()
        sol = aco.runACO(N_iter)
        b = tm.clock()
        t+=b-a
        r+=sol.cost
    resPq0.append(r/5.0)
    timePq0.append(t/5.0)

q0_opt = P_q0[resPq0.index(min(resPq0))]

plt.figure(1)
plt.plot(P_q0, resPq0)
plt.xlabel("q0")
plt.ylabel("Solution cost")
plt.figure(2)
plt.plot(P_q0, timePq0)
plt.xlabel("q0")
plt.ylabel("Execution time")


resPbeta=[]
timePbeta=[]
for p in P_beta:
    r=0
    t=0
    for i in range(5):
        aco = ACO.ACO(q0_opt, p, 0.1, 0.1, 10, 'qatar')
        a = tm.clock()
        sol = aco.runACO(N_iter)
        b = tm.clock()
        t+=b-a
        r+=sol.cost
    resPbeta.append(r/5.0)
    timePbeta.append(t/5.0)
beta_opt = P_beta[resPbeta.index(min(resPbeta))]
plt.figure(3)
plt.plot(P_beta, resPbeta)
plt.xlabel("beta")
plt.ylabel("Solution cost")
plt.figure(4)
plt.plot(P_beta, timePbeta)
plt.xlabel("beta")
plt.ylabel("Execution time")

resPrho=[]
timePrho=[]
for p in P_rho:
    r=0
    t=0
    for i in range(5):
        aco = ACO.ACO(q0_opt, beta_opt, p, 0.1, 10, 'qatar')
        a = tm.clock()
        sol = aco.runACO(N_iter)
        b = tm.clock()
        t+=b-a
        r+=sol.cost
    resPrho.append(r/5.0)
    timePrho.append(t/5.0)

rho_opt = P_rho[resPrho.index(min(resPrho))]
plt.figure(5)
plt.plot(P_rho, resPrho)
plt.xlabel("rho")
plt.ylabel("Solution cost")
plt.figure(6)
plt.plot(P_rho, timePrho)
plt.xlabel("rho")
plt.ylabel("Execution time")


resPphi=[]
timePphi=[]
for p in P_phi:
    r=0
    t=0
    for i in range(5):
        aco = ACO.ACO(q0_opt, beta_opt, rho_opt, p, 10, 'qatar')
        a = tm.clock()
        sol = aco.runACO(N_iter)
        b = tm.clock()
        t+=b-a
        r+=sol.cost
    resPphi.append(r/5.0)
    timePphi.append(t/5.0)

phi_opt = P_phi[resPphi.index(min(resPphi))]
plt.figure(7)
plt.plot(P_phi, resPphi)
plt.xlabel("phi")
plt.ylabel("Solution cost")
plt.figure(8)
plt.plot(P_phi, timePphi)
plt.xlabel("phi")
plt.ylabel("Execution time")


resPK=[]
timePK=[]
for p in P_K:
    r=0
    t=0
    for i in range(5):
        aco = ACO.ACO(q0_opt, beta_opt, rho_opt, phi_opt, p, 'qatar')
        a = tm.clock()
        sol = aco.runACO(N_iter)
        b = tm.clock()
        t+=b-a
        r+=sol.cost
    resPK.append(r/5.0)
    timePK.append(t/5.0)

K_opt = P_K[resPK.index(min(resPK))]
plt.figure(9)
plt.plot(P_K, resPK)
plt.xlabel("K")
plt.ylabel("Solution cost")
plt.figure(10)
plt.plot(P_K, timePK)
plt.xlabel("K")
plt.ylabel("Execution time")
print (q0_opt,beta_opt,rho_opt,phi_opt,K_opt)
print tm.time()-ZZ
plt.show()