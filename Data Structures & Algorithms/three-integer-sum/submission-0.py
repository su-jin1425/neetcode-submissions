class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        arr = [(nums[i], i) for i in range(len(nums))]
        target=0
        arr.sort(key=lambda x: x[0])
        answer = []
        for i in range(len(arr) - 2):
            if i > 0 and arr[i][0] == arr[i - 1][0]:
                continue

            left = i + 1
            right = len(arr) - 1
            while left < right:
                total = arr[i][0] + arr[left][0] + arr[right][0]

                if total == target:

                    values = [
                        arr[i][0],
                        arr[left][0],
                        arr[right][0]
                    ]

                    indices = [
                        arr[i][1],
                        arr[left][1],
                        arr[right][1]
                    ]

                    answer.append(values)
                    left += 1
                    right -= 1

                    while left < right and arr[left][0] == arr[left - 1][0]:
                        left += 1
                    while left < right and arr[right][0] == arr[right + 1][0]:
                        right -= 1

                elif total < target:
                    left += 1

                else:
                    right -= 1

        return answer



        