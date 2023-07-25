let subscribeForm = document.getElementById('subscribe-form')

subscribeForm.addEventListener('submit', function(e){
    e.preventDefault()
    let email = document.getElementById('email').value
    fetch('http://localhost:8000/api/subscribers/', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : subscribeForm.csrfmiddlewaretoken.value
        },
        body: JSON.stringify({
            'email' : email,
        })
        
    })
    .then(response => {
        if (response.ok){
            subscribeForm.innerHTML = `<h2>Thanks for your subscribing!</h2>`
        }
        else{
            alert('Error')
        }
    })
})