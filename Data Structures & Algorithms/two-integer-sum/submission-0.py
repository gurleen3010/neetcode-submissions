class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {} 

        # Dictionary in Python:
        
        # Declaration w/o values: dictionary = dict()
        # Declaration with values: dictionary = {"name":"Gurleen", "age":24}
        # Add values: dictionary["a"] = 1
        # Update values: dictionary["a"] = 5
        # Access values: print(dictionary["a"])
        # Check if value is present:
        #   if dictionary["a"]: --> error if a is not present
        #   check: if "a" in dictionary
        # Get: freq["a"] = freq.get("a", 0) + 1
        # Iterate keys: for key in freq: print(key)
        # Iterate over values: for value in freq.values() : print(value)
        # Access both key, value: for key, value in freq.items(): print(key, value)
        # Remove key: del freq["a"] or freq.pop("a")
        # No. of keys: len(freq)
        # Remove all entries: freq.clear()

        for idx, value in enumerate(nums):
            dictionary[value] = idx

        ans = [0] * 2;

        for idx, value in enumerate(nums):
            if (target-value) in dictionary and dictionary[target - value] != idx:
                ans[0] = idx
                ans[1] = dictionary[target - value]
                return ans

        return ans