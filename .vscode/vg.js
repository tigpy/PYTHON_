const searchForm = document.getElementById("search-form");
const searchInput = document.getElementById("search-input");
const searchButton = document.getElementById("search-button");
const resultsList = document.getElementById("results");

searchForm.addEventListener("submit", (event) => {
  event.preventDefault(); // Prevent page refresh
  const searchQuery = searchInput.value;
  // Here you would make a request to your search API or database to retrieve search results
  // For this example, we will create some dummy search results
  const searchResults = [
    {
      title: "Search Result 1",
      url: "https://www.example.com/search-result-1"
    },
    {
      title: "Search Result 2",
      url: "https://www.example.com/search-result-2"
    },
    {
      title: "Search Result 3",
      url: "https://www.example.com/search-result-3"
    },
  ];
  displaySearchResults(searchResults);
});

function displaySearchResults(searchResults) {
  // Clear previous search results
  resultsList.innerHTML = "";
  // Loop through search results and create a list item for each one
  searchResults.forEach(result => {
    const listItem = document.createElement("li");
    listItem.className = "result";
    const link = document.createElement("a");
    link.href = result.url;
    link.textContent = result.title;
    listItem.appendChild(link);
    resultsList.appendChild(listItem);
  });
}
