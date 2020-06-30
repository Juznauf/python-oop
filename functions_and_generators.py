

def outer():
    x = 'old'
    def _changer():
        nonlocal x # when call non local, variable x will be avilable in the local scope of outer(), of there is another variable named x in the function body, it will be overided by this x as there are in the same namespace now 
        x = 'somewhat nonlocal'
        return 0
    _changer()
    return x

x = [24]
def go_global():
    global y 
    y = 'new' # will ensure that the variable y can be used outside of the scope of the function 
    # best to use if we want to use y in the main scope without returning y
    return 0


if __name__ == "__main__":
    print("to test the global names")
    print(go_global())
    print(y)

    print("\nTo test the non local names")
    print(outer())
