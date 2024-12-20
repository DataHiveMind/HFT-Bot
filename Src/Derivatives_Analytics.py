import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from dataclasses import dataclass

mpl.rcParams['font.family'] = 'serif'

@dataclass
class derivatives_analytics():
    pass

    def basic():
        # Option Strike
        k = 8000

        # Graphical Output
        s = np.linspace(7000, 9000, 100) # index level values
        h = np.maximum(s - k, 0) # inner values of call option

        plt.figure()
        plt.plot(s, h, lw = 2.5)
        plt.xlabel("Index Level")
        plt.ylabel("Inner value of European call option")
        plt.grid(True)