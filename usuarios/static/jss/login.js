const init = () => {
    const inputRA = document.querySelector ('input[type="RA"]');
    const inputSenha = document.querySelector ('input[type="Senha"]');
    const submitButton = document.querySelector ('.login_submit');

    if(submitButton) {
        submitButton.addEventListener('click', (event) => {
            event.preventDefault ();

            fetch ('https://reqres.in/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    RA: inputRA.value,
                    Senha: inputSenha.value,
                })
            }).then((response) => {
                return response.json();
            }).then ((data) => {
                console.log(data);
            })
        })
    }
}

window.onload = init;