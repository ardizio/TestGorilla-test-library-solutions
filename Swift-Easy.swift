func calculateExtraCharge(_ c:Double,_ h:Double ) -> Double {

	var sum_c_h = c + h
	let kg_free = 15.0 + 7.0
	let kg_max = 45.0

    // free wight custumer can distribute
	if(sum_c_h<kg_free){
		return 0.0
	}
    // Not allowed weight
	else if (sum_c_h>kg_max){
		return -1.0
	}
    // Customer fined
	else{
		return (sum_c_h - kg_free) * 10.0
	}	
}

// max 15C and 7h
// rearange available
// if customerwight> 15+7 pay
// if customerwight> 30 + 15 return -1
// else return -1