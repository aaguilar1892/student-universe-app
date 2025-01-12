import React, { useEffect, useState } from "react";
import { fetchProtectedEvents } from "../api";

const ProtectedEvents = () => {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        fetchProtectedEvents()
            .then((data) => setEvents(data))
            .catch((err) => alert("Unauthorized access! Please log in."));
    }, []);

    return (
        <div>
            <h1>Protected Events</h1>
            <ul>
                {events.map((event) => (
                    <li key={event._id}>{event.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default ProtectedEvents;
