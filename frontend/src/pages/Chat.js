import React, { useState, useEffect } from "react";
import { io } from "socket.io-client";

const socket = io("ws://localhost:8000/ws/chat");

const Chat = () => {
    const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState("");
    const [userEmail, setUserEmail] = useState(localStorage.getItem("email"));

    useEffect(() => {
        // Receive messages from the server
        socket.on("message", (data) => {
            setMessages((prevMessages) => [...prevMessages, data]);
        });

        return () => {
            socket.disconnect();
        };
    }, []);

    const sendMessage = () => {
        if (message.trim()) {
            const chatMessage = {
                sender_email: userEmail,
                receiver_email: "student2@example.com", // Adjust for dynamic receiver
                message: message,
            };
            socket.emit("message", chatMessage);
            setMessage(""); // Clear input field
        }
    };

    return (
        <div>
            <h1>Real-Time Chat</h1>
            <div>
                {messages.map((msg, index) => (
                    <p key={index}>
                        <strong>{msg.sender_email}:</strong> {msg.message}
                    </p>
                ))}
            </div>
            <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
            />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
};

export default Chat;
