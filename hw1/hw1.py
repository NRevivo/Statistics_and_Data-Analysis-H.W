###### Your ID ######
# ID1: 322957879
# ID2:
#####################

# imports
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# IMPORTANT - read before you start
# * Do NOT change the names of the functions or the names/order of their parameters.
#   The grader calls every function with keyword arguments and with OTHER values than the defaults.
# * Every function must RETURN its answer (printing is not enough) in the exact type described.
# * Do not run code at the top level of this file (only imports and definitions).
#   You may add helper functions and extra parameters, as long as extra parameters have default values.
# * Allowed packages: numpy, pandas, scipy, matplotlib and the Python standard library.


### Question 1 ###

def binom_pvalue(k=16, n=40, p0=0.2):
    """
    Right-sided p-value of observing k or more successes out of n under the null model Binom(n, p0).

    Returns:
    - a float: P(X >= k) for X ~ Binom(n, p0).
    """
    p_value = stats.binom.sf(k - 1, n, p0)
    return float(p_value)


def critical_k(n=40, p0=0.2, alpha=0.01):
    """
    The rejection threshold of the right-sided binomial test.

    Returns:
    - an int: the smallest k such that P(X >= k) <= alpha for X ~ Binom(n, p0).
      (If no k in 0..n satisfies this, return n + 1.)
    """
    for k in range(n + 1):
        p_value = binom_pvalue(k, n, p0)

        if p_value <= alpha:
            return k

    return n + 1    
    


def power(n=40, p0=0.2, p1=0.35, alpha=0.01):
    """
    The power of the test that rejects H0 when X >= critical_k(n, p0, alpha).

    Returns:
    - a float: the probability to reject H0 when the true success probability is p1.
    """
    k = critical_k(n, p0, alpha)
    return binom_pvalue(k, n, p1)


def power_drops(p0=0.2, p1=0.35, alpha=0.01, n_max=150):
    """
    Returns:
    - a sorted 1-d numpy array of ints: every n in {2, ..., n_max} for which
      power(n, p0, p1, alpha) < power(n - 1, p0, p1, alpha).
    """
    drops = []

    for n in range(2, n_max + 1):
        current = power(n, p0, p1, alpha)
        previous = power(n - 1, p0, p1, alpha)

        if current < previous:
            drops.append(n)

    return np.array(drops, dtype=int)


def min_sample_size(p0=0.2, p1=0.35, alpha=0.01, target=0.8):
    """
    Returns:
    - an int: the smallest number of patients n >= 1 for which power(n, p0, p1, alpha) >= target.
    """
    n = 1

    while power(n, p0, p1, alpha) < target:
        n += 1

    return n


### Question 2 ###

def shots_pmf(t=10, r=3, p=0.4):
    """
    T is the number of shots a player with success probability p takes until the r-th success.

    Input:
    - t: an int OR a 1-d numpy array of ints.

    Returns:
    - P(T = t): a float if t is an int, a 1-d numpy array of the same length if t is an array.
    """
    return stats.nbinom.pmf(t - r, r, p)


def duel_probs(pA=0.3, rA=5, pB=0.45, rB=8):
    """
    Two players shoot synchronously (one shot each per round). Player A needs rA successes and has success
    probability pA; player B needs rB successes and has success probability pB. All shots are independent.

    Returns:
    - a tuple of 3 floats: (P(A completes strictly before B), P(both complete in the same round),
                            P(B completes strictly before A)).
    """
    a_win = 0.0
    b_win = 0.0
    tie = 0.0
    t = 1

    while True:
        a = shots_pmf(t, rA, pA)
        b = shots_pmf(t, rB, pB)

        a_survives = stats.nbinom.sf(t - rA, rA, pA)
        b_survives = stats.nbinom.sf(t - rB, rB, pB)

        a_win += a * b_survives
        b_win += b * a_survives
        tie += a * b

        if max(a_survives, b_survives) < 1e-12:
            break

        t += 1

    return (float(a_win), float(tie), float(b_win))


