from collections import defaultdict
from heapq import *


class WordCount:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __eq__(self, other):
        return self.count == other.count

    def __lt__(self, other):
        return self.count < other.count

class Solution(object):
    def topK_frequent(self, words, k):
        result = []
        word_count = defaultdict(int)
        min_heap = []
        for word in words:
            word_count[word] += 1
        print(word_count)

        for word in word_count:
            count = word_count[word]
            heappush(min_heap, (WordCount(word, count), word))
            if len(min_heap) > k:
                heappop(min_heap)
        

        for i in range(k):
            result.append(heappop(min_heap)[1])

        return result



# Test Case
words= ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(Solution().topK_frequent(words,k))

words= ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(Solution().topK_frequent(words,k))