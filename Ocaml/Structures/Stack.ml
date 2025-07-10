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

type 'a stackCall=
    Spop 
  |Spush of 'a
  |Speek
  |SisEmpty 
  |S;;
type 'a stackReturn = 
  |Srlist of 'a list 
  |Srelement of 'a
  |Srbool of bool
  |None
let makeStack q = let ll = ref q in 
  fun call -> match call with 
    |Spop -> let e, l = (pop !ll )in ll:= l;Srelement(e) 
    |Spush(el) -> ll:=(push !ll el);None 
    |Speek -> Srelement(peek !ll) 
    |SisEmpty -> Srbool(!ll = []) 
    |S -> Srlist(!ll);; 


let m9 = reverse_list(make_num_list 9) ;;
let mighty_nein = makeStack m9 ;;
mighty_nein S ;;
mighty_nein SisEmpty ;;
mighty_nein S ;;
mighty_nein Spop ;;
mighty_nein S ;;
mighty_nein (Spush 1) ;;
mighty_nein S ;;
mighty_nein Speek ;;
mighty_nein S ;;

let lorenzo = makeStack [];;
lorenzo SisEmpty
