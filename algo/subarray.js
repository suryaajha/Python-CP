const printSubarray = (array, startIndex, endIndex) => {
	if(endIndex >= array.length)
		return console.log('Boundaries are not good');
	let output = '';
	for(let i = startIndex; i <= endIndex; i++ )
		output += array[i] + ' ';
	console.log(output);
}

const printAllSubarrays1 = (array, k) => {
	let runningSum = 0;
	let total = 0 ;
	for(let i = 0; i < array.length ; i++ ){
		runningSum = 0;
		for(let j = i ; j < array.length ; j++ ){
			runningSum += array[j];
			total += runningSum;
		}
	}
	console.log(total);
}

const printAllSubarrays = (array, k) => {
	let runningSum = 0;
	let prefixSumEnds = { 0 : [-1, 2] }
	for(let i = 0; i < array.length ; i++ ){
		runningSum += array[i];
		if(prefixSumEnds[runningSum - k]){
			prefixSumEnds[runningSum - k].forEach(endIndex => printSubarray(array, endIndex + 1, i));
		}
	}
}

const main = () => {
	let array = [2,3,4,3];
	let k = 4;

	printAllSubarrays1(array, k);
}

main();