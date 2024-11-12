import React, { useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const BookingForm = () => {
    const { id } = useParams();
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [numberOfPeople, setNumberOfPeople] = useState('');
    const [message, setMessage] = useState('');
    const [bookingID, setBookingID] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        const bookingData = {
            campsite_id: id,
            start_date: startDate,
            end_date: endDate,
            number_of_people: numberOfPeople,
        };

        console.log('Data being sent:', bookingData);

        try {
            // Check availability
            const response = await axios.post('http://127.0.0.1:8000/api/availabilities/update-availability/', bookingData); 

                if (response.data.status === 'Availability updated successfully') {
                    setBookingID(response.data.booking_id)
                    setMessage('Booking successful!');
                } else if (response.data.error) {
                    setMessage(response.data.error);
                } else {
                    setMessage('An unexpected response was recieved.')
                }

            } catch (error) {
                console.error('Error making booking:', error);
                setMessage('An error occurred while making the booking.');
            }
        };

        return (
            <div>
                <h1>Book a Campsite</h1>
                <form onSubmit={handleSubmit}>
                    <div>
                        <label>Start Date:</label>
                        <input
                            type="date"
                            value={startDate}
                            onChange={(e) => setStartDate(e.target.value)}
                            required
                        />
                    </div>
                    <div>
                        <label>End Date:</label>
                        <input
                            type="date"
                            value={endDate}
                            onChange={(e) => setEndDate(e.target.value)}
                            required
                        />
                    </div>
                    <div>
                        <label>Number of People:</label>
                        <input
                            type="number"
                            value={numberOfPeople}
                            onChange={(e) => setNumberOfPeople(e.target.value)}
                            required
                        />
                    </div>
                    <button type="submit">Book</button>
                </form>
                {message && <p>{message}</p>}
                {bookingID && <p>Your Booking ID: {bookingID}</p>}
            </div>
        );
    };

    export default BookingForm;
