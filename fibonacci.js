let n = 5;
function fibonacci(n) {
    if (n == 1) {
	console.log([0]);
	return [0];
    }
    if (n == 2){
	console.log([1]);
	return [0, 1];	
    }
    let sequence = [0, 1]
    let i = 0;
    for (i; i < n; i++){
	sum = sequence[sequence.length - 1] + sequence[sequence.length - 2]
	console.log(i+1, sum);
	sequence.push(sum);
    }
    console.log(sequence);
    return sequence.slice(0, n);
}
fibonacci(n)
