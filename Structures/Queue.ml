exception OutOfBounds;;
let rec make_num_list n = if n = 0 then [] else n :: (make_num_list (n -1)) ;;
let rec reverse_list ll = match ll with 
  |[] -> [] 
  |x::rest -> (reverse_list rest)@[x] ;; 
let push ll el= el::ll ;;
let pop ll = match ll with
  |[] -> raise OutOfBounds
  |x::rest -> x,rest
let peek ll = match ll with
  |[] -> raise OutOfBounds
  |x::_ -> x;;

type 'a queueCall=
    Qpop 
  |Qpush of 'a
  |Qpeek
  |QisEmpty 
  |Q;;
type 'a queueReturn = 
  |Qrlist of 'a list 
  |Qrelement of 'a
  |Qrbool of bool
  |None
let makeQueue q = let ll = ref q in 
  fun call -> match call with 
    |Qpop -> let e, l = (pop !ll )in ll:= l;Qrelement(e) 
    |Qpush(el) -> ll:=(push !ll el);None 
    |Qpeek -> Qrelement(peek !ll) 
    |QisEmpty -> Qrbool(!ll = []) 
    |Q -> Qrlist(!ll);; 


let m9 = reverse_list(make_num_list 9) ;;
let mighty_nein = makeQueue m9 ;;
mighty_nein Q ;;
mighty_nein QisEmpty ;;
mighty_nein Q ;;
mighty_nein Qpop ;;
mighty_nein Q ;;
mighty_nein (Qpush 1) ;;
mighty_nein Q ;;
mighty_nein Qpeek ;;
mighty_nein Q ;;

let lorenzo = makeQueue [];;
lorenzo QisEmpty