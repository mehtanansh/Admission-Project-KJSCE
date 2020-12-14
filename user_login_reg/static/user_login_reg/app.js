var example1 = document.getElementById('example1'),
	example2Left = document.getElementById('example2-left'),
	example2Right = document.getElementById('example2-right');

// Example 1 - Simple list
new Sortable(example1, {
	animation: 150,
	ghostClass: 'blue-background-class'
});


// Example 2 - Shared lists
new Sortable(example2Left, {
	group: 'shared', // set both lists to same group
	animation: 150
});

new Sortable(example2Right, {
	group: 'shared',
	animation: 150
});
