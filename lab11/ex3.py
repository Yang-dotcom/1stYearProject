# A sparse array is a sequence of numbers in which most entries are zero. An
# efficient way of storing a sparse array is a dictionary in which the keys are the positions
# with nonzero values, and the values are the corresponding values in the sequence. For
# example, the sequence 0 0 0 0 0 4 0 0 0 2 9 would be represented with the dictionary {
# 5:4, 9:2, 10:9 }. Write a function sparseArraySum, whose arguments are two such
# dictionaries a and b, that produces a sparse array that is the vector sum; that is, the result’s
# value at position i is the sum of the values of a and b at position i. [P8.22]
