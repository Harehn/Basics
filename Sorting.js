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

function getSmallest(array){
  smallest = array.reduce((curr_smallest, num) =>
                curr_smallest < num ? curr_smallest:num);
  return smallest;
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

arr = makeList(12)
console.log(arr)
console.log(bubbleSort(arr));
console.log(selectionSort(arr));
console.log(arr)
console.log(insertionSort(arr));
