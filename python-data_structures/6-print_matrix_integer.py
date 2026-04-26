#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Matrisi rəqəmlər arasında boşluq olmaqla çap edir."""
    for row in matrix:
        for i in range(len(row)):
            # Əgər bu, sətrin sonuncu elementi deyilsə, boşluqla çap et
            if i < len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                # Sonuncu elementdən sonra boşluq qoyma
                print("{:d}".format(row[i]), end="")
        # Bir sətir tam bitdikdən sonra yeni sətirə keç
        print()
