quicksort :: [Int] -> [Int]
quicksort [] = []
quicksort (x:xs) = left ++ [x] ++ right
  where
    left = quicksort [a | a <- xs, a <= x]
    right = quicksort [a | a <- xs, a > x]
-- in-place가 아닌 퀵소트 구현
-- quicksort [] = [] 은 pattern-matching

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

eras :: Int -> [Int]
eras n = [x | x <- [2..n], all (\y -> x `mod` y /= 0) [2..(x-1)]]

positions :: Eq a => a -> [a] -> [Int]
positions x xs = 
  [i | (x', i) <- xs `zip` [0..n], x == x']
  where n = (length xs) - 1
-- positions 0 [0, 1, 0, 1, 1, 1, 1, 0]
-- [0,2,7] 

-- using accumlator
fac n = aux n 1
  where
    aux n acc
      | n <= 1 = acc
      | otherwise = aux (n-1) (n*acc)

-- important
myelem :: Eq a => a -> [a] -> Bool
myelem _ [] = False
myelem e (x:xs) = (e == x) || (myelem e xs)

-- removes duplicate
mynub :: Eq a => [a] -> [a]
mynub xs = aux xs []
  where
    -- important
    aux [] b = b
    aux (x:xs) ys
      | x `myelem` ys = aux xs ys
      | otherwise = aux xs (ys ++ [x])

isAscending :: Ord a => [a] -> Bool
isAscending xs = and [x <= y | (x, y) <- pairs xs]
  where
    -- important
    pairs :: [a] -> [(a, a)]
    pairs [] = []
    pairs ys = ys `zip` (tail ys)

-- same, but better

isAscending' :: Ord a => [a] -> Bool
isAscending' [] = True
isAscending' [x] = True
isAscending' (x:y:xs) = (x <= y) && isAscending' (y:xs)


hasPath :: [(Int, Int)] -> Int -> Int -> Bool
hasPath [] x y = x == y
hasPath xs x y
  | x == y = True
  | otherwise =
    let xs' = [(start, end) | (start, end) <- xs, start /= x] -- xs' = different starting node
      in or [hasPath xs' end y | (start, end) <- xs, start == x] -- xs = same starting node

test :: [(Int, Int)]
test = [(1, 2), (2, 3), (3, 4), (4, 2)]

-- A tail recursion based approach to the exercise 4:
-- 매우 중요한 풀이임. 완벽 이해

hasPath' :: [(Int, Int)] -> Int -> Int -> Bool
hasPath' graph start finish = dfs [] [start]
  where
    dfs _ [] = False
    dfs marked (x:stack) = (x == finish) || dfs (x:marked) (neighbors marked x ++ stack)
    neighbors marked x = [fin | (st, fin) <- graph, st == x && not (fin `elem` marked)]
    -- neighbors = same start, not visited fin
    -- (x == finish) -> 하나라도 finish인지 check (어차피 neighbors에서 start는 check 됨)

-- list comprehenison 대신에 filter (\x y -> x /= y) 를 사용할 수도 있다 

-- (.) :: (b -> c) -> (a -> b) -> a -> c
-- (.) f g = f . g = (\x -> f g x)
-- . (합성함수 연산자 == 합성함수를 만드는 In-Fix Functor)의 정의
-- ex) ascendingSort를 descendingSort로 만들기 : (reverse . ascendingSort)
descSort1 = reverse . quicksort
descSort2 = minus . quicksort . minus
  where
    minus :: [Int] -> [Int]
    minus xs = map (\x -> 0 - x) xs
-- ex2) 다른 방법: ((-) . ascendingSort . ())

map2D :: (a -> b) -> [[a]] -> [[b]]
map2D = map . map
map2D' f xs = map (\ys -> map f ys) xs
-- 즉, map (row에 map을 해주는 람다함수) xs
-- mapnD도 같은 방식으로 만들 수 있음.
-- 이거 쓰면 행렬에 map 간단하게 할 수 있을듯?