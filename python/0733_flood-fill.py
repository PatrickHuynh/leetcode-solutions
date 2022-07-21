class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        new_image = [r[:] for r in image] # deepcopy
        rowmax = len(image)
        colmax = len(image[0])
        
        def flood(oldc, newc, x):
            if new_image[x[0]][x[1]] == oldc:
                new_image[x[0]][x[1]] = newc
                px = [[x[0]-1, x[1]], [x[0]+1, x[1]], [x[0], x[1]+1], [x[0], x[1]-1]]
                for p in px:
                    if 0 <= p[0] < rowmax and 0 <= p[1] < colmax:
                        flood(oldc, newc, p)
        
        pixel_color = image[sr][sc]
        if pixel_color != color:
            flood(pixel_color, color, [sr,sc])
        
        return new_image