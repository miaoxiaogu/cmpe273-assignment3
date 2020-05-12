from random import shuffle
from bitarray import bitarray
import mmh3
import math

class BloomFilter():
    def __init__(self,num_keys,false_positive_probability):
        self.num_keys = num_keys
        self.false_positive_probability = false_positive_probability
        self.num_bit = self.get_num_bit(num_keys,false_positive_probability)
        self.num_hash = self.get_num_hash(self.num_bit,num_keys)
        self.bit_array = bitarray(self.num_bit)
        self.bit_array.setall(0)
        
        
    def get_num_bit(self,num_keys,false_positive_probability):
        res = int(-(num_keys*math.log(false_positive_probability))/(math.log(2)**2))
        return res
        
    def get_num_hash(self,num_bit,num_keys):
        res = int((num_bit/num_keys)*math.log(2))
        return res
       
    
    def add(self,key):
        res = []
        i = 0
        while i < self.num_hash:
            temp = mmh3.hash(key,i) % self.num_bit
            res.append(temp)
            self.bit_array[temp] = True
            i = i + 1
            
    def is_member(self,key):
        i = 0
        while i < self.num_hash:
            index = mmh3.hash(key,i) % self.num_bit
            if self.bit_array[index] == False:
                return False
            i = i + 1
        return True

#if __name__ == "__main__":
#    a = BloomFilter(1000000,0.05)
#    res = a.get_num_bit(1000000,0.05)
#    print(res)
#    res2 = a.get_num_hash(res,1000000)
#    print(res2)
