window.addEventListener('load', async function (event) {
    let responseCategory = await this.fetch('http://localhost:8000/api/categories/')
    let resDataCategory = await responseCategory.json()
    let categorySelect = document.querySelector('[name="category"]')
    for (category of resDataCategory) {
        categorySelect.innerHTML += `
        <option value="${category.id}">${category.title}</option>
        `
    }

    let responseTags = await this.fetch('http://localhost:8000/api/tags/')
    let resDataTags = await responseTags.json()
    let TagSelect = this.document.querySelector('[name = "tags"]')
    for (tag of resDataTags) {
        TagSelect.innerHTML += `
        <option value="${tag.id}">${tag.title}</option>
        `
    }
})

let recipeCreationForm = document.querySelector('#recipeForm')
let token = localStorage.getItem('token')
recipeCreationForm.addEventListener('submit', function (event) {
    event.preventDefault()
    let formData = new FormData(recipeCreationForm)
    let response = fetch('http://localhost:8000/api/recipes/', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`
        },
        body: formData
    })
    if (response){
        alert('success')
    }
})