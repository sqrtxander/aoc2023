import System.IO
import Data.List
import Data.Char

getNums :: String -> [Integer]
getNums "" = []
getNums (x:xs)
    | isDigit x = (toInteger . digitToInt) x:getNums xs
    | otherwise = getNums xs

sumFirst :: [Integer] -> Integer
sumFirst [] = 0
sumFirst (x:xs) = x

sumLast :: [Integer] -> Integer
sumLast [] = 0
sumLast [x] = x
sumLast (x:xs) = sumLast(xs)

sumFirstLast :: [Integer] -> Integer
sumFirstLast list = 10 * sumFirst list + sumLast list

main = do
    input <- readFile "input.in"
    let ls = lines input
    print $ sum $ map (sumFirstLast . getNums) ls