def duel_expected_length(pA=0.3, rA=5, pB=0.45, rB=8):
    """
    Same setting as duel_probs.

    Returns:
    - a float: the expected number of rounds until the FIRST of the two players completes her task.
    """
    expected = 0.0
    t = 0

    while True:
        a_survives = stats.nbinom.sf(t - rA, rA, pA)
        b_survives = stats.nbinom.sf(t - rB, rB, pB)

        prob_continue = a_survives * b_survives

        expected += prob_continue

        if prob_continue < 1e-12:
            break

        t += 1

    return float(expected)


### Question 3 ###

def conv_pmf(P, Q):
    """
    Input:
    - P, Q: 2-d numpy arrays [[values], [probabilities]] of two independent random variables X ~ P, Y ~ Q.
      The values are integers (not necessarily sorted, consecutive, or positive).

    Returns:
    - a 2-d numpy array [[values], [probabilities]] with the distribution of X + Y,
      values sorted in increasing order (values with probability 0 may be included or omitted).
    """
    result = {}

    for x, px in zip(P[0], P[1]):
        for y, py in zip(Q[0], Q[1]):
            z = int(x + y)

            result[z] = result.get(z, 0.0) + px * py

    values = sorted(result.keys())
    probabilities = [result[v] for v in values]

    return np.array([values, probabilities])


def nfold_pmf(P, n=2):
    """
    Input:
    - P: 2-d numpy array [[values], [probabilities]] with integer values.
    - n: an int >= 1.

    Returns:
    - a 2-d numpy array [[values], [probabilities]] with the distribution of X_1 + ... + X_n,
      where X_1, ..., X_n are independent and each has the distribution P (sorted values).
    """
    pass


### Question 4 ###

def cc_cdf(N=20, t=60):
    """
    T_N is the waiting time (number of draws) for a full collection of N equiprobable coupons.

    Returns:
    - a float: P(T_N <= t), computed exactly (no simulation), with a RELATIVE error below 1e-6
      even when the probability is tiny (e.g. 1e-40).
    """
    pass


def cc_partial_quantile(N=100, m=80, q=0.95):
    """
    Returns:
    - an int: the smallest t such that P(at least m different coupons appear among the first t draws) >= q.
    """
    pass


### Question 5 ###

def clean_log(df):
    """
    Input:
    - df: a pandas DataFrame with the raw inspection log (as returned by pd.read_csv on a log file).

    Returns:
    - a pandas DataFrame with ONE row per usable batch (a batch whose true number of defective items can be
      determined from the log) and (at least) the columns: batch_id, machine, inspected, defective,
      holding the TRUE values. Machine names must be exactly 'A', 'B', 'C' or 'D'.
    """
    pass


def defect_rates(df):
    """
    Input:
    - df: a raw inspection log (pandas DataFrame).

    Returns:
    - a dict {machine: estimated defect rate}, e.g. {'A': 0.031, 'B': 0.052, 'C': 0.044, 'D': 0.027}.
      The estimated rate of a machine = (total defective items) / (total inspected items) over its usable batches.
    """
    pass


def log10_pvalue(df, machine='B', p0=0.03):
    """
    Input:
    - df: a raw inspection log (pandas DataFrame).
    - machine: 'A', 'B', 'C' or 'D'.
    - p0: the defect rate claimed by the manufacturer.

    Returns:
    - a float: log10 of the right-sided binomial p-value P(X >= D), X ~ Binom(N, p0), where N and D are the total
      numbers of inspected and defective items of this machine (over its usable batches).
      Must be accurate (relative error < 1e-6) even when the p-value is smaller than 1e-300.
    """
    pass


def items_needed(df, machine='A', r=10, q=0.95):
    """
    Input:
    - df: a raw inspection log (pandas DataFrame).

    Returns:
    - an int: the smallest number n of products from this machine we need to inspect so that
      P(at least r of them are defective) >= q, assuming each product is defective independently
      with probability equal to the machine's estimated defect rate (from defect_rates).
    """
    pass
