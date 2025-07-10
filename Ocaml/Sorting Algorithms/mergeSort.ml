exception OutOfBounds;;
let sortedList = [14; 21; 24; 29; 30; 31; 39; 54; 67; 68; 76; 81; 83; 89; 97]
let rec randList n = if n=0 then [] else (Random.int 100)::(randList (n-1)) ;;
let myList = randList 15 ;;
let rec merge l1 l2= match l1, l2 with
  |x::xs, y::ys -> if x < y then x::(merge xs l2) else y::(merge ys l1)
  |[], _-> l2
  |_,[] -> l1
let unzip l = 
  let rec helper l1 l2 l =
    match l with
    |[] -> l1,l2
    |x::rest-> helper l2 (x::l1) rest
  in helper [] [] l;;
let rec mergeSort ll = match ll with
  |[] -> []
  |[a] -> [a] 
  |_ -> match unzip ll with
    |a,b -> merge (mergeSort a) (mergeSort b);;
mergeSort myList;;