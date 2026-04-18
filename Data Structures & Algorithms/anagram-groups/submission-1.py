class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapp = {}

        
    
        sorted_list = ["".join(sorted(word)) for word in strs]

        for i in range(len(sorted_list)):

            key = sorted_list[i]
            
            if key not in mapp:

                mapp[key] = []

            
            mapp[key].append(strs[i])

            
        return list(mapp.values())

    






