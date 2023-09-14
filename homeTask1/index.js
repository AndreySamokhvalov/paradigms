// императивный подход

const arr = [-9,12,4,0,7,-1,1]
function imperativeSort(arr) {
    for (let j = arr.length - 1; j > 0; j--) {
        for (let i = 0; i < j; i++) {
            if (arr[i] < arr[i + 1]) {
            let temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
            }
        }
    } return arr
}
console.log(imperativeSort(arr))


// декларативный подход 


const arr2 = [-9,12,4,0,7,-1,1]
arr2.sort((a, b) => b - a);

console.log(arr2);