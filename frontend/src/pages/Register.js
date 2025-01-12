import React, { useState } from "react";
import { registerUser } from "../api";

const Register = () => {
    const [formData, setFormData] = useState({ email: "", password: "" });

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await registerUser(formData);
            alert("User registered successfully!");
        } catch (error) {
            alert("Error registering user.");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="email"
                placeholder="Email"
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
            />
            <input
                type="password"
                placeholder="Password"
                onChange={(e) => setFormData({ ...formData, password: e.target.value })}
            />
            <button type="submit">Register</button>
        </form>
    );
};

export default Register;
