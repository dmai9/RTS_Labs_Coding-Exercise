# Problem 1
def aboveBelow(arr: [], target: int) -> None:
    above = 0
    below = 0
    for i in arr:
        if (i > target):
            above += 1
        elif (i < target):
            below += 1
    print("above: " + str(above) + ", below: " + str(below))


# Problem 2
def rotateStr(string: str,target: int) -> str:
    string = list(string)
    newStr = [None] * len(string)
    for i in range(len(string)):
        newLoc = (i + target) % len(string)
        newStr[newLoc] = string[i]
    return "".join(newStr)

# Problem 3
'''
If I could change one thing about Python, it would be that Python is able to support multithreading.
Currently, Python is unable to support it due to Global Interperter Lock (GIL) which essentially
only allows one thread to run at a time. Though there are solutions out there for this such as multiprocessing
it takes more space and is also time consuming. It would be ideal for a multithreading because it is more economical
and with the growing interest in Python from both the software and data science field, it would help a lot of
Python programmers improve the speed of their program.

'''