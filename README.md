# This is a repository that keeps our small little group for get started with machine learning algorithm
# Our first start is the playground competition on www.kaggle.com - Santa's Uncertain Bags
# Enjoy!

SETUP
=====
  - supported python3 only
  - install python3.x from www.python.org
  - install python dependency packages with pip
```
    python -m pip install numpy
    python -m pip install click
```

RUN
====
```
python -i evolution2.py
>>> run_test()
```

Simulator 
=========
Simulator is made for local training
Usage:
```
    from Simulator import *
    s = Sim(seed)
    score = s.submit(csv)

```
or
```
    python simulator.py --seed=[seed] --file=[file]
```
