class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap_s_to_t={}
        hashmap_t_to_s={}

        for i in range(len(s)):
            char1,char2=s[i],t[i]

            if (char1 in hashmap_s_to_t and hashmap_s_to_t[char1]!=char2 or
            char2 in hashmap_t_to_s and hashmap_t_to_s[char2]!=char1 ):
                return False

            hashmap_s_to_t[char1]=char2
            hashmap_t_to_s[char2]=char1

        return True

        