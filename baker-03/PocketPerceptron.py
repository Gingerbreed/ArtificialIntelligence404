import numpy as np
import matplotlib.pyplot as plt
import copy
from sklearn.datasets.samples_generator import make_blobs
class PocketPerceptron:
    def __init__ (self):
        ctrs= 3*np.random.normal(0, 1,(2,2))
        self.X, self.y= make_blobs(n_samples=100, centers=ctrs, n_features=2, cluster_std=1.0, shuffle=False , random_state=0)
        self.y[self.y==0] = -1
        c0= plt.scatter(self.X[self.y==-1,0],self.X[self.y==-1,1], s=20, color='r', marker='x')
        c1= plt.scatter(self.X[self.y==1,0],self.X[self.y==1,1], s=20, color='b', marker='o')
        plt.legend((c0,c1),('Class -1','Class +1'), loc='upper right',
            scatterpoints=1, fontsize=11)
        plt.xlabel(r'$x 1$')
        plt.ylabel(r'$x 2$')
        plt.title(r'Two Simple Clusters of random data')
        plt.savefig('hw3.plot.pdf',bbox_inches='tight')
        plt.show()
 
    def plot(self, mispts=None, vec=None, save=False):
        fig = plt.figure(figsize=(5,5))
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        V = self.V
        a, b = -V[1]/V[2], -V[0]/V[2]
        l = np.linspace(-1,1)
        plt.plot(l, a*l+b, 'k-')
        cols = {1: 'r', -1: 'b'}
        for x,s in self.X:
            plt.plot(x[1], x[2], cols[s]+'o')
        if mispts:
            for x,s in mispts:
                plt.plot(x[1], x[2], cols[s]+'.')
        if vec != None:
            aa, bb = -vec[1]/vec[2], -vec[0]/vec[2]
            plt.plot(l, aa*l+bb, 'g-', lw=2)
        if save:
            if not mispts:
                plt.title('N = %s' % (str(len(self.X))))
            else:
                plt.title('N = %s with %s test points' \
                          % (str(len(self.X)),str(len(mispts))))
            plt.savefig('p_N%s' % (str(len(self.X))), \
                        dpi=200, bbox_inches='tight')
 
    def classification_error(self, vec, pts=None):
        # Error defined as fraction of misclassified points
        if not pts:
            pts = self.X
        M = len(pts)
        n_mispts = 0
        for x,s in pts:
            if int(np.sign(vec.T.dot(x))) != s:
                n_mispts += 1
        error = n_mispts / float(M)
        return error
 
    def choose_miscl_point(self, vec):
        # Choose a random point among the misclassified
        pts = self.X
        mispts = []
        for x,s in pts:
            if int(np.sign(vec.T.dot(x))) != s:
                mispts.append((x, s))
        return mispts[random.randrange(0,len(mispts))]
 
    def pla(self, save=False):
        # Initialize the weigths to zeros
        w = np.zeros(3)
        X,y = self.X, self.y
        N = len(X)
        it = 0
        bestW = copy.deepcopy(w)
        # Iterate until all points are correctly classified
        while self.classification_error(w) != 0:
            it += 1
            # Pick random misclassified point
            x, s = self.choose_miscl_point(w)
            w += s*x
            # Update weights if needed (classification_error)
            if(self.classification_error(w, pts=X)<self.classification_error(bestW, pts=X)):
            # make a deep copy
                bestW = copy.deepcopy(w)
        print(it)
        if save:
            self.plot(vec=bestW)
            plt.title('N = %s, Iteration %s\n' \
                     % (str(N),str(it)))
            plt.savefig('p_N%s_it%s' % (str(N),str(it)), \
                        dpi=200, bbox_inches='tight')
            plt.show()
        self.w = w
 
    def linear_regression(self,save=False):
        X = self.generate_blobs(); 
        N = len(X)
        x = X[:,0]
        y = X[:,1]
        w = np.dot(x,y)
        if save:
            fig = plt.figure(figsize=(5,5))
            plt.xlim(-2.5,2.5)
            plt.ylim(-2.5,2.5)
            cols = {1: 'r', -1: 'b'}
            for x,s in X:
                plt.plot(x, s)
            l = np.linspace(-2.5,2.5)
            m, b = -w/w, -w/w
            plt.plot(l, m*l+b, 'k-')
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            plt.savefig('p_N%s_linear_regression' % (str(N)), \
                        dpi=200, bbox_inches='tight')
            plt.show()
        self.pocket(w) #Uncomment if attempting way 3
        return w
        