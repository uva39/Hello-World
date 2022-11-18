quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = left ++ [x] ++ right
  where
    left = quicksort [a | a <- xs, a <= x]
    right = quicksort [a | a <- xs, a > x]
-- in-place가 아닌 퀵소트 구현
-- quicksort [] = [] 은 pattern-matching

factorial n = product [1..n]
palindrome xs = reverse xs == xs

abs n = if n >= 0 then n else -n
perceptron n
  | n > 0 = 1
  | n < 0 = -1
  | otherwise = 0

minus = \x -> \y -> x - y

length' xs = sum [1 | _ <- xs]

-- 369게임
check :: Int -> Int
check x = sum [1 | c <- show x, c `elem` "369"]
game n = [if check x > 0 then -(check x) else x | x <- [1..n]]

-- Transform uppercase <-> lowercase
toUpper :: Char -> Char
toUpper c = toEnum (fromEnum c + fromEnum 'A' - fromEnum 'a')
toLower :: Char -> Char
toLower c = toEnum (fromEnum c + fromEnum 'a' - fromEnum 'A')
change :: String -> String
change [] = []
change (x:xs) = if x `elem` ['a'..'z'] then (toUpper x) : change xs
                          else if x `elem` ['A'..'Z'] then (toLower x) : change xs
                          else x : change xs

-- arr = [x | x <- randomRs (1, 100), x < 50]

isTriangle :: Int -> Int -> Int -> Bool
isTriangle a b c = a + b > c && a + c > b && b + c > a
isRight :: Int -> Int -> Int -> Bool
isRight a b c = (a^2 + b^2 == c^2 || a^2 + c^2 == b^2 || b^2 + c^2 == a^2) && (isTriangle a b c)

eras :: Int -> [Int]
eras n = [x | x <- [2..n], all (\y -> x `mod` y /= 0) [2..(x-1)]]

pairs :: [a] -> [(a, a)]
pairs xs = xs `zip` (tail xs)

isSorted :: Ord a => [a] -> Bool
isSorted xs = and [x <= y | (x, y) <- pairs xs]

positions :: Eq a => a -> [a] -> [Int]
positions x xs = 
  [i | (x', i) <- xs `zip` [0..n], x == x']
  where n = (length xs) - 1

-- positions 0 [0, 1, 0, 1, 1, 1, 1, 0]
-- [0,2,7] 