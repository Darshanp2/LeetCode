"""

733. Flood Fill

"""

def floodFill(image, sr, sc, color):
    R = len(image)
    C = len(image[0])
    existingColor = image[sr][sc]
    if existingColor == color:
        return image
    
    def dfs(r, c):

        if image[r][c] == existingColor:
            image[r][c] = color
            if r >= 1:
                dfs(r-1, c)
            if r+1 < R:
                dfs(r+1, c)
            if c >=1 :
                dfs(r, c-1)
            if c+1 < C:
                dfs(r, c+1)

    dfs(sr, sc)
    return image
