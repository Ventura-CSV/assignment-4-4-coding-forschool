def main():

    numbers = []

    for i in range(0,5):
        value = int(input(f'Enter value {i+1}: '))
        numbers.append(value)
        
    minval = numbers[0]
    maxval = numbers[0]
    
    for num in numbers:
        if num < minval:
            minval = num
        if num > maxval:
            maxval = num
            

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
