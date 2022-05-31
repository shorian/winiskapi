
function handleSubmit (values, {setSubmitting}) {
                    const url = '/'
                    const requestOptions = {
                        method: 'POST',
                        redirect: "follow",
                        headers: {'Content-Type': 'application/json',
                        "X-CSRFToken": document.getElementById("csrf_token").value},
                        body: JSON.stringify({values})
                    };
                    fetch(url, requestOptions)
                        .then(response => {
                            if (response.redirected) {
                                window.location.href = response.url;
                            }
                        })
                        .catch(error => console.log('Form submit error', error))
                    setSubmitting(false);
                }

export default handleSubmit