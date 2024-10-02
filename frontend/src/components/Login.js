// src/components/Login.js
import { useDispatch } from 'react-redux';
import authService from '../utils/authService';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async (event) => {
        event.preventDefault();
        try {
            let loginData = {
                email,
                password
            };
            await authService.login(loginData);
            navigate('/profile'); // Redirect to profile page
        } catch (error) {
            console.error("Login failed:", error);
        }
    };

    return (
        <div>
            <form onSubmit={handleLogin}>
                <label>Email</label>
                <input value={email} onChange={(e) => setEmail(e.target.value)} />
                <label>Password</label>
                <input value={password} onChange={(e) => setPassword(e.target.value)} />
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default Login;