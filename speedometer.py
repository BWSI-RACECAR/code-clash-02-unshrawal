class Solution:
    def two_numbers(self, ary, target):
        # type ary: list
        # type target: int
        # return type: list or bool

       # TODO: Write code below to return a list with the solution to the prompt
        for i in range(0, len(ary)):
            for j in range(0, len(ary)):
                if i == j:
                    continue
                if(ary[i] + ary[j] == target):
                    return [i, j]
        return False
        pass

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])
    target = int(input())

    tc1 = Solution()
    ans = tc1.two_numbers(array, target)
    print(ans)

if __name__ == "__main__":
    main()