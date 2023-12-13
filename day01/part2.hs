import System.IO
import Data.List
import Data.Char

getNums :: String -> [Integer]
getNums "" = []
getNums (x:xs)
    | isPrefixOf "one" (x:xs) = 1:getNums xs
    | isPrefixOf "two" (x:xs) = 2:getNums xs
    | isPrefixOf "three" (x:xs) = 3:getNums xs
    | isPrefixOf "four" (x:xs) = 4:getNums xs
    | isPrefixOf "five" (x:xs) = 5:getNums xs
    | isPrefixOf "six" (x:xs) = 6:getNums xs
    | isPrefixOf "seven" (x:xs) = 7:getNums xs
    | isPrefixOf "eight" (x:xs) = 8:getNums xs
    | isPrefixOf "nine" (x:xs) = 9:getNums xs
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
    print (sum [(sumFirstLast . getNums) x | x <- ls])
