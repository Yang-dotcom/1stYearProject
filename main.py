##
# def main():
#     foo = int(input("square size: "))
#     drawSquare(foo)
#
#
# def drawSquare(size):
#     for l in range(size):
#         drawLine(size)
#
#
# def drawLine(anyone):
#     print("#" * anyone)
#
#
# main()

##
# def foo (x):
#     okay = x ** 3
#     return okay, "hello"     #I need to return something, else I get output "none" (no value) because okay is not defined.
# z, nice = foo(2)
# print(foo(3), z, nice)


## Parameter passing.
# the object "james bond" defined by the variable stringObject in the global frame is passed to the parameter s, such that it's used in the foo frame.
# def foo(s):
#     print(f"you called the function with \"{s}\" as argument")
#
# stringObject = "james bond"
# foo(stringObject)

## List = dynamic data structure
# values = ["nice", "hello", "ok"]
#
# def main():
#     values = ["nice", "hello", "ok"]
#     for i, b in enumerate(values):
#         print(f"I love {i+1} and then {b}")
#
# if __name__ == '__main__':
#     main()
## .insert method
# values = ["nice", "hello", "ok", 4, "no", "nada"]
# print(values.index("hello"))
# values.insert(1, "meow")
# print(values, values.index("hello"))
##
# def main():
#     foo = list("Giovanni Adolfo Pietro Pio Squillero")
#     # pos = myIndex(foo, "i")
#     # while "i" in foo:
#     #     i = foo.index("i")
#     #     foo[i] = "X"
#     replacedList = subI(foo)
#     print(replacedList)
#
# def subI(foo):
#     """Replaces every "i" with "X" """
#     while "i" in foo:
#         i = foo.index("i")
#         foo[i] = "X"
#     return foo
# def myIndex(list_, element):
#     """Returns a list with all the positions of element "i" in list_"""
#     pos = []
#     for i, e in enumerate(list_):
#         if e == element:
#             pos.append(i)
# #     return pos
# if __name__ == '__main__':
#     main()
## element separator
# def main():
#     friends = ["Alice", "Bob", "Carla", "David"]
#
#     results = ""
#     # for n in friends[:-1]:
#     #     results += n + ", "
#     # results += friends[-1]
#     #
#     # print(f"{results}")
#
#     results = ", ".join(friends)
#     print(results)
#
# if __name__ == '__main__':
#     main()

## custom min function
# import random
#
# def main():
#     array = []
#     for i in range(1_000):
#         array.append(random.randint(-10_000, +10_000))
#
#     smallest = largest = None
#
#     for e in array:
#         if largest is None or e > largest:
#             largest = e
#         if smallest is None or e < largest:
#             smallest = e
#
#     print(f"smallest is {smallest}, largest is {largest}")
#
# if __name__ == '__main__':
#     main()

## linear search

# import random
#
# def main():
#     array = []
#     for i in range(100):
#         array.append(random.randint(-1_000, +1_000))
#
#     target = 42
#     found = None
#
#     for i,e in enumerate(array):
#         if e == target and found is None:
#             found = i
#
#     if found is not None:
#         print((f"Element {target} found at position {found}"))
#     else:
#         print(f"Element {target} found at position {found}")
#
#
# if __name__ == '__main__':
#    main()

## remove and loop through list
# array = [4, 1, 8, 3, 4, 5, 9, 4]
#
# for i in range(len(array)):
#     if i <= len(array): # one way to avoid going out of index. although popping the element in a reversed list is preferrable
#         if array[i] == 4:
#             array.pop(i)
#
# print(array)
## compute and print frequency of each die value.

