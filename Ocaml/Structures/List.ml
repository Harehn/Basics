exception OutOfBounds;;
let rec make_num_list n = if n = 0 then [] else n :: (make_num_list (n -1)) ;;
let rec reverse_list ll = match ll with 
  |[] -> [] 
  |x::rest -> (reverse_list rest)@[x] ;; 
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
let rec add ll i e = match ll, i with
  |ll, 0 -> e::ll
  |x::rest, _-> x::(add rest (i-1) e)
  |_ -> raise OutOfBounds;;
let rec removei ll i = match ll, i with
  |x::rest, 0 -> rest
  |x::rest, _-> x::(removei rest (i-1))
  |_ -> raise OutOfBounds;;
let rec removee ll e = match ll with
  |x::rest-> if x = e then rest else x::(removee rest e)
  |[] -> raise OutOfBounds;;
let clear ll = [] ;;
type 'a listCall=
  Lget of int
  |Lset of (int * 'a)
  |Ladd of (int * 'a)
  |Lremovei of int
  |Lremovee of 'a
  |Lclear
  |LisEmpty
  |Lsize 
  |L;;
type 'a listReturn = 
  |Lrlist of 'a list
  |Lrint of int
  |Lrbool of bool
  |Lrelement of 'a
  |None ;;
let makeList a = let ll = ref a in
  fun call -> match call with
  |Lget(i) -> Lrelement(get  !ll i)
  |Lset(i, e) -> ll := set !ll i e; None
  |Ladd(i, e) -> ll := add !ll i e; None
  |Lremovei(i) -> ll := removei !ll i; None
  |Lremovee(e) -> ll := removee !ll e; None
  |Lclear -> ll := []; None
  |LisEmpty -> Lrbool(!ll = [])
  |Lsize -> Lrint(size !ll)
  |L -> Lrlist(!ll)

let m9 = reverse_list(make_num_list 9) ;;
let mighty_nein = makeList m9 ;;
mighty_nein L ;;
mighty_nein LisEmpty ;;
mighty_nein Lsize ;;
mighty_nein (Lget 6) ;;
mighty_nein (Lset (6,12)) ;;
mighty_nein L ;;
mighty_nein (Ladd (6,7)) ;;
mighty_nein L ;;
mighty_nein (Lremovei 7) ;;
mighty_nein L;;
mighty_nein (Lremovee 8) ;;
mighty_nein L;;
mighty_nein Lclear;;
mighty_nein L;;
