# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.

# Constraints

# Output Format

# Print the runner-up score.

# Sample Input 0

# 5
# 2 3 6 6 5
# Sample Output 0

# 5


#######################################################################################
# Solution 1

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     ls  = list(arr)

#     ls.sort()
#     max_A  = ls[-1]
#     B      = [i for i in ls if i<max_A]
#     B.sort()
#     second = B[-1]
#     print(second)

########################################################################################
# Solution 2

if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    arr.sort(reverse=True)
    print(arr[1])