window.addEventListener('load', async function (event) {
    let response = await fetch('http://localhost:8000/api/recipes/')
    let resData = await response.json()
    let recipe_lists = document.querySelector('#recipe_lists')
    for (recipe of resData) {
        recipe_lists.innerHTML += `
        <div class="col">
        <div class="card" style="width: 18rem;">
            <img src="${recipe.image}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">${recipe.title} - ${recipe.category.title}</h5>
                <p class="card-text">${recipe.small_description}</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </div>
    </div>
        `
    }
})