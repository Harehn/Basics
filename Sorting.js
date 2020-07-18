function makeList(n){
  var arr = [];
  for(var i = 0; i < n; i++){
    arr.push(Math.round(Math.random() * 100));
  }
  return arr;
}

function bubbleSort(arr0){
  var arr = [...arr0]
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

arr = makeList(12)
console.log(arr)
console.log(bubbleSort(arr));
