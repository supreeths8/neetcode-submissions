class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        running_sum = 0
        num_subarrays = 0

        for r in range(len(arr)):
            running_sum += arr[r]

            if r - l + 1 == k:
                avg = running_sum / k
                if avg >= threshold:
                    num_subarrays += 1
                
                running_sum -= arr[l]
                l += 1
        
        return num_subarrays