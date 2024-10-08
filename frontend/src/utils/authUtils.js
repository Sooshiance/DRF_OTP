// src/utils/authUtils.js
import apiCall from './apiCall';
import { useNavigate } from 'react-router-dom';

export const fetchWithAuth = async (endpoint, navigate) => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
        console.warn("No access token found, redirecting to login.");
        navigate('/login'); // Redirect to login if no token
        return null;
    }

    try {
        const response = await apiCall.get(endpoint);
        return response.data;
    } catch (error) {
        console.error("Failed to fetch data:", error);
        throw error;
    }
};