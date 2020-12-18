if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    array = list(arr)
    array.sort(reverse=True)
    print(array)
    for i in range (n-1):
        if array[i+1] < array[i] :
            secondLar = array[i+1]
            print (secondLar)
            break
    