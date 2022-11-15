f [] = []
f (x:xs) = f ys ++ [x] ++ zs -- 퀵소트 잘못된 구현임
          where
            ys = [a | a <- xs, a <= x]
            zs = [b | b <- xs, b > x]

factorial n = product [1..n]