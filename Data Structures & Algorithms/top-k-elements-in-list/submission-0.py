class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = dict()

        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1

        sortedItems = sorted(mapping.items(), key = lambda item: item[1], reverse = True)

        answer = []

        for num, freq in sortedItems[:k]:
            answer.append(num)

        return answer