let loginForm = document.querySelector('#login-form')

loginForm.addEventListener('submit', async function(e){
    e.preventDefault()
    let postData = {
        'email': loginForm.email.value,
        'password': loginForm.password.value
    }
    let response = await fetch('http://localhost:8000/auth/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body:JSON.stringify(postData),
    })
    let resData = await response.json()
    if (response){
        localStorage.setItem('token', resData.access)
    }

})