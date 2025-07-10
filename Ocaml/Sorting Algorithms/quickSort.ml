exception OutOfBounds;;
let rec randList n = if n=0 then [] else (Random.int 100)::(randList (n-1)) ;;
let myList = randList 15 ;;
let partition ll = if ll =[] then [],[],[] else
    let p, rl = match ll with
      |[]->raise OutOfBounds
      |x::rest -> x, rest in 
    let rec helper pivot left right l =
      match l with
      |[] -> left, [pivot], right
      |x::rest -> if x < pivot then helper pivot (x::left) right rest
          else helper pivot left (x::right) rest
    in
    helper p [] [] rl;;
let join truple = match truple with
  |x, [y], z -> x @(y::z)
  |_ -> raise OutOfBounds
let rec quicksort ll = match ll with
  |[] ->[]
  |[a]->[a]
  |_ -> match partition ll with 
    |x,y,z -> join((quicksort x), y, (quicksort z));;
quicksort myList;;