# Python for financial research (2018 workshop)

[Vincent Grégoire](http://www.vincentgregoire.com), University of Melbourne

This repository contains material for the 2018 Python for financial research workshop for honours and Ph.D. students at the University of Melbourne.

## Outline

The workshop is divided into four blocks of three hours each:

**1. Introduction to Python programming**

We will discuss what Python is and you will learn the basic structure of the
language. You will also learn your way around the programming environment,
including the two main editors for scientific Python, Spyder, and Jupyter.
You will learn how to import and explore data using pandas by generating summary statistics and plotting graphs using matplotlib.

**2.    Introduction to data analysis using pandas and matplotlib**

You will learn how to import, export and transform data using pandas, the
panel data package for Python. You will also see how to do basic portfolio
analysis while replicating a classic paper.

Recommended reading: [Bondt, W.F. and Thaler, R., 1985. Does the stock market overreact?. The Journal of finance, 40(3), pp.793-805.](http://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1985.tb05004.x/full)

**3.    More data analysis using pandas and statsmodels**

You will learn more advanced features of Python and pandas, including dealing
with timestamps and estimating measures from daily and intraday data. You
will also learn how to estimate OLS and panel regressions using statsmodels.

**4.    Other topics**

In this block, you will be introduced briefly to other Python packages that 
can be helpful for research. We will look at an example of web scraping with
textual analysis.

## Software

I recommend the [Anaconda distribution](https://www.anaconda.com/download/),
which is available for Windows, Mac OS and  Linux. We are using the Python
3.6 version for the workshop.


## Material


### Slides

- [Python for Financial Research (PDF)](https://github.com/vgreg/python-finance-unimelb2018/blob/master/slides/PythonWorkshopMarch2018.pdf)
- [Introduction to Web Scraping with Python (PDF)](https://github.com/vgreg/python-finance-unimelb2018/blob/master/slides/WebScrapingPythonMarch2018.pdf)


### Code


**Note**: this code is for illustrative purpose, and does not necessarily show
the *correct* or *best* way to do something, the main goal is to illustrate
the Python language, its libraries, and some common use cases in research.

**Block 1:**

- [PythonIntro.py](https://github.com/vgreg/python-finance-unimelb2018/blob/master/code/PythonIntro.py): Introduction to the Python language.
- [Kickstarter exploration](https://github.com/vgreg/python-finance-unimelb2018/blob/master/notebooks/kickstarter/KickstarterExploration.ipynb): Introduction to data exploration using a Kickstarter dataset.

**Block 2:**

- [DeBondt and Thaler 1985](https://github.com/vgreg/python-finance-unimelb2018/blob/master/notebooks/debondt_thaler_1985/DeBondtThaler.ipynb): Partial replication of a paper with portoflio formation.

**Block 3:**

- [Introduction to empirical market microstructure in Python](https://github.com/vgreg/python-finance-unimelb2018/blob/master/notebooks/micrsostructure/ASX_Microstructure.ipynb): Intro to using pandas with intraday data.
- [Estimating standard errors in Python](https://github.com/vgreg/python-se): Using statsmodels and pandas for panel regressions.

**Block 4:**

- [SEC Press Releases](https://github.com/vgreg/python-finance-unimelb2018/blob/master/notebooks/micrsostructure/SEC_News_Releases.ipynb): Scrape data from website and apply textual (sentiment) analysis.

