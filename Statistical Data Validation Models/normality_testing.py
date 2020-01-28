# Importing data managment and transformation packages:
import pandas as pd
import numpy as np
import scipy
# Importing data vizualization packages:
import matplotlib as mpl
import matplotlib.pyplot as plt


class normality_validation(object):
    """
    The normality_validation object is designed to perform visual and
    statistical tests to determine if the data conforms to a normal distribution.
    The tests are broken down into two main sections: visual and statistical.

    Methods
    -------
    visual_tests()
        This method performs both visual tests for normality on the dataframe:
        a histogram plot and a Quantile-Quantile Plnt

    results_sum()
        This method initalizes all the statistical normality tests and compiles
        their return results in a summary dataframe.

    shapiro-wilk_test()
        The method performs the shapir0-wilk test for normality.

    k^2_test()
        The method performs the D’Agostino’s K^2 test for normality.

    anderson_darling_test()
        The method performs the Anderson-Darling test for normality.

    kolmogorov-smirnov_test()
        The method performs the Kolmogorov–Smirnov test for normality.

    """

    def __init__(self, input_data):
        """
        Parameters
        ----------
        input_data : Pandas dataframe/Series
            This is the dataframe that the normality tests will be performed on. The
            test is designed to perform analysis on a dataframe with a single column.
        """
            pass
