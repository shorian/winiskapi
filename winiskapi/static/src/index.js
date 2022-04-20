import React from "react";
import * as yup from "yup"
import {createRoot} from "react-dom/client";
import Form, {useFormValues} from "react-formal"

const contactSchema = yup.object({
                    firstName: yup.string().required("Required"),
                    middleName: yup.string(),
                    lastName: yup.string(),
                    nickname: yup.string(),

                    birthday: yup.date().max(new Date(), "Date of birth must be in the past."),
                    pronouns: yup.string(),
                    gender: yup.string(),

                    organization: yup.string(),
                    role: yup.string()
                });

const handleSubmit = (formData) => {
  alert(JSON.stringify(formData, null, 2));
};

const Names = () => {
    const names = useFormValues(["firstName", "middleName", "lastName"]).filter(Boolean).join(" ");
    return (
        <span>{names}</span>
    );
};

const mySubmit = () => <button type="submit" className="btn btn-primary">Submit</button>


const contactForm = <Form schema={contactSchema}>
    <fieldset>
        <legend>Name</legend>
        <div className="d-flex">
            <label className="form-label mr-2">
                First name
                <Form.Field name="firstName" className="form-control"/>
            </label>
            <label className="form-label mr-2">
                Middle name
                <Form.Field name="middleName" className="form-control"/>
            </label>
            <label className="form-label mr-2">
                Last name
                <Form.Field name="lastName" className="form-control"/>
            </label>
            <label className="form-label mr-2">
                Nickname
                <Form.Field name="nickname" className="form-control"/>
            </label>
        </div>
        <span><small>Their full name will be displayed as <Names/>. Is that correct?</small></span>
    </fieldset>
    <fieldset>
        <legend>Personal details</legend>
        <label className="form-label mr-2">
            Birthday
            <Form.Field name="birthday" className="form-control"/>
        </label>
        <label className="form-label mr-2">
            Pronouns
            <Form.Field name="pronouns" as="select" className="form-control">
                <option value=" "> </option>
                <option value="he">He/him/his/his</option>
                <option value="she">She/her/her/hers</option>
                <option value="they">They/them/their/theirs</option>
            </Form.Field>
        </label>
        <label className="form-label mr-2">
            Gender
            <Form.Field name="gender" as="select" className="form-control">
                <option value="U"> </option>
                <option value="M">Male</option>
                <option value="F">Female</option>
                <option value="N">Nonbinary</option>
            </Form.Field>
        </label>
    </fieldset>
    <fieldset>
        <legend>Work</legend>
            <div className="d-flex">
                <label className="form-label mr-2">
                    Organization
                    <Form.Field name="organization" className="form-control"/>
                </label>
                <label className="form-label mr-2">
                    Role
                    <Form.Field name="role" className="form-control"/>
                </label>
            </div>
    </fieldset>
    <Form.Submit type="submit" as={mySubmit}/>
</Form>;
//
// onSubmit={(values, {setSubmitting}) => {
//                     const url = '/'
//                     const requestOptions = {
//                         method: 'POST',
//                         redirect: "follow",
//                         headers: {'Content-Type': 'application/json'},
//                         body: JSON.stringify({values})
//                     };
//                     fetch(url, requestOptions)
//                         .then(response => {
//                             if (response.redirected) {
//                                 window.location.href = response.url;
//                             }
//                         })
//                         .catch(error => console.log('Form submit error', error))
//                     setSubmitting(false);
//                 }


function App() {
    return contactForm;
}

const container = document.getElementById('root');
const root = createRoot(container); // createRoot(container!) if you use TypeScript
root.render(<App tab="home"/>);