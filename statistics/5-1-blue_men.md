[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

How many people are between 5'10" and 6'1"?

In [36]:
```
# 5'10" = 177.8cm , 6'1" = 185.9cm
low = 177.8
high = 185.9
dist.cdf(high) - dist.cdf(low)
```
Out[36]:
```
0.35790905843912685
```

About 36% of the male population is between 5'10" and 6'1".
