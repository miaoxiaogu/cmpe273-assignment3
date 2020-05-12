# cmpe273-assignment3
- Result of test_lru_cache.py
cache hit
cache hit
cache hit
cache hit
fibonacci(6)=8

{'id': 1, 'value': 'Foo Bar - 1'}
{'id': 2, 'value': 'Foo Bar - 2'}
{'id': 3, 'value': 'Foo Bar - 3'}
{'id': 4, 'value': 'Foo Bar - 4'}
cache hit
{'id': 1, 'value': 'Foo Bar - 1'}
cache hit
{'id': 2, 'value': 'Foo Bar - 2'}
cache hit
{'id': 3, 'value': 'Foo Bar - 3'}
cache hit
{'id': 4, 'value': 'Foo Bar - 4'}
{'id': 5, 'value': 'Foo Bar - 5'}
{'id': 6, 'value': 'Foo Bar - 6'}
Num of function calls:10
Num of cache misses:6

- Result of test_bloom_filter.py
'accessable' is probably present!
'bloom' is probably present!
'twitter' is a false positive!
'abundant' is probably present!
'abundance' is probably present!
'facebook' is definitely not present!
'bolster' is probably present!
'bonus' is probably present!
'blossom' is probably present!
'bonny' is probably present!
'abounds' is probably present!
'abound' is probably present!

- Answer the following question:

What are the best k hashes and m bits values to store one million n keys (E.g. e52f43cd2c23bb2e6296153748382764) suppose we use the same MD5 hash key from pickle_hash.py and explain why?
k is 4 and m is 6235224.
n = 1million p = 0.05 
use the  formula to calculate Bit array size:m = int(- (n * ln(p)) / (ln(2)^2) )    
=>     m =  6235224        
use the formula k = int((m/n)ln(2) )    
=>    num_hash k = 4
