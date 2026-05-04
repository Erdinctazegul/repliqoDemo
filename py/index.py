def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid
        elif target > data[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def input_lst():
    numbers = []
    total = int(input("Enter number of elements: "))

    print("Enter elements:")
    for _ in range(total):
        value = int(input())
        numbers.append(value)

    return numbers


def display_lst(data):
    if not data:
        print("List is empty")
    else:
        print("Current List:", data)


def linear_menu(data):
    while True:
        print("\n--- Linear Search Menu ---")
        print("1. Enter elements into the list")
        print("2. Display the list")
        print("3. Search for a value")
        print("4. Go back")

        option = input("Enter your choice: ")

        if option == "1":
            data = input_lst()

        elif option == "2":
            display_lst(data)

        elif option == "3":
            if not data:
                print("List is empty")
            else:
                key = int(input("Enter value to search: "))
                position = linear_search(data, key)

                if position == -1:
                    print("Value not found")
                else:
                    print("Value found at index:", position)

        elif option == "4":
            print("Returning to main menu...")
            return data

        else:
            print("Invalid choice")


def binary_menu(data):
    while True:
        print("\n--- Binary Search Menu ---")
        print("1. Enter elements into the list")
        print("2. Display the list")
        print("3. Search for a value")
        print("4. Go back")

        option = input("Enter your choice: ")

        if option == "1":
            data = input_lst()

        elif option == "2":
            display_lst(data)

        elif option == "3":
            if not data:
                print("List is empty")
            else:
                key = int(input("Enter value to search: "))
                ordered = sorted(data)

                print("Sorted List:", ordered)

                position = binary_search(ordered, key)

                if position == -1:
                    print("Value not found")
                else:
                    print("Value found at index:", position)

        elif option == "4":
            print("Returning to main menu...")
            return data

        else:
            print("Invalid choice")


def main():
    current_lst = []

    while True:
        print("\nSelect Search Method:")
        print("1. Linear Search")
        print("2. Binary Search")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            current_lst = linear_menu(current_lst)

        elif choice == "2":
            current_lst = binary_menu(current_lst)

        elif choice == "0":
            print("Program exited.")
            break

        else:
            print("Invalid choice")


main()