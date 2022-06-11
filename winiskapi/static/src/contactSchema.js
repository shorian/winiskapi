import * as yup from "yup";

let cid = 0;

const contact_field = yup.object({
  id: yup.number().default(() => cid++),
  type: yup.string(),
  value: yup.string(),
});

const contactSchema = yup.object({
  first_name: yup
    .string()
    .max(30, "Names must be 30 characters or less")
    .required("First name is required")
    .trim(),
  middle_name: yup
    .string()
    .max(30, "Names must be 30 characters or less")
    .trim(),
  last_name: yup.string().max(30, "Names must be 30 characters or less").trim(),
  nickname: yup.string().max(30, "Names must be 30 characters or less").trim(),
  dob: yup.date().max(new Date(), "Date of birth must be in the past"),
  pronouns: yup.string().oneOf(["", "he", "she", "they"]),
  gender: yup.string().max(30, "Gender must be 30 characters or less").trim(),
  organization: yup
    .string()
    .max(50, "Organization must be 50 characters or less")
    .trim(),
  job_title: yup.string().max(50, "Role must be 50 characters or less").trim(),
  // contact_info: yup.array().of(contact_field)
});

export { contact_field, contactSchema };
