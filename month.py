#!/usr/bin/env python3

# Created by: Evano Fotia
# Created on: Oct 2019
# this program makes an integer from any mouth of the year


def main():
    # this shows the right month number
    while True:
        # input
        month = int(input("Enter month here!: "))

    # process and output
        print("your month is")
        if month == 1:
            print("January")
            break
        elif month == 2:
            print("February")
            break
        elif month == 3:
            print("March")
            break
        elif month == 4:
            print("April")
            break
        elif month == 5:
            print("May")
            break
        elif month == 6:
            print("June")
            break
        elif month == 7:
            print("July")
            break
        elif month == 8:
            print("August")
            break
        elif month == 9:
            print("September")
            break
        elif month == 10:
            print("October")
            break
        elif month == 11:
            print("November")
            break
        elif month == 12:
            print("December")
            break
        else:
            print("Error try again!")


if __name__ == "__main__":
    main()
