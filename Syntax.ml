(*
* This is a comment.
*)
let arithmetic = (1 * 2) + (6 / 3) -1 ;;
let arithmetic2 = (1.0 *. 2.0) +. (6.0 /. 3.0) -. 1.0 ;;
let variables = [("int", 2), ("float", 2.0), ("char", 'c'), ("String", "Hello world")] ;;
let f vars = vars (* function *) ;;
f arithmetic ;;
let rec rev_loop n = match n with 
  |1 -> [1] 
  |x -> x:: rev_loop (n - 1) ;; 
rev_loop 10;;
let rec rev  ll = match ll with 
  |[] -> [] 
  |x::rest -> (rev rest) @ [x] ;;
let loop n = rev(rev_loop n) ;;
let greater n = if n > 10 then "greater" else "less" ;; (*if else*)
let obj_maker () = let a = ref 1 in 
  fun n ->
    a := !a + n ;!a;;
let obj = let ab = ref 1 in 
  fun n ->
    ab := !ab + n ;!ab;;
let obj2 = obj_maker ();;
obj 2;;

Printf.printf "Hello world" ;;

type 'a tree = Empty | Node of 'a tree * 'a * 'a tree;;
let rec mapTree(f, (t: 'a tree)) =
  match t with
  | Empty -> Empty
  | Node(l,v,r) -> Node((mapTree(f,l)), (f v), (mapTree(f, r)));;
  
let rec randList n = if n=0 then [] else (Random.int 100)::(randList (n-1)) ;;
let myList = randList 15 ;;

exception OutOfBounds;;
raise OutOfBounds;;
