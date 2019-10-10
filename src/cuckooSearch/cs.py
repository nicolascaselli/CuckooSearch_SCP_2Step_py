import numpy as np
from cuckooSearch import individual as id
from cuckooSearch import function as fn
import sys
import os
import csv
from cuckooSearch.config import Config as cf
import time


if os.path.exists("results"):
    pass
else:
    os.mkdir("results")

results = open("results" + os.sep + "results.csv", "w")
results_writer = csv.writer(results, lineterminator="\n")


def run_CS():
    print(cf.get_trial())
    
    for trial in range(cf.get_trial()):
        cf.set_Seed(int(round(time.time(),0)))
        np.random.seed(cf.get_Seed())

        results_list = [] # fitness list
        cs_list = []
        """Generate Initial Population"""
        for p in range(cf.get_population_size()):
            cs_list.append(id.Individual())
        print("cs_list[0].get_position(): ",cs_list[0].get_position())    
        print("len(cs_list[0].get_position()): ",len(cs_list[0].get_position()))
        """Sort List"""
        cs_list = sorted(cs_list, key=lambda ID: ID.get_fitness())

        """Find Initial Best"""
        BestPosition = cs_list[0].get_position()
        BestFitness = fn.calculation(cs_list[0].get_position(),cf.get_Cost())

        """↓↓↓Main Loop↓↓↓"""
        for iteration in range(cf.get_iteration()):

            """Generate New Solutions"""
            for i in range(len(cs_list)):
                cs_list[i].get_cuckoo()
                cs_list[i].set_fitness(fn.calculation(cs_list[i].get_position(),cf.get_Cost()))

                """random choice (say j)"""
                j = np.random.randint(low=0, high=cf.get_population_size())
                while j == i: #random id[say j] ≠ i
                    j = np.random.randint(0, cf.get_population_size())

                # for minimize problem
                if(cs_list[i].get_fitness() < cs_list[j].get_fitness()):
                    cs_list[j].set_position(cs_list[i].get_position())
                    cs_list[j].set_fitness(cs_list[i].get_fitness())

            """Sort (to Keep Best)"""
            cs_list = sorted(cs_list, key=lambda ID: ID.get_fitness())

            """Abandon Solutions (exclude the best)"""
            for a in range(1,len(cs_list)):
                r = np.random.rand()
                if(r < cf.get_Pa()):
                    cs_list[a].abandon()
                    cs_list[a].set_fitness(fn.calculation(cs_list[a].get_position(),cf.get_Cost()))

            """Sort to Find the Best"""
            cs_list = sorted(cs_list, key=lambda ID: ID.get_fitness())

            if cs_list[0].get_fitness() < BestFitness:
                BestFitness = cs_list[0].get_fitness()
                BestPosition = cs_list[0].get_position()

            sys.stdout.write("\r Trial:%3d , Iteration:%7d, BestFitness:%.4f" % (trial , iteration, BestFitness))

            results_list.append(str(BestFitness))

        results_writer.writerow(results_list)

if __name__ == '__main__':
    run_CS()
    results.close()