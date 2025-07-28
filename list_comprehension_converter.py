#simple list creation

def Main():
    even_simple_list = []
    for i in range(10):
        if i % 2 == 0:  # Example condition to filter even numbers
            even_simple_list.append(i)
    # Using list comprehension to create the same list
    even_comprehension_list = [ i for i in range(10) if i % 2 == 0]

    matrix = [(x,y) for x in range(3) for y in range(3)]

    print(matrix, even_simple_list, even_comprehension_list)

if __name__ == "__main__":
    Main() 