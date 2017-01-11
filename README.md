# This is a repository that keeps our small little group for get started with machine learning algorithm
# Our first start is the playground competition on www.kaggle.com - Santa's Uncertain Bags
# Enjoy!

SETUP
=====
supported python3 only
install python3.x from www.python.org
then install numpy package with
    python -m pip install numpy

RUN
====
```
python -i evolution2.py
```
```
>>> run_test()
```
Script Existing Limitation
==========================
  - fitness is base on total weight improvement, may not accurate/ align to goal
  - it didnt train with feedback result
  - it didnt have local training ground to improve the algorithm/ expedite the improvement

Simulator 
=========
Simulator is made for local training
Usage:
```
    from Simulator import *
    s = Sim(seed)
    score = s.submit(csv)
```
