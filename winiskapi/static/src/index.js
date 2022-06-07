import React from "react";
import { createRoot } from "react-dom/client";
import ContactForm from "./ContactForm";
import "bootstrap";

function App() {
  return ContactForm;
}

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App />);
