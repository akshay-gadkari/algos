const voters = [
    {name:'Bob' , age: 30, voted: true},
    {name:'Jake' , age: 32, voted: true},
    {name:'Kate' , age: 25, voted: false},
    {name:'Sam' , age: 20, voted: false},
    {name:'Phil' , age: 21, voted: true},
    {name:'Ed' , age:55, voted:true},
    {name:'Tami' , age: 54, voted:true},
    {name: 'Mary', age: 31, voted: false},
    {name: 'Becky', age: 43, voted: false},
    {name: 'Joey', age: 41, voted: true},
    {name: 'Jeff', age: 30, voted: true},
    {name: 'Zack', age: 19, voted: false}
];

function voterResults(voters) {
    // Your code here
    const results = {
	youngVotes: 0,
	youth: 0,
	midVotes: 0,
	mids: 0,
	oldVotes: 0,
	olds: 0
    };
    
    return voters.reduce((acc, curr) => {
	if (curr.age >= 18 && curr.age <= 25) {
            acc.youth++;
            if (curr.voted) {
		acc.youngVotes++;
            }
	} else if (curr.age >= 26 && curr.age <= 35) {
            acc.mids++;
            if (curr.voted) {
		acc.midVotes++;
            }
	} else if (curr.age >= 36 && curr.age <= 55) {
            acc.olds++;
            if (curr.voted) {
		acc.oldVotes++;
            }
	}
	console.log(acc);
	return acc;
    }, results);
    console.log(results);
}
