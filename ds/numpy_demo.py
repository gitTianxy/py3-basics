# coding=utf8
"""
I. numpy-array vs python list
---
1. Arrays support vectorised operations, while lists don’t.
2. Once an array is created, you cannot change its size. You will have to create a new array or overwrite the existing one.
3. Every array has one and only one dtype. All items in it should be of that dtype.
4. An equivalent numpy array occupies much less space than a python list of lists.
"""
import numpy as np


def print_version():
    print("numpy version:", np.__version__)


def array_operate():
    """
    array operations: create, transform, copy, generate(sequence, random, repeat)
    ---
    Tips:
    1. `np.random.RandomState` or `np.random.seed`: If you want to repeat the same set of
    random numbers every time, you need to set the seed or the random state.
    The see can be any value. The only requirement is you must set the seed to the same value
    every time you want to generate the same set of random numbers.
    """
    print('---array operations')
    l = list(range(10))
    arr1d = np.array(l)
    print(f"type: {type(arr1d).__name__}, content: {arr1d}")
    print(f"{arr1d} + 1: {arr1d+1}")
    for i in l:
        if i % 2 == 0:
            l[i] = str(i)
    arr1do = np.array(l, dtype='object')
    print(f"object array:", arr1do)
    l2d = [[j for j in range(i - 3, i)] for i in range(3, 10, 3)]
    arr2d = np.array(l2d)
    print("2d array:", arr2d)
    arr2df = np.array(l2d, dtype='float')
    print("2d float array:", arr2df)
    arr2db = arr2d.astype(dtype='bool')
    print("2d boolean array:", arr2db)
    arr2db2 = arr2d > 0
    print("2d boolean array 2:", arr2db2)
    print("convert array 2 list:", l2d == arr2d.tolist())

    # sequence
    print("seq 0 to 5:", np.arange(5))
    print("seq 0 to 9:", np.arange(0, 10))
    print("seq 0 to 9 with step of 2:", np.arange(0, 10, 2))

    # generate random numbers
    print("Random numbers between [0,1) of shape 2,2:", np.random.rand(2, 2))
    print("Normal distribution with mean=0 and variance=1 of shape 2,2:", np.random.randn(2, 2))
    print("Random integers between [0, 10) of shape 2,2:", np.random.randint(0, 10, size=[2, 2]))
    print("One random number between [0,1):", np.random.random())
    print("Pick 10 items from a given list, with equal probability:",
          np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
    print("Pick 10 items from a given list with a predefined probability 'p':",
          np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10, p=[0.3, .1, 0.1, 0.4, 0.1]))

    # repeat
    a = np.arange(5)
    print("Repeat whole of 'a' two times:", np.tile(a, 2))
    print("Repeat each element of 'a' two times:", np.repeat(a, 2))


def array_prop():
    """
    get properties of array
    :return:
    """
    print("---get properties of array")
    l2d = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]]
    arr2df = np.array(l2d, dtype='float')
    print('Shape: ', arr2df.shape)
    print('Datatype: ', arr2df.dtype)
    print('Size: ', arr2df.size)
    print('Num Dimensions: ', arr2df.ndim)


def array_elements():
    """
    extract elements from array
    ---
    You can extract specific portions on an array using indexing starting with 0,
    something similar to how you would do with python lists.
    Additionally, numpy arrays support boolean indexing--extract elements by boolean index
    """
    print("---operations on array elements")
    l2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr2d = np.array(l2d)
    print("array:", arr2d)
    print(f"element at position ({1},{1}): {arr2d[1,1]}")
    print(f"elements at postion [:{2},:{2}]: {arr2d[:2, :2]}")
    print("reverse row positions:", arr2d[::-1, ])
    arr2db = arr2d > 5
    print(f"elements greater than 5:", arr2d[arr2db])


def array_analysis():
    """
    1. not a number, infinite element
    nan, inf should assign to float datatype
    2. mean,max,min
    3. uniques
    """
    print("---array analysis")
    l2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr2 = np.array(l2d, dtype='float')
    # add nan, inf
    arr2[1, 1] = np.nan
    arr2[1, 2] = np.inf
    print("array:", arr2)
    # check nan, inf, label as -1
    arr2_isnan = np.isnan(arr2)
    arr2[arr2_isnan] = -1
    print(f"label 'nan' as -1: {arr2}")

    print("Mean value is: ", arr2.mean())
    print("Max value is: ", arr2.max())
    print("Min value is: ", arr2.min())

    arr_rand = np.random.randint(0, 5, size=10)
    print("arr_rand:", arr_rand)
    uniqs, counts = np.unique(arr_rand, return_counts=True)
    print("Unique items : ", uniqs)
    print("Counts       : ", counts)


if __name__ == '__main__':
    print_version()
    array_operate()
    array_prop()
    array_elements()
    array_analysis()
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)
    print(np.hstack((a,b)))
