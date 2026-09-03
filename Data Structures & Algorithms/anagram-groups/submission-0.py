class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            anagram="".join(sorted(i))
            if anagram in dict :
                dict[anagram].append(i)
            else :
                dict[anagram]=[i]
        result=[]
        for i in dict:
            result.append(dict[i])
        return result
            
        