f [] = []
f (x:xs) = f ys ++ [x] ++ zs
           where
             ys = [a | a <- xs, a <= x]
             zs = [b | b <- xs, b > x]