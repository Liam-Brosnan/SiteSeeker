import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Navbar from './components/navbar/Navbar';
import BookingForm from './pages/booking/Booking';
import HomePage from './pages/home/Home';
import Information from './pages/information/information';
import List from './pages/list/List';

function App() {
    return (
        <Router>
            <div className="App">
                <Navbar />
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/campsites" element={<List />} />
                    <Route path="/campsite/:id" element={<BookingForm />} />
                    <Route path="/information" element={<Information />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;

