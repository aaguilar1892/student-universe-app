import axios from "axios";

const API_URL = "http://localhost:8000/api";

export async function fetchEvents() {
  const response = await fetch(`${API_URL}/events`);
  return response.json();
}

export async function createEvent(eventData) {
  const response = await fetch(`${API_URL}/events`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(eventData),
  });
  return response.json();
}

export const registerUser = async (userData) => {
    return await axios.post(`${API_URL}/auth/register`, userData);
};

export const loginUser = async (credentials) => {
    const response = await axios.post(`${API_URL}/auth/login`, credentials);
    localStorage.setItem("token", response.data.access_token);
    return response.data;
};

export const fetchProtectedEvents = async () => {
    const token = localStorage.getItem("token");
    const response = await axios.get(`${API_URL}/events`, {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });
    return response.data;
};