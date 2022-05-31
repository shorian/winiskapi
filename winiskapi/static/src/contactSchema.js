import * as yup from "yup";

const contactSchema = yup.object({
    name: yup.object({
        first: yup.string().max(30, "Names must be 30 characters or less").required("First name is required"),
        middle: yup.string().max(30, "Names must be 30 characters or less"),
        last: yup.string().max(30, "Names must be 30 characters or less"),
        nickname: yup.string().max(30, "Names must be 30 characters or less"),
    }),
    birthday: yup.date().max(new Date(), "Date of birth must be in the past"),
    pronouns: yup.string().oneOf(["", "he", "she", "they"]),
    gender: yup.string().oneOf(["U", "N", "M", "F"]),

    organization: yup.string().max(50, "Organization must be 50 characters or less"),
    role: yup.string().max(50, "Role must be 50 characters or less")
});

export default contactSchema