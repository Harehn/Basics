exception OutOfBounds;;
let sortedList = [14; 21; 24; 29; 30; 31; 39; 54; 67; 68; 76; 81; 83; 89; 97]
let rec randList n = if n=0 then [] else (Random.int 100)::(randList (n-1)) ;;
let myList = randList 15 ;;
let bubble ll = 
  let rec helper ll b=
    match  ll with
    |[] -> [], false
    |[x] -> [x], false
    |x::y::rest -> let l, m, bb = if x <= y then x, y, false else y, x, true
        in
        match (helper (m::rest) bb) with
        |lll, bs -> l::lll, bs||bb
  in helper ll false
let rec bubbleSort ll = match (bubble ll) with
  | l, b -> if b then bubbleSort l else l ;;
bubbleSort myList ;;