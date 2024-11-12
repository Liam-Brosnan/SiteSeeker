import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Information = () => {
    const [bookingId, setBookingId] = useState('');
    const [campsiteId, setCampsiteId] = useState(null);
    const [bookingData, setBookingData] = useState(null);
    const [campsiteData, setCampsiteData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const fetchBookingDetails = async () => {
        setLoading(true);
        setError(null);
        try {
            console.log('getting data')
            const bookingResponse = await axios.get(`http://127.0.0.1:8001/api/bookings/${bookingId}/`);
            setBookingData(bookingResponse.data);
            console.log(bookingData)

            const campsiteId = bookingResponse.data.campsite_id;
            setCampsiteId(campsiteId);

            const campsiteResponse = await axios.get(`http://127.0.0.1:8000/api/campsites/${campsiteId}/`);
            setCampsiteData(campsiteResponse.data);
        } catch (err) {
            setError(err);
        } finally {
            setLoading(false);
        }
    };

    const handleInputChange = (e) => {
        setBookingId(e.target.value);
    };

    const handleFormSubmit = (e) => {
        e.preventDefault();
        fetchBookingDetails();
    };

    return (
        <div>
            <form onSubmit={handleFormSubmit}>
                <label>
                    Enter Booking ID:
                    <input type="text" value={bookingId} onChange={handleInputChange} />
                </label>
                <button type="submit">Fetch Details</button>
            </form>

            {loading && <div>Loading...</div>}
            {error && <div>Error: {error.message}</div>}


            {campsiteData && (
                <div>
                    <h1>Campsite Details</h1>
                    <div>
                        <p><strong>Name:</strong> {campsiteData.name}</p>
                        <p><strong>Location:</strong> {campsiteData.location}</p>
                        <p><strong>Amenities:</strong> {campsiteData.amenities}</p>
                        <p><strong>Description:</strong> {campsiteData.description}</p>
                    </div>
                </div>
            )}

            {bookingData && (
                <div>
                    <h1>Booking Details</h1>
                    <div>
                        <p><strong>BookingID</strong> {bookingData.booking_id}</p>
                        <p><strong>Check in Date</strong> {bookingData.check_in_date}</p>
                        <p><strong>Check out Date</strong> {bookingData.check_out_date}</p>
                        <p><strong>Number of People</strong> {bookingData.number_of_people}</p>
                </div>
                </div>
            )}
        </div>
    );
};

export default Information;

