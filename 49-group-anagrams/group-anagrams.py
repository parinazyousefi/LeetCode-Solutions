# input= list of strings
# out= list of lists which each list contains anagrams
# operations:
# anagram: the frequency of the alphabet used in the words are the same
# map=[0] * 26 zeros ==> a-z index=0==>a ,index=1 ==>b
# we go through eachs string and we creat a map of the word on the array so for example for word :"eat" : the value for index 4,1,19 are going to be 1.
# ****the anagrams all have the same pattern/map***
# the list which describes each word is going to be the key in a hashmap and its value is going to be a list of the word it maps to
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            char_freq_array = [0] * 26

            for char in string:
                char_freq_array[ord(char) - ord("a")] += 1

            # using tuple ds as a key in dict because it is immutable(can't be changed)
            result[tuple(char_freq_array)].append(string)

        return result.values()
