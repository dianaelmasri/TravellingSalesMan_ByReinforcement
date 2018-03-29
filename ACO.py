import numpy as np
import random as rd
from Graph import Graph
from Solution import Solution

SOURCE = 0


class ACO(object):
    def __init__(self, q0, beta, rho, phi, K, data):
        self.parameter_q0 = q0
        self.parameter_beta = beta
        self.parameter_rho = rho
        self.parameter_phi = phi
        self.parameter_K = K

        self.graph = Graph(data)
        self.best = Solution(self.graph)
        self.best.cost = np.inf
        self.pheromone_init = np.ones((self.graph.N, self.graph.N))
        f = open(data + '_init', 'r')
        l = float(f.readline())
        self.pheromone_init *= l
        self.pheromone = np.ones((self.graph.N, self.graph.N)) * l

    def get_next_city(self, sol):
        q = rd.random()
        sol.visited.insert(0,SOURCE)
        m=sol.visited[-1]
        candidates = np.divide(self.pheromone[m,sol.not_visited[1:]],np.power(self.graph.costs[m,sol.not_visited[1:]],self.parameter_beta))
        norm = np.sum(candidates)
        if q <= self.parameter_q0:
            ind = sol.not_visited[np.argmax(candidates)+1]
            sol.visited.pop(0)
        else:
            ind = np.random.choice([a for a in sol.not_visited[1:] ],p=candidates/norm)
            sol.visited.pop(0)

        return ind


    def heuristic2opt(self, sol):
        sol.visited.insert(0,SOURCE)
        for i in range(len(sol.visited)-1):
            for j in range(i+2,(len(sol.visited)-1)):
                s = sol.cost
                sol.cost -= sol.g.costs[sol.visited[i],sol.visited[i+1]]
                sol.cost-= sol.g.costs[sol.visited[j],sol.visited[j+1]]
                sol.cost += sol.g.costs[sol.visited[i], sol.visited[j]]
                sol.cost += sol.g.costs[sol.visited[i+1], sol.visited[j+1]]
                if s>sol.cost:
                    sol.inverser_ville(i,j)
                else:
                    sol.cost = s
        sol.visited.pop(0)


    def global_update(self, sol):
        sol.visited.insert(0,SOURCE)
        Lgb = sol.cost

        self.pheromone = self.pheromone*(1-self.parameter_rho)
        delta_pheromone_ij = np.zeros((self.graph.N, self.graph.N))
        for k in range(len(sol.visited)-1) :
            delta_pheromone_ij[sol.visited[k]][sol.visited[k+1]]= 1.0/Lgb
            delta_pheromone_ij[sol.visited[k+1]][sol.visited[k]] = 1.0 / Lgb
        self.pheromone += self.parameter_rho*delta_pheromone_ij

        sol.visited.pop(0)


    def local_update(self, sol):
        edges = [(SOURCE,sol.visited[0])]+[(sol.visited[i],sol.visited[i+1]) for i in range(len(sol.visited)-1)]
        for e in edges:
            self.pheromone[e[0],e[1]] =(1-self.parameter_phi)*self.pheromone[e[0],e[1]]+self.parameter_phi*self.pheromone_init[e[0],e[1]]
            self.pheromone[e[1], e[0]] =self.pheromone[e[0],e[1]]


    def runACO(self, maxiteration):
        K = self.parameter_K
        for i in range(maxiteration):
            F = [Solution(self.graph) for i in range (K)]
            for sol in F:
                self.build_solution(sol)
                self.local_update(sol)
            m=min(F,key=lambda s: s.cost)
            while 1:
                c = m.cost
                self.heuristic2opt(m)
                if m.cost==c:
                    break
            if m.cost<self.best.cost:
                self.best=m
            self.global_update(self.best)
        return self.best


    def build_solution(self, sol):
        while len(sol.not_visited)>1:
            if len(sol.visited)==0:
                sol.add_edge(SOURCE,self.get_next_city(sol))
            else:
                sol.add_edge(sol.visited[-1],self.get_next_city(sol))
        sol.add_edge(sol.visited[-1],SOURCE)



if __name__ == '__main__':
    aco = ACO(0.5, 2, 0.1, 0.1, 1, '')
    aco.runACO(1)
