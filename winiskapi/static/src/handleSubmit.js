
const handleSubmit = (formData) => {
                    const url = '/contacts/new'
                    const requestOptions = {
                        method: 'POST',
                        redirect: "follow",
                        headers: {'Content-Type': 'application/json',
                        "X-CSRFToken": document.getElementById("csrf_token").value},
                        body: JSON.stringify({formData})
                    };
                    fetch(url, requestOptions)
                        .then(response => {
                            if (response.redirected) {
                                window.location.href = response.url;
                            }
                        })
                        .catch(error => console.log('Form submit error', error))
                        }

export default handleSubmit