# abv-calculation-py
Python script to calculate ABV from Plato density readings. No dependencies.

Uses an alternative formula for ABV calculation in high-abv beers (default > 8%).

## Usage examples
ABV > 8.0 %
```python
python abv-calculation.py -t 9.0 -o 20 -f 4
>>> 9.47 %
```

ABV < 8.0 %
```python
python abv-calculation.py -t 6 -o 14 -f 3
>>> 5.92 %
```
