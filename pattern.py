# n = 5

# for i in range(1, n + 1):
#     print("*" * i)


# n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

n = int(input("Enter the number of rows: "))

# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)
for i in range(n):
    print(" " * (n-i), end ="")
    val =1
    for j in range(i+1):
        print(f"{ val}", end ="")
        val =  val *(i - j)//(j+1)

    print()