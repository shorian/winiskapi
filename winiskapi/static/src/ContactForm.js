import React from "react";
import Form from "react-formal";
import { contactSchema } from "./contactSchema";
import handleSubmit from "./handleSubmit";
import { createRoot } from "react-dom/client";
/* eslint-disable jsx-a11y/label-has-associated-control */

// const handleSubmit = (formData) => {
//   alert(JSON.stringify(formData, null, 2));
// };
//

const ContactForm = (
  <Form schema={contactSchema} submitForm={handleSubmit}>
    <legend className="mt-4 h2 text-center">Create New Contact</legend>
    <fieldset className="border border-primary rounded m-2 px-4 pb-3">
      <legend>Name</legend>
      <div className="d-flex justify-content-between">
        <label className="form-label mr-2">
          First name<span className="text-primary">*</span>
          <Form.Field name="first_name" className="form-control" />
        </label>
        <label className="form-label mr-2">
          Middle name
          <Form.Field name="middle_name" className="form-control" />
        </label>
        <label className="form-label mr-2">
          Last name
          <Form.Field name="last_name" className="form-control" />
        </label>
        <label className="form-label mr-2">
          Nickname
          <Form.Field name="nickname" className="form-control" />
        </label>
      </div>
      <div>
        <Form.Message
          for={["first_name", "middle_name", "last_name", "nickname"]}
        >
          {(errors) => <span>{errors.pop()}</span>}
        </Form.Message>
      </div>
    </fieldset>
    <div className="d-flex justify-content-between">
      <fieldset className="border border-primary rounded m-2 px-4 pb-3">
        <legend>Personal details</legend>
        <div className="d-flex justify-content-between flex-fill">
          <label className="form-label mr-2">
            Birthday
            <Form.Field name="dob" className="form-control" />
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
              <option value=""></option>
              <option>Male</option>
              <option>Female</option>
              <option>Nonbinary</option>
            </Form.Field>
          </label>
        </div>
        <div>
          <Form.Message for={["dob", "pronouns", "gender"]}>
            {(errors) => <span>{errors.pop()}</span>}
          </Form.Message>
        </div>
      </fieldset>
      <fieldset className="border border-primary rounded m-2 px-4 pb-3">
        <legend>Work</legend>
        <div className="d-flex flex-fill justify-content-between">
          <label className="form-label mr-2">
            Organization
            <Form.Field name="organization" className="form-control" />
          </label>
          <label className="form-label mr-2">
            Role
            <Form.Field name="job_title" className="form-control" />
          </label>
        </div>
        <div>
          <Form.Message for={["organization", "job_title"]}>
            {(errors) => <span>{errors.pop()}</span>}
          </Form.Message>
        </div>
      </fieldset>
    </div>

    <div className="d-flex justify-content-center">
      <Form.Submit
        type="submit"
        className="btn btn-lg btn-primary my-3 px-4 text-center"
      >
        Submit
      </Form.Submit>
    </div>
  </Form>
);

const container = document.getElementById("contact-form");
if (container) {
  const root = createRoot(container);
  root.render(ContactForm);
}
