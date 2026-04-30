from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        dict_t = Counter(t)
        required = len(dict_t)
        left, right = 0, 0
        formed = 0
        window_counts = {}
        min_len = float('inf')
        min_window = (0, 0)
        
        while right < len(s):
            c = s[right]
            window_counts[c] = window_counts.get(c, 0) + 1
            
            if c in dict_t and window_counts[c] == dict_t[c]:
                formed += 1
            
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = (left, right)
                
                # shrink window
                c2 = s[left]
                window_counts[c2] -= 1
                if c2 in dict_t and window_counts[c2] < dict_t[c2]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        l, r = min_window
        return s[l:r+1] if min_len != float('inf') else ""