#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Skriptin adını saymırıq
    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        # Burada "s" hərfi yoxdur!
        print("1 argument:")
    else:
        # Burada "s" hərfi var
        print("{} arguments:".format(count))

    # Arqumentləri birdən başlayaraq sıralayırıq
    for i in range(1, count + 1):
        print("{}: {}".format(i, sys.argv[i]))
