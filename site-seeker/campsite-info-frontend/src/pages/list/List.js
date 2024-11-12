import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import "./list.css"

const CampsiteList = () => {
    const [campsites, setCampsites] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchCampsites();
    }, []);

    const fetchCampsites = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/campsites/');
            setCampsites(response.data);
            setLoading(false);
        } catch (error) {
            console.error('Error fetching campsites:', error);
            setLoading(false);
        }
    };


    if (loading) {
        return <p>Loading...</p>;
    }

    return (
        <div>
            <h2 className='page-title'>Campsites</h2>
            <ul className='campsite-list'>
                {campsites.map(campsite => (
                    <li key={campsite.id} className="campsite-item">
                        <strong className='campsite-title'>{campsite.name}</strong>
                        <span> <strong>Location:</strong> {campsite.location}</span>
                        <span> <strong>Capacity:</strong> {campsite.capacity}</span>
                        <span> <strong>Amenities:</strong> {campsite.amenities}</span>
                        <span> <strong>Description:</strong> {campsite.description}</span>
                        <Link to={`/campsite/${campsite.id}`}>Book</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CampsiteList;
