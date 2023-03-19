# python3

def SiftDown(data, swaps, i):
    # tiek iziets cauri visiem elementiem un maina tos vietām

    # iegūst masīva garumu
    n = len(data)
    indekss = i
    
    # pārbauda leftchild un, vai ir datu robežās
    leftchild = 2 * i + 1
    mc = leftchild < n and data[leftchild] < data[indekss]
    indekss += mc * (leftchild - indekss)
    leftchild += mc
    
    rightchild = 2 * i + 2
    mc = rightchild < n and data[rightchild] < data[indekss]
    indekss += mc * (rightchild - indekss)
    rightchild += mc

    if indekss != i:
        swaps.append((i, indekss))
        data[i], data[indekss] = data[indekss], data[i]
        SiftDown(data, swaps, indekss)


def build_heap(data):
    swaps = [] 

    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    # veido koku un sakārto vēlamajā secībā
    n = len(data)
    i = n // 2 - 1
    while i >= 0:
        SiftDown(data, swaps, i)
        i -= 1
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    
    text = input("Input 'I' or 'F': ")
    
    # input from keyboard
    if "I" in text:
        n = int(input("Input the size: "))
        data = list(map(int, input("Input the heap: ").split()))
        
        # checks if lenght of data is the same as the said lenght
        assert len(data) == n

    elif "F" in text:
    # nolasa faila nosaukumu
        print("Input filename: ")
        faila_nosaukums = input()
    # pārbauda vai faila nosaukums satur "a"
        # if "a" in faila_nosaukums:
        #   print("Nederīgs faila nosaukums!")

    # atver failu un nolasa vērtības
        cels = "./tests/"
        with open(cels + faila_nosaukums, 'r') as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