#   dice fairness
# NUM_VALUES = 60000
# import random
# def main():
#     """Main entry point"""
#     dieValues = list()
#     for i in range(NUM_VALUES):
#         dieValues.append(random.randint(1,6))
#     print(dieValues)
#     if check(dieValues):
#         print("The dice is fair")
#     else:
#         print("The dice is not fair")
#
#
# def check(values):
#     """Check whether the dice is fair"""
#     # frequency = [0, 0, 0, 0, 0, 0]
#     #step 1: count results
#     # for r in values:
#     #     frequency[r-1] = frequency[r-1] + 1
#     frequency = []
#     for r in range(6):
#         frequency.append(values.count(r+1) / len(values))
#     print(frequency)
#
#     #normalize:
#     # for f in range(len(frequency)):
#     #     frequency[f] = frequency[f] / len(values)
#     # check them
#     expectedFrequency = 1/6
#     acceptableError = 0.01
#     allCorrect = True
#     for f in frequency:
#         if abs(f - expectedFrequency) > acceptableError:
#             allCorrect = False
#     return allCorrect
#
#
#
#
# if __name__ == '__main__':
#     main()

## tables

# ROWS = 3
# COLUMNS = 5
#
# table = []
#
# for i in range(ROWS):
#     table.append(([0] * COLUMNS))
# table[2][1] = 99
# print(table)
#
#

## Convert from one base to another
# def main():
#     """Main entry point"""
#     number = int(input("Number: "))
#     base = int(input("Base: "))
#     value = convert(number, base)
#     print(f"{number}|10 = {value}|{base}")
#
# def convert(number, base):
#     """Convert base 10 to any other base"""
#     result = ""
#     while number > 0:
#         result = result + str(number % base)
#         number = number // base
#     if result == "":
#         result = 0
#     return result[::-1]

# def convert(number, base):
# """Convert any other base to base 10"""
#     value = 0
#     for n, d in enumerate(reversed(str(number))):
#         value += int(d) * base ** n
#     return value
#
# if __name__ == '__main__':
#     main()
#

##  better converter
# AVAILABLE_DIGITS = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# def main():
#     number = input("Enter value to be converted: ")
#     baseFrom = int(input("Base to convert from: "))
#     baseTo = int(input("Base to convert To: "))
#     value = None
#     result = None
#     if baseFrom == 10:
#         value = int(number)
#     else:
#         value = convertBase10(number, baseFrom)
#
#     if baseTo == 10:
#         result = str(value)
#     else:
#         result = convertGenericBase(value, baseTo)
#
#     print(f"{number}|{baseFrom} = {result}|{baseTo}")
#
#
# def convertGenericBase(number, base):
#     """Convert a number in base10 to a different base(return a str)"""
#     result = ""
#     while number > 0:
#         result = result + hexadecimalDigit(number % base)
#         number //= base
#     if result == "":
#         result = "0"
#     return result[::-1]
#
# def convertBase10(number, baseFrom):
#     """Convert a number in any base to base 10"""
#     result = 0
#     for d in number:
#         result = result * baseFrom + singleValue(d)
#     return result
#
#
# def hexadecimalDigit(val):
#     """Hexadecimal digit of a certain value"""
#     print(val)
#     return "0123456789ABCDEF"[val]
#
# def singleValue(digit):
#     """Value of a single hexadecimal digit"""
#     return "0123456789ABCDEF".index(digit.upper())
#
# if __name__ == '__main__':
#     main()

## Text File handling (write missing)

# FILENAME = 'sample.txt'

# def main():
#     input_file = open(FILENAME, 'r')
#     ## for line in input_file:
#     #     line = line.rstrip()
#     #     for word in line.split():
#     #         trimmed_word = word.strip('.,!?\'"')
#     #         print(f">>>{trimmed_word}<<<")
#     #chunk = input_file.read()
#     ## while chunk != '':
#     #     print(f"Chunk: >>{chunk}<<")
#     #     chunk = input_file.read(5)
#     ## for line in chunk.splitlines():
#     #     print(f"Chunk: >>{line.rstrip()}<<")
#
#     input_file.close()
#
# if __name__ == '__main__':
#     main()

## defining parameters when calling a function
# def foo(day, month):
#     print(f"Hey, day = {day} and month = {month}")
#
# def main():
#     foo(23, 10)
#     foo(month=10, day=23)
#
# if __name__ == '__main__':
#     main()

