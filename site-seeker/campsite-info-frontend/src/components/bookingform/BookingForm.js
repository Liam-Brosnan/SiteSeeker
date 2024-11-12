import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import './BookingForm.css';

const BookingForm = () => {
    const [startDate, setStartDate] = useState(new Date());
    const [endDate, setEndDate] = useState(new Date());
    const [guests, setGuests] = useState(1);

    return (
        <div className="booking-form">
            <h1>Book Now</h1>
            <form>
                <div>
                    <label>Check In</label>
                    <DatePicker selected={startDate} onChange={date => setStartDate(date)} />
                </div>
                <div>
                    <label>Check Out</label>
                    <DatePicker selected={endDate} onChange={date => setEndDate(date)} />
                </div>
                <div>
                    <label>Guests</label>
                    <input type="number" value={guests} onChange={e => setGuests(e.target.value)} min="1" />
                </div>
                <button type="submit">Search</button>
            </form>
        </div>
    );
};

export default BookingForm;
