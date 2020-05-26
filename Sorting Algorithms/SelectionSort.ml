exception OutOfBounds;;
let rec randList n = if n=0 then [] else (Random.int 100)::(randList (n-1)) ;;
let myList = randList 15 ;;
let maxList ll = 
  if ll = [] then raise OutOfBounds else
    let rec helper  ll currmax= 
      match ll with 
      |[] -> currmax
      |x::rest -> if x > currmax then helper rest x else helper rest currmax
    in helper ll min_int 
let rec remove ll e = match ll with
  |x::rest-> if x = e then rest else x::(remove rest e)
  |[] -> raise OutOfBounds;;
let rec selectionSort ll = if ll = [] then [] else
    let m = maxList ll in
    m::(selectionSort (remove ll m)) ;;
selectionSort myList