## example of managing 2 text files
# POPULATION_FILENAME = 'population.txt'
# AREA_FILENAME = 'area.txt'
#
# def main():
#     population = []
#     file1 = open(POPULATION_FILENAME, 'r')
#     for line in file1:
#         ## country, population = line.rsplit(maxsplit=1)
#         # print(f"{country}: {int(population):,}")
#         country, pop = line.rsplit(maxsplit=1)
#         population.append((country, int(pop)))
#     file1.close()
#     print(f"Population: {population}")
#
#     file2 = open(AREA_FILENAME, 'r')
#     area = []
#     for line in file2:
#         country, a = line.rsplit(maxsplit=1)
#         area.append((country, float(a)))
#     file2.close()
#     print(f"Area: {area}")
#
#     for i in range(len(area)):
#         print(f"{population[i][0]}: density {population[i][1] / area[i][1]: .2f}")
#
#
# if __name__ == '__main__':
#     main()

## Exception handling

# def foo(x):
#     if x == 42:
#         raise ValueError("Can't handle 42")
#     print(f"x is {x}")
#
# def main():
#     try:
#         foo(23)
#         foo(42)
#         foo(10)
#     except ValueError as ve:
#         print(f"Lmao: {ve}")
#     finally:
#         print("That's all..")
#
# if __name__ == '__main__':
#     main()
# use WITH compound statement block to open file and close it automatically when you exit the block.

# a = [1, 2, 3]
# foo = (2, a)
# a.pop()
# print(foo)

## Computer Architecture
"""
input device = everything that is used to give information to the computer (keyboard, mouse, microphone)
output device =  everything that is used to give info from computer to outside world (e.g. monitor, loudspeaker)
asynchronous analog signals are used by the human body (signal that can have all possible values and can change at every single instant)
syncrhonous = interested in specific instant; digital = interested in specific value

an analog signal has intrinsic error (real world error) that carries over and may increase when copied (increase in noise)
a digital signal doesn't lose accuracy coping a digital signal
from analog to digital there is possibility of losing quality because of compression
the output from either analog or digital is defacto analog thus may add noise.

External Memory:
    storage hardware that is cheaper, but slower than internal memory
    external memory does not depend on Abus because it's considered a peripheral.
CPU (central processing unit) is made up of main blocks:
    1) CONTROL UNIT: kernel (brain or heart) of CPU. I.e. the director that gives out instructions. Made of:
        - Program Counter = Fetches instruction. point in memory (memory = big indexed list) where I'm supposed to find instructions on what I need to do. It has a counter that increases as it moves to another instruction. The instruction is encoded.
        - Instruction register = holds the current instruction so that it can be  decoded and inputed to the Control logic
        - Control Logic = hardware that's able to read instructions given by the Instruction Register and issue a command.
        - Various registers such as: [Register = local memory elements used to store data temporally. It's has word dimensions (64 bit)]
            [Flag register = state indicator of the ALU (arithmetic logic unit) result. It's single bit (0 = false, 1 = True).
                the most common flags are Z (zero), V (overflow), CY (carry), N (negative)]
            [ALU register performs all integer computations, FPU (floating point unit) performs floating point computations. FPU is legacy since it's not as used anymore]
        clock period = distance between two peaks of a repetitive clock signal.
        clock frequency = reciprocal of clock period
        machine-cycle = time interval to execute a basic operation. integral multiple of the clock period
    2) MEMORY (DRAM):
        1) Addressing: Memory is organized in cells (min directly accessible unit) an address (index number) is assigned to each cell to identify it. The size of one cell is one byte
            [1 byte = 8 bit] remember convention we call the size of a cell with byte.
        2) Parallelism : how much information we're able to transfer to and out of the memory at same time.
        3) Internal memory : small, volatile (data is lost if pc is unplugged) fast, expensive, called main memory
            maximum size of internal memory: maximum index that one can use. max index = 2^(bits allocated to select the cell)
             the channel to read and write cells is called Bbus and is 64bit nowdays.
    3) BUS: circulatory system of the PC.
        - transports data
        - frequency = n. of bits transported in a second
        - width = n. of bit composing a single data
        can be a significant bottleneck if single bus in a system because it allows only 2 elements in the system to comunicate.
        A single bus is composed of:
            1) Data Bus (Dbus)
            2) Address Bus(Abus)
            3) Control (Cbus)
        in the CPU a single unit handles the coordination of the buses

"""
