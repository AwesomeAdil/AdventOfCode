import System.IO
import Data.List
import Data.List.Split

isNum :: Char -> Bool
isNum x = x `elem` ['1'..'9']

findLeast :: String -> Char
findLeast [] = '0'
findLeast (x:xs) = if isNum x then x else findLeast xs

findMost :: String -> Char
findMost = findLeast . reverse 

lineCalc :: String -> String
lineCalc x = 
  let tens = findLeast x
      ones = findMost x
  in [tens] ++ [ones]

collectLines :: String -> [String]
collectLines = splitOn $ "\n"

main :: IO()
main = do
  input <- openFile "sample.txt" ReadMode
  raw_data <- hGetContents input
  putStrLn(show(sum(map (\x-> read x::Int) [lineCalc x| x <- collectLines raw_data])))

