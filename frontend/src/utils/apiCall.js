// src/utils/apiCall.js
import axios from 'axios';

const apiCall = axios.create({
    baseURL: "http://127.0.0.1:8000/api/",
    timeout: 3000,
    headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
    }
});

// Add a request interceptor to include the token in the headers
apiCall.interceptors.request.use(
    config => {
        const token = localStorage.getItem('accessToken');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        } else {
            // Handle the case where there is no token
            console.warn("No access token found, redirecting to login.");
            // Optionally, you can redirect to login page here if needed
            // window.location.href = '/login';
        }
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);

export default apiCall;