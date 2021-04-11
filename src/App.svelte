<script>
	export let name;
	let todoItems = [
		{'name': 'make to-do app', 'done': true},
		{'name': 'make second item', 'done': false}
	];
	let inputText = 'New item';
	function handleClick() {
		if (inputText == 'New item') return
		todoItems = [...todoItems, {'name': inputText, 'done': false}]
	}
</script>

<main>
	<h1>Hello {name}!</h1>
	<input bind:value={inputText}>
	<button on:click={handleClick}>Add item</button>
	<ul>{#each todoItems as item}
		<li>{item.name}<input type=checkbox bind:checked={item.done}></li>
	{/each}
	</ul>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #9c5138;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>