import numpy as np

import matplotlib.pyplot as plt


class Equation:

    def __init__(self, e, sig, d):

        self.e = 8/(e**2)

        self.dvc = d

        self.s = 4/sig

        self.n = [1]


    def plugnchug(self, N):

        return self.e * np.log(self.s * ((2*N)**self.dvc + 1))


    def calculate(self):

        it = 0
 
        N = self.plugnchug(self.n[it])

        while N > self.n[it]:

            it += 1

            self.n.append(N)

            N = self.plugnchug(N)
            print N

        return N


    def plot(self):

        max = np.ceil(self.n[len(self.n)-1]+1)

        plt.xlim(0.0, 20)

        plt.ylim(0.0, 500000)

        plt.title('Iterations of Equation Algorithm')
        plt.xlabel('Iteration number')
        plt.ylabel('Size of sample')
        for i in range(1, len(self.n)):

            plt.plot(i, self.n[i], 'ro')
        plt.show()



 

def main():

    s = Equation(0.05, 0.05, 10)

    size = s.calculate()

    print('You will need ' + str(np.ceil(size)) + ' samples at the least.')

    s.plot()


 

main()
