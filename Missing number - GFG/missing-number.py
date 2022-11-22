#User function Template for python3

def missingNumber( A, N):
     # Your code goes here
    #  get the total num of sum
    total_sum = (N*(N+1))/2
    current_sum = 0
    for i in A:
        current_sum += i
    missing_num = total_sum - current_sum
    return int(missing_num)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(missingNumber(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends