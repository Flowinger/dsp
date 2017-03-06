[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

Compute the median, mean, skewness and Pearson’s skewness of the resulting sample. 
```
In [52]:
Mean(sample), Median(sample)
Out[52]:
(74278.707531187203, 51226.454478940461)

In [53]:
Skewness(sample), PearsonMedianSkewness(sample)
Out[53]:
(4.9499202444295829, 0.7361258019141782)
```

What fraction of households report a taxable income below the mean? 
```
In [59]:
cdf.Prob(Mean(sample))
Out[59]:
0.66000587956687196
```

All of this is based on an assumption that the highest income is one million dollars, but that's certainly not correct. What happens to the skew if the upper bound is 10 million?
Without better information about the top of this distribution, we can't say much about the skewness of the distribution.
```
In [48]:
Mean(sample2), Median(sample2)
Out[48]:
(124267.39722164685, 51226.454478940461)

In [49]:
Skewness(sample2), PearsonMedianSkewness(sample2)
Out[49]:
(11.603690267537793, 0.39156450927742087)

In [51]:
cdf2.Prob(Mean(sample2))
Out[51]:
0.8565630665207663
```

Reasons that there is a right skew:
  - Mean is bigger than median
  - Skewness & Pearson Median Skewness are positive

If the upper bound is changed
  - Skewness increases
  - Pearson Median Skewness decreases
  - Mean dramatically increases 
  - Both measure (skewness and mean) are sensitive to the upper bound
