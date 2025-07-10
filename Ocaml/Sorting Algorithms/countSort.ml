exception OutOfBounds;;
let sortedList = [14; 21; 24; 29; 30; 31; 39; 54; 67; 68; 76; 81; 83; 89; 97]
let rec randList n = if n=0 then [] else (Random.int 100)::(randList (n-1)) ;; 
let myList = randList 15 ;; 
let rec size ll = match  ll with 
  |[] -> 0
  |x :: rest-> 1 + size rest ;;
let rec get ll i = match ll, i with
  |x::_, 0 -> x
  |_::rest, _-> get rest (i-1)
  |_ -> raise OutOfBounds;; 
let rec set ll i e = match ll, i with
  |_::rest, 0 -> e::rest
  |x::rest, _-> x::(set rest (i-1) e)
  |_ -> raise OutOfBounds;;
let rec createzeros n = if n=0 then [] else 0::(createzeros (n-1)) ;;
let rec update ll n =
  match ll with
  |x::xs -> if n = 0 then (x+1)::xs else x::(update xs (n-1)) 
  |[] -> raise OutOfBounds;;
let rec decrement ll n =
  match ll with
  |x::xs -> if n = 0 then (x-1)::xs else x::(decrement xs (n-1)) 
  |[] -> raise OutOfBounds;;
let enumerate ll = 
  let rec helper ll n =
    match ll with
    |[] -> raise OutOfBounds
    |[x] -> [(x, n)]
    |x::xs-> (x, n)::(helper xs (n+1))
  in helper ll 0;;
let rec updateList indices ll = 
  match ll with
  |[] -> indices
  |x::xs -> updateList (update indices x) xs;;
let rec modifyCountList ll=
  match ll with
  |[] -> []
  |[x] -> [x]
  |x::y::rest -> x::(modifyCountList ((x+y)::rest));;
let countSort ll = 
  let newlist = createzeros (size ll) in
  let indices = modifyCountList (updateList (createzeros 100) ll) in
  let rec helper l currlist ind=
    match l with
    |[] -> currlist
    |x::rest -> helper rest (set currlist ((get ind x)-1) x) (decrement ind x)
  in helper ll newlist indices;;