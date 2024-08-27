class Solution(object):
    
    def __init__(self):
        self.explored = set()
        self.stack = []
    
    def floodFill(self, image, sr, sc, color):
        
        print(image)
        ogColor = image[sr][sc]
        image[sr][sc] = color 
        self.explored.add((sr,sc))
        
        if len(image[0]) > (sc + 1):
            if (sr,sc+1) not in self.explored and image[sr][sc+1] == ogColor:
                self.stack.append((sr, sc+1))
        if len(image) > sr +1:
            if (sr+1, sc) not in self.explored and image[sr+1][sc] == ogColor:
                self.stack.append((sr+1, sc))
        if sc-1 >= 0:
            if (sr,sc-1) not in self.explored and image[sr][sc-1] == ogColor:
                self.stack.append((sr, sc-1))
        if sr-1 >= 0:
            if (sr-1,sc) not in self.explored and image[sr-1][sc] == ogColor:
                self.stack.append((sr-1, sc))   

        while self.stack:
            next_sr, next_sc = self.stack.pop()
            self.floodFill(image, next_sr, next_sc, color)
        
        return image 
