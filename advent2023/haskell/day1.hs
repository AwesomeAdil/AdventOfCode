import System.IO
import Data.List
import Data.List.Split
nums = [1..9]

-- to determine if word exists
getNum:: String->Char
getNum "one" = '1'
getNum "two" = '2'
getNum "three" = '3'
getNum "four" = '4'
getNum "five" = '5'
getNum "six" = '6'
getNum "seven" = '7'
getNum "eight" = '8'
getNum "nine" = '9'
getNum _ = '0'

fixPart :: Int->String->String
fixPart x y =  reverse (take x (reverse y))

checkIfWord :: (Int -> String -> String) -> String -> Char
checkIfWord f x
  | one `elem` ['1'..'9'] = one
  | trip /= '0' = trip
  | quat /= '0' = quat
  | quin /= '0' = quin
  | otherwise = '0'
  where one = (head . (f 1)) x
        trip = (getNum . (f 3)) x
        quat = (getNum . (f 4)) x
        quin = (getNum . (f 5)) x

isWordNumForward :: String -> Char
isWordNumForward x
  | x == [] = '0'
  | result /= '0' = result
  | otherwise = isWordNumForward rest
  where rest = tail x
        result = checkIfWord (take) x

isWordNumBackWord :: String -> Char
isWordNumBackWord x 
  | x == [] = '0'
  | result /= '0' = result
  | otherwise = isWordNumBackWord rest
  where rest = init x
        result = checkIfWord (fixPart) x 

isNum :: Char -> Bool
isNum x = x `elem` ['1'..'9']

findLeast :: String -> Char
findLeast [] = '0'
findLeast (x:xs) = if isNum x then x else findLeast xs

findMost :: String -> Char
findMost = findLeast . reverse 

-- day1 method
lineCalc :: String -> String
lineCalc x = 
  let tens = findLeast x
      ones = findMost x
  in [tens] ++ [ones]

-- day2 method
lineCalc_1 :: String -> String
lineCalc_1 x = 
  let tens = isWordNumForward x
      ones = isWordNumBackWord x
  in [tens] ++ [ones]

-- input parsing
collectLines :: String -> [String]
collectLines = splitOn $ "\n"

main :: IO()
main = do
  input <- openFile "sample.txt" ReadMode
  raw_data <- hGetContents input
  putStrLn(show(sum(map (\x-> read x::Int) [lineCalc_1 x| x <- collectLines raw_data])))

