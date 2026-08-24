class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        # Count whites in the first window
        white = blocks[:k].count('W')
        ans = white

        # Slide the window
        for i in range(k, len(blocks)):
            
            # Add the new character
            if blocks[i] == 'W':
                white += 1
            
            # Remove the character leaving the window
            if blocks[i - k] == 'W':
                white -= 1
            
            ans = min(ans, white)

        return ans