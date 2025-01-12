import React from "react";
import { BrowserRouter as Router, Route, Routes, Navigate } from "react-router-dom";
import Register from "./pages/Register";
import Login from "./pages/Login";
import Home from "./pages/Home";
import ProtectedEvents from "./pages/ProtectedEvents";
import EventForm from "./pages/EventForm";

// Authentication Check Function
const isAuthenticated = () => {
    return !!localStorage.getItem("token");
};

// Protected Route Component
const ProtectedRoute = ({ element }) => {
    return isAuthenticated() ? element : <Navigate to="/login" />;
};

const App = () => {
    return (
        <Router>
            <div>
                {/* Simple Navigation Bar */}
                <nav>
                    <a href="/">Home</a> |{" "}
                    <a href="/register">Register</a> |{" "}
                    <a href="/login">Login</a> |{" "}
                    <a href="/events">Events</a> |{" "}
                    <a href="/create-event">Create Event</a>
                </nav>

                {/* Route Management */}
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/login" element={<Login />} />
                    
                    {/* Protected Routes */}
                    <Route path="/events" element={<ProtectedRoute element={<ProtectedEvents />} />} />
                    <Route path="/create-event" element={<ProtectedRoute element={<EventForm />} />} />
                    
                    {/* Catch-all Route */}
                    <Route path="*" element={<h2>404 - Page Not Found</h2>} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
