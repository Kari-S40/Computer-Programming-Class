import random  # to use random.choice(list)

def main():
    # create an empty list to store grades
    grades = []

    # input loop
    while True:
        entry = input("Please enter one grade or -1 to stop: ")
        if entry == "-1":
            break
        # keep it simple: accept whole numbers only
        if entry.strip().isdigit():
            grades.append(int(entry))          # >>> .append(item)
        else:
            print("Please enter a whole number grade or -1.")

    # print the list of grades
    print(grades)

    # ----- remove the lowest grade -----
    print("\nRemoving lowest grade")
    if len(grades) > 0:                        # >>> len(list)
        lowest_value = min(grades)             # >>> min(list)
        lowest_index = grades.index(lowest_value)  # >>> .index(item)
        grades.pop(lowest_index)               # >>> .pop([index])
    print(grades)

    # ----- remove a random grade -----
    print("\nRemoving random grade")
    if len(grades) > 0:
        random_value = random.choice(grades)   # >>> random.choice(list)
        grades.remove(random_value)            # >>> .remove(item)
    print(grades)

    # ----- edit a grade -----
    print("\nEdit a grade")
    if len(grades) > 0:
        # list the index (starting at 1) and each grade
        for counter, item in enumerate(grades, start=1):  # >>> enumerate(list, start=1)
            print(f"{counter}. {item}")

        # ask which numbered item to edit; validate the choice
        while True:
            choice = input("Which grade do you want to edit (enter a number between 1 and " + str(len(grades)) + "): ")
            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(grades):
                    break
            print("Please enter a valid grade number.")

        # get the new grade value and update the list position
        new_value = int(input("Enter the new grade: "))
        grades[choice_num - 1] = new_value      # set by index

    print(grades)

    # ----- sort and reverse the list -----
    print("\nSorting and reversing the list")
    grades.sort()                               # >>> .sort()
    grades.reverse()                            # >>> .reverse()
    print(grades)

    # ----- total and average -----
    print("\nGetting Grade Total and Average")
    total = sum(grades)                         # >>> sum(list)
    print("Total:", total)
    if len(grades) > 0:
        average = total / len(grades)
    else:
        average = 0
    print("Average:", average)

    # assignment completion line
    print("Completed by, Kari Shaddinger")

if __name__ == "__main__":
    main()
