-- input parsing
collectLines :: String -> [String]
collectLines = splitOn $ "\n"

-- main
main :: IO()
main = do
  input <- openFile "sample.txt" ReadMode
  raw_data <- hGetContents input
  IDs <- [0..]


