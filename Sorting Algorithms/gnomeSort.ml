exception OutOfBounds;;
let sortedList = [14; 21; 24; 29; 30; 31; 39; 54; 67; 68; 76; 81; 83; 89; 97]
let rec randList n = if n=0 then [] else (Random.int 100)::(randList (n-1)) ;;
let rec reverse_list ll = match ll with 
  |[] -> [] 
  |x::rest -> (reverse_list rest)@[x] ;; 
let myList = randList 15 ;; 
let rec size ll = match  ll with 
  |[] -> 0
  |x :: rest-> 1 + size rest ;;
let rec swap ll n =
  match ll, n with
  |[], _ -> raise OutOfBounds
  |[x], _ -> raise OutOfBounds
  |x::y::rest, _-> if n = 1 then 
        if x <= y then (x::y::rest), false
        else (y::x::rest), true
      else let l, b = swap (y::rest) (n-1) in
        x::l, b;;
let gnomeSort ll = 
  let n = size ll in
  let rec helper currlist index =
    if index = 1 then helper currlist (index + 1)
    else if index = (n+1) then currlist
    else let l,b = swap currlist (index-1) in
      if b then helper l (index-1)
      else helper l (index + 1)
  in 
  helper ll 1;;
gnomeSort myList ;;
  (*let gnomeSort ll = 
   let rec helper sorted unsorted = 
     match sorted,unsorted with
     |_, [] -> sorted
     |[], x::xs -> helper [x] xs
     |x::xs , y::ys  -> if x <= y then helper (y::x::xs) ys else helper (y::xs) (x::ys)
   in helper [] ll;;
 gnomeSort myList;;
*)