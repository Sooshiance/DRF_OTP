// src/components/Profile.js
import React, { useEffect, useState } from 'react';
import apiCall from '../utils/apiCall';
import { useNavigate } from 'react-router-dom';
import { fetchWithAuth } from '../utils/authUtils';

function Profile() {
    const [profile, setProfile] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const data = await fetchWithAuth("user/profile/", navigate);
                if (data) {
                    setProfile(data);
                }
            } catch (error) {
                console.error("Failed to fetch profile:", error);
            }
        };

        fetchProfile();
    }, [navigate]);

    return (
        <>
            <div>Profile Page</div>
            <div>
                {profile ? (
                    <h1>{profile.phone}</h1>
                ) : (
                    <p>Loading...</p>
                )}
            </div>
        </>
    );
}

export default Profile;