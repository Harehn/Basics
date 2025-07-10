exception OutOfBounds;;
let sortedList = [14; 21; 24; 29; 30; 31; 39; 54; 67; 68; 76; 81; 83; 89; 97]
let rec randList n = if n=0 then [] else (Random.int 100)::(randList (n-1)) ;; 
let myList = randList 15 ;; 

type 'a tree = Empty | Node of 'a tree * 'a * 'a tree ;;
let rec insert t element = 
  match t with
  |Empty -> Node(Empty, element, Empty)
  |Node(left, x, right) -> 
      if x < element 
      then Node(insert left element, x, right)
      else Node(left, x, insert right element);;
let listtotree ll = 
  let rec helper ll t=
    match ll with
    |[] -> t
    |x::xs -> helper xs (insert t x)
  in
  helper ll Empty;; 
let rec flatten t = match t with 
  |Empty -> []
  |Node(left, x, right) -> ((flatten left)@ (x::(flatten right))) ;;

let binarySort ll = flatten (listtotree ll);;