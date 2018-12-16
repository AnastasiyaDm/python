# TASK-1
# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Assume that:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

from random import randint
N = randint(1, 100000)
A = [randint(-1000000, 1000000) for x in range(0, N)]


def solution(a):
    return min(list(filter(lambda x: x > 0 and x not in a, [int(i) for i in range(0, 1000000)])))


print(A)
print(solution(A))
