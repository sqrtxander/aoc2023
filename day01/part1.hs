import System.IO
import Data.List
import Data.Char

getNums :: String -> [Integer]
getNums "" = []
getNums (x:xs)
    | isDigit x = (toInteger . digitToInt) x:getNums xs
    | otherwise = getNums xs

getFirst :: [Integer] -> Integer
getFirst [] = 0
getFirst (x:xs) = x

getLast :: [Integer] -> Integer
getLast [] = 0
getLast [x] = x
getLast (x:xs) = getLast(xs)

sumFirstLast :: [Integer] -> Integer
sumFirstLast list = 10 * getFirst list + getLast list

main = do
    input <- readFile "input.in"
    let ls = lines input
    print $ sum $ map (sumFirstLast . getNums) ls

