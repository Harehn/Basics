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
    sortedarr[index] = val;
  }

  return sortedarr;
}

function mergesort(arr){
  function breakarr(arr){
    return [arr.slice(0, arr.length/2), arr.slice(arr.length/2, arr.length)];
  }
  function join(arr1, arr2){
    if(arr1.length == 0){
      return arr2;
    }
    if(arr2.length == 0){
      return arr1;
    }
    if(arr1[0] < arr2[0]){
      return [arr1[0], ...(join(arr1.slice(1, arr1.length), arr2))];
    }else{
      return [arr2[0], ...(join(arr1, arr2.slice(1, arr2.length)))];
    }
  }
  if(arr.length < 2){
    return arr;
  } else{
    [list1, list2] = breakarr(arr);
    console.log(list1, list2);
    return join(mergesort(list1), (list2));
  }


}

arr = makeList(12);
arr2 = makeList(12);
// console.log("bubblesort", bubbleSort(arr));
// console.log("selectionSort", selectionSort(arr));
// console.log("insertionSort", insertionSort(arr));
console.log("Countsort", countsort(arr));
console.log("mergesort", mergesort(arr));
// console.log("Original array", arr);
// console.log("Second array", arr2);
// console.log("Joined", join(arr, arr2))
// console.log("Breaking arr", breakarr(arr));
// console.log("Original array", arr);
