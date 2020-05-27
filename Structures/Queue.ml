exception OutOfBounds;;
let rec make_num_list n = if n = 0 then [] else n :: (make_num_list (n -1)) ;;
let rec reverse_list ll = match ll with 
  |[] -> [] 
  |x::rest -> (reverse_list rest)@[x] ;; 
let enqueue ll el= ll@[el] ;;
let dequeue ll = match ll with
  |[] -> raise OutOfBounds
  |x::rest -> x,rest 
type 'a queueCall=
    Qdequeue 
  |Qenqueue of 'a
  |QisEmpty 
  |Q;;
type 'a queueReturn = 
  |Qrlist of 'a list 
  |Qrelement of 'a
  |Qrbool of bool
  |None
let makeQueue q = let ll = ref q in 
  fun call -> match call with 
    |Qdequeue -> let e, l = (dequeue !ll )in ll:= l;Qrelement(e) 
    |Qenqueue(el) -> ll:=(enqueue !ll el);None 
    |QisEmpty -> Qrbool(!ll = []) 
    |Q -> Qrlist(!ll);; 


let m9 = reverse_list(make_num_list 9) ;;
let mighty_nein = makeQueue m9 ;;
mighty_nein Q ;;
mighty_nein QisEmpty ;;
mighty_nein Q ;;
mighty_nein Qdequeue ;;
mighty_nein Q ;;
mighty_nein (Qenqueue 1) ;;
mighty_nein Q ;; 

let lorenzo = makeQueue [];;
lorenzo QisEmpty