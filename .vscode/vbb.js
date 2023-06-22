// Select all elements with the 'animate' class and add the 'animate' class to them
const animateElements = document.querySelectorAll('.animate');
animateElements.forEach(element => element.classList.add('animate'));

// Add a 'shake' class to each section element when it's hovered over
const sectionElements = document.querySelectorAll('section');
sectionElements.forEach(section => {
	section.addEventListener('mouseover', () => {
		section.classList.add('shake');
	});

	section.addEventListener('mouseout', () => {
		section.classList.remove('shake');
	});
});
