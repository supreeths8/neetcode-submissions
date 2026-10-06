class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        def dfs(image, r,c):
            R = len(image)
            C = len(image[0])

            if r < 0 or c < 0 or r == R or c == C:
                return image
            if image[r][c] != original_color:
                return image


            # if image[r][c] == original_color:
            image[r][c] = color

            image = dfs(image, r + 1, c)
            image = dfs(image, r, c + 1)
            image = dfs(image, r - 1, c)
            image = dfs(image, r, c - 1)


            return image
        return dfs(image, sr,sc)
        
            

