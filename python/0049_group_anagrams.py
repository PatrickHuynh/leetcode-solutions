class Solution:
    def is_anagram2(self, str1, str2):
        if len(str1) != len(str2):
            return False
        a = list(str1)
        a.sort()
        b = list(str2)
        b.sort()
        return a == b
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empty_str_list = []
        anagram_dict = {}
        while len(strs) > 0:
            word = strs[-1]
            if word == "":
                empty_str_list.append(word)
                del strs[-1]
                continue
            
            sorted_word = list(word)
            sorted_word.sort()
            sorted_word = "".join(sorted_word)
            anagram_dict[sorted_word] = anagram_dict.get(sorted_word, []) + [word]
            del strs[-1]
            
        result = [v for v in anagram_dict.values()]
        if len(empty_str_list) > 0:
            result += [empty_str_list]
        return result
