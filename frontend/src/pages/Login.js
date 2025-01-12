import React, { useState } from "react";
import { loginUser } from "../api";

const Login = () => {
    const [formData, setFormData] = useState({ email: "", password: "" });

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const data = await loginUser(formData);
            alert(`Welcome! Token: ${data.access_token}`);
        } catch (error) {
            alert("Login failed!");
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
            <button type="submit">Login</button>
        </form>
    );
};

export default Login;
