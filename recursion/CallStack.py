def funcOne():
    funcTwo()
    print("one")

def funcTwo():
    funcThree()
    print("two")

def funcThree():
    print("three")


funcOne()