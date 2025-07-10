exception OutOfBounds;;
let rec randList n = if n=0 then [] else (Random.int 100)::(randList (n-1)) ;;
let myList = randList 15 ;;
let rec insert ll e = match ll with 
  |[] -> [e]
  |x::rest -> if x > e then x::(insert rest e) else e::x::rest 
let insertionSort ll = 
  let rec helper ll acc =
    match ll with
    |[] -> acc
    |x::rest -> helper rest (insert acc x)
  in helper ll [] ;;
insertionSort myList ;;
