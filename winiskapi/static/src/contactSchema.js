import * as yup from "yup";

let cid = 0;

const contact_field = yup.object({
        id: yup.number().default(() => cid++),
        type: yup.string(),
        value: yup.string()
    })

const contactSchema = yup.object({
    first_name: yup.string().max(30, "Names must be 30 characters or less").required("First name is required"),
    middle_name: yup.string().max(30, "Names must be 30 characters or less"),
    last_name: yup.string().max(30, "Names must be 30 characters or less"),
    nickname: yup.string().max(30, "Names must be 30 characters or less"),
    dob: yup.date().max(new Date(), "Date of birth must be in the past"),
    pronouns: yup.string().oneOf(["", "he", "she", "they"]),
    gender: yup.string().oneOf(["U", "N", "M", "F"]),

    organization: yup.string().max(50, "Organization must be 50 characters or less"),
    job_title: yup.string().max(50, "Role must be 50 characters or less"),
    // contact_info: yup.array().of(contact_field)
});

export {contact_field, contactSchema}