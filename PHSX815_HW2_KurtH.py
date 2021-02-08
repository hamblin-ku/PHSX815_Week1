#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import argparse
import my_params

#################
# Random class
#################
# class that can generate random numbers
class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        self.m_u = np.uint64(self.m_u * 2862933555777941757) + np.uint64(7046029254386353087)
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

def make_plot(data):
    #imort custom matplotlib parameters from file
    custom_params = my_params.params()
    mpl.rcParams.update(custom_params)
    
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(myx, 50, density=True, facecolor='g', alpha=0.75)
    ax.set_xlabel('x')
    ax.set_ylabel('Probability')
    ax.set_title('Uniform Random Number')

    
# main function for this Python code
if __name__ == "__main__":
    
    # Set up parser to handle command line arguments
    # Run as 'python PHSX815_HW2_KurtH.py -h' to see all available commands
    parser = argparse.ArgumentParser()
    parser.add_argument("--Read_From", "-r", help="File to read numbers from")
    parser.add_argument("--seed", "-s", help="Seed number to use")
    args = parser.parse_args()

    # default seed
    seed = 5555
    if args.seed:
        print("Set seed to %s" % args.seed)
        seed = args.seed

    if args.Read_From:
        print("Reading numbers from file %s" % args.Read_From)
        readFile = args.Read_From
        myx = np.loadtxt(readFile)
        make_plot(myx)
    
    else:
        # set random seed for numpy
        np.random.seed(seed)

        # class instance of our Random class using seed
        random = Random(seed)

        # create some random data
        N = 10000

        # an array of random numbers from numpy
        x = np.random.rand(N)

        # an array of random numbers using our Random class
        myx = np.array([])
        for i in range(0,N):
            myx = np.append( myx, random.rand())
        make_plot(myx)
    
    plt.show()
