function makeList(n){
  var arr = [];
  for(var i = 0; i < n; i++){
    arr.push(Math.round(Math.random() * 100));
  }
  return arr;
}

function bubbleSort(arr0){
  var arr = [...arr0];
  for(var i = 0; i < arr.length; i++){
    for(var j = 0; j < arr.length; j++){
      if(arr[i] < arr[j]){
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
    }
  }
  return arr;
}

function selectionSort(arr0){
  function getSmallest(array){
    smallest = array.reduce((curr_smallest, num) =>
                  curr_smallest < num ? curr_smallest:num);
    arr.splice(arr.indexOf(smallest),1);
    return smallest;
  }
  var arr = [...arr0];
  var sortedarr = [];
  for(var i = 0; i < arr0.length; i++){
    sortedarr.push(getSmallest(arr));
  }
  return sortedarr;
}

function insertionSort(arr){
  var sortedarr = [];
  function insert(arr, element){
    var added = false;
    for(var i = 0; i < arr.length; i++){
      if(arr[i] >= element ){
        arr.splice(i, 0, element);
        added = true;
        break;
      }
    }
    if(!added){
      arr.splice(arr.length, 0, element);
    }
  }
  for(var i = 0; i < arr.length; i++){
    insert(sortedarr, arr[i]);
  }
  return sortedarr;
}

function countsort(arr){
  var counts = [];
  for(var i = 0; i < 100; i++){counts.push(0)}
  var sortedarr = [];
  for(var i = 0; i < arr.length; i++){sortedarr.push(0)}
  for(var val of arr){
    counts[val]++;
  }
  for(var i = 1; i < counts.length; i++){
    counts[i] += counts[i - 1]
  }
  for(var val of arr){
    var index = counts[val];
    counts[val]--;
    sortedarr[index - 1] = val;
  }

  return sortedarr;
}

function gnomesort(arr){
  var index = 0;
  let  reachedEnd = false;
  while(! reachedEnd ){
    if(index == 0){
      index++;
    }
    if(arr[index] >= arr[index - 1]){
      index++;
    }else{
      temp = arr[index];
      arr[index] = arr[index - 1];
      arr[index - 1] = temp;
      index--;
    }
    if(index == arr.length){
      reachedEnd = true;
    }
  }
  return arr;
}

function quicksort(arr){
  if(arr.length < 2){
    return arr;
  }
  var pivot = arr[0];
  var less = []
  var more = []
  for(var i = 1; i < arr.length;i++){
    if(arr[i] < pivot){
      less.push(arr[i])
    }else{
      more.push(arr[i])
    }
  }
  less = quicksort(less)
  more = quicksort(more)
  less.push(pivot)
  for(var v of more){
    less.push(v)
  }
  return less;
}

function mergesort(arr){
  if(arr.length < 2){
    return arr;
  } else{
    var list1 = []
    var list2 = []
    for(var i = 0; i < Math.floor(arr.length/2); i++){
      list1.push(arr[i]);
    }
    for(var i = Math.floor(arr.length / 2); i < arr.length; i++){
      list2.push(arr[i]);
    }
    list1 = mergesort(list1)
    list2 =  mergesort(list2)
    var result = []
    while(list1.length && list2.length){
      if(list1[0] < list2[0]){
        result.push(list1[0])
        list1.splice(0, 1)
      }else{
        result.push(list2[0])
        list2.splice(0, 1)
      }
    }
    for( var v of list1 ){
      result.push(v)
    }
    for( var v of list2 ){
      result.push(v)
    }
    return result;
  }
}

function treesort(arr){
  function initializeleft(node){
    if (node.left == null){
      node.left = {
        value : null,
        left  : null,
        right : null
    }}
  }
  function initializeright(node){
    if (node.right == null){
      node.right = {
        value : null,
        left  : null,
        right : null
    }}
  }
  function valueExists(node){
    return node.value != null;
  }
  function insertTree(node, val){
    if(! valueExists(node)){
      node.value = val
    }else if(node.value > val){
      initializeleft(node)
      insertTree(node.left, val)
    }else{
      initializeright(node)
      insertTree(node.right, val)
    }
  }
  function getTree(arr){
    rootnode = {
      value : null,
      left  : null,
      right : null
    }
    for(var v of arr){
      insertTree(rootnode, v)
    }
    return rootnode;
  }
  var result = []
  function traverse(node){
    //left, root, right
    if(! valueExists(node)){
      return arr
    }
    initializeleft(node);
    traverse(node.left)
    result.push(node.value)
    // console.log(node.value)
    initializeright(node);
    traverse(node.right)
    return arr
  }

  return traverse(getTree(arr), result)
}

arr = makeList(12);
console.log("bubblesort", bubbleSort(arr));
console.log("selectionSort", selectionSort(arr));
console.log("insertionSort", insertionSort(arr));
console.log("Countsort", countsort(arr));
console.log("gnomesort", gnomesort(arr));
console.log("mergesort", mergesort(arr));
console.log("quicksort", quicksort(arr));
console.log("treesort", treesort(arr));
