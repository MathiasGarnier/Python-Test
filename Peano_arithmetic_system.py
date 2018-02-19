from types import SimpleNamespace
import numpy as np

class Peano(object):

    def __init__(self, *args):

        self.peano_postulates = SimpleNamespace() 
        self.peano_postulates.id = []
        self.peano_postulates.value = []
        
        self.dimension = len(args)
        self.defined = False
        
        for i in range(self.dimension):
            if isinstance(args[i], str):
                self.peano_postulates.id.append(args[i])

    def define(self, *args):

        if len(args) == len(self.peano_postulates.id):
            self.defined = True
            self.peano_postulates.value = []
            
            for i in range(self.dimension):
                self.peano_postulates.value.append(abs(args[i]))

    def equals(self):
        
        if self.defined:
            return self.peano_postulates.value.count(self.at(0)) == self.dimension
    
    def at(self, i):

        if self.defined:
            return self.peano_postulates.value[i]
    
    def callback(self):

        if self.defined:
            for i in range(self.dimension):
                print(self.peano_postulates.id[i], " <=> ", self.peano_postulates.value[i])

    def s(self, i):

        if self.defined:
            return self.at(i) + 1

#All of these functions must return true everytime
    def single_equivalence_axiom(self):

        if self.defined and self.dimension == 1:
            return self.at(0) == self.at(0) 

    def double_equivalence_axiom(self):

        if self.defined and self.dimension == 2 and self.at(0) == self.at(1):
            return self.at(1) == self.at(0)

    def multiple_equivalence_axiom(self):

        if self.defined and self.dimension > 2 and self.equals():
            return self.at(0) == self.at(self.dimension)
        
    def equivalent_successor_axiom(self):

        if self.defined and self.dimension == 2 and self.at(0) == self.at(1):
            return self.s(1) == self.s(0)

    def multiple_equivalent_addition_axiom(self):

        if self.defined and self.dimension > 2 and (self.peano_postulates.value.count(self.at(0)) == self.dimension - 1 or self.peano_postulates.value.count(self.at(1)) == self.dimension - 1):

            unique = np.unique(np.array(self.peano_postulates.value))
            return unique[0] + unique[1] == unique[1] + unique[0]

    def multiple_equivalent_multiplication_axiom(self):

        if self.defined and self.dimension > 2 and (self.peano_postulates.value.count(self.at(0)) == self.dimension - 1 or self.peano_postulates.value.count(self.at(1)) == self.dimension - 1):

            unique = np.unique(np.array(self.peano_postulates.value))
            return unique[0] * unique[1] == unique[1] * unique[0]
    
    def zero_addition_axiom(self):

        if self.defined and self.dimension == 1:
            return 0 + self.at(0) == self.at(0)

    def double_successor_addition_axiom(self):

        if self.defined and self.dimension == 2:
            return self.s(0) + self.at(1) == ((self.at(0)) + self.at(1)) + 1

    def zero_multiplication_axiom(self):

        if self.defined and self.dimension == 1:
            return 0 * self.at(0) == 0

    def double_successor_multiplication_axiom(self):

        if self.defined and self.dimension == 2:
            return self.s(0) * self.at(1) == ((self.at(0)) * self.at(1)) + self.at(1)

    def equivalent_peano_axiom(self):

        if self.defined and self.dimension == 2 and self.s(0) == self.s(1):
            return self.at(0) == self.at(1)

    def zero_successor_axiom(self):

        if self.defined and self.dimension == 1:
            return not(self.s(0) == 0)
