import React from 'react';
import { createRoot } from 'react-dom/client';
import NavBar from './components/NavBar';
import FormComponent from './components/FilterForm';

const navbarContainer = document.getElementById('navbar');
const formContainer = document.getElementById('form-root');

if (navbarContainer) {
    const navbarRoot = createRoot(navbarContainer);
    navbarRoot.render(<NavBar />);
}

if (formContainer) {
    const formRoot = createRoot(formContainer);
    formRoot.render(<FormComponent />);
}