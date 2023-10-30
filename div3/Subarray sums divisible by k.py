class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        count = {0: 1}  # Initialize with one 0 sum (mod k) subarray
        cumulative_sum = 0
        result = 0

        for num in nums:
            cumulative_sum += num
            modulus = cumulative_sum % k

            if modulus in count:
                result += count[modulus]
                count[modulus] += 1
            else:
                count[modulus] = 1

        return result

# we use prefix sum
