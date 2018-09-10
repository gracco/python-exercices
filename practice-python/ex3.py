#Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

def main():
    compareLists()

def compareLists():
    listA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    new_list = []
    number = 5
    for interactor in listA:
        if interactor < number:
            new_list.append(interactor)
    for interactor in new_list:
        print(interactor, end=' ')


if __name__ == "__main__":
    main()