import React from "react";
import Form from "react-formal";
import contactSchema from "./contactSchema";
/* eslint-disable jsx-a11y/label-has-associated-control */

const handleSubmit = (formData) => {
  alert(JSON.stringify(formData, null, 2));
};



const ContactForm = <Form schema={contactSchema} onSubmit={handleSubmit}>
    <legend className="mt-4 h2 text-center">Create New Contact</legend>
    <fieldset className="border border-primary rounded mt-2 px-4 pb-3">
        <legend className="w-auto px-2">Name</legend>
        <div className="d-flex justify-content-between">
            <label className="form-label mr-2">
                First name<span className="text-primary">*</span>
                <Form.Field name="name.first" className="form-control"/>
            </label>
            <label className="form-label mr-2">
                Middle name
                <Form.Field name="name.middle" className="form-control"/>
            </label>
            <label className="form-label mr-2">
                Last name
                <Form.Field name="name.last" className="form-control"/>
            </label>
            <label className="form-label mr-2">
                Nickname
                <Form.Field name="name.nickname" className="form-control"/>
            </label>
        </div>
        <div><Form.Message for={["name.first", "name.middle", "name.last", "name.nickname",]}>
            {errors => <span>{errors.pop()}</span>}
        </Form.Message></div>
    </fieldset>
    <div className="d-flex justify-content-between">
        <fieldset className="border border-primary rounded mt-2 px-4 pb-3">
            <legend className="w-auto px-2">Personal details</legend>
            <div className="d-flex flex-column justify-content-between flex-fill"><label className="form-label mr-2">
                Birthday
                <Form.Field name="birthday" className="form-control"/>
            </label>
                <label className="form-label mr-2">
                    Pronouns
                    <Form.Field name="pronouns" className="form-control" as="select">
                        <option value=""></option>
                        <option value="he">He/him/his/his</option>
                        <option value="she">She/her/her/hers</option>
                        <option value="they">They/them/their/theirs</option>
                    </Form.Field>
                </label>
                <label className="form-label mr-2">
                    Gender
                    <Form.Field name="gender" as="select" className="form-control">
                        <option value="U"></option>
                        <option value="M">Male</option>
                        <option value="F">Female</option>
                        <option value="N">Nonbinary</option>
                    </Form.Field>
                </label></div>
            <div><Form.Message for={["birthday", "pronouns", "gender"]}>
                {errors => <span>{errors.pop()}</span>}
            </Form.Message></div>
        </fieldset>
        <fieldset className="border border-primary rounded mt-2 px-4 pb-3">
            <legend className="w-auto px-2">Work</legend>
            <div className="d-flex flex-column flex-fill justify-content-between">
                <label className="form-label mr-2">
                    Organization
                    <Form.Field name="organization" className="form-control"/>
                </label>
                <label className="form-label mr-2">
                    Role
                    <Form.Field name="role" className="form-control"/>
                </label>
            </div>
            <div><Form.Message for={["organization", "role"]}>
                {errors => <span>{errors.pop()}</span>}
            </Form.Message></div>
        </fieldset>
    </div>

    <div className="d-flex justify-content-center"><Form.Submit type="submit" className="btn btn-lg btn-primary my-3 px-4 text-center">Submit</Form.Submit></div>
</Form>;

export default ContactForm