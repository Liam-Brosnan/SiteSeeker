import React from 'react';
import './home.css';
import Header from '../../components/header/Header';

function HomePage() {
    return (
        <div>
            <Header />
            <div className='main-content'>
                <img src='/home-page-image.jpg' alt='scenic view' className='background-image' />
            </div>
        </div>

    );
}

export default HomePage;
