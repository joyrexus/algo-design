My implementation of the Gale/Shapley algorithm in Python.  This algorithm is designed to address the [Stable Marriage Problem](http://en.wikipedia.org/wiki/Stable_marriage_problem).

Compare this recursive variant with the implementations on [Rosetta Code](http://rosettacode.org/wiki/Stable_marriage_problem#Python).


## Problem description

Given an equal number of men and women to be paired for marriage, each man ranks all the women in order of his preference and each women ranks all the men in order of her preference.

A stable set of engagements for marriage is one where no man prefers a women over the one he is engaged to, where that other woman also prefers that man over the one she is engaged to. I.e. with consulting marriages, there would be no reason for the engagements between the people to change.

Gale and Shapley proved that there is a stable set of engagements for any set of preferences and the first link above gives their algorithm for finding a set of stable engagements.


## Task Specifics

We're provided with a list of men (`M`) and women (`W`), indicating each mans (and womans) spousal preferences ranked from highest to lowest.

The task is to implement the Gale-Shapley algorithm for finding a stable set of engagements.

We want to use this algorithm to produce a matching, which we can then test for
stability by the criteria indicated above.

We're also asked to perturb the resulting matching (swapping the spouses of two
couples) and re-test for stability.  The perturbed matching should be found to
be unstable.
