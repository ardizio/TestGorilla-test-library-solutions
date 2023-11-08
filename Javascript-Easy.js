export function find_total( my_numbers ) {
	//Insert your code here 
	let count = 0;
	for(let num of my_numbers){
		if(num%2 == 0){
			//add one if even
			count += 1;
		}
		else{
			if(num!=5){
				// if odd not 5
				count += 3;
			}
			else{
				// if 5
				count += 5;
			}
		}
		console.log(`c:${count} - n:${num}`)
	}
	return count;
}
