import React from 'react';
import { Link } from 'react-router-dom';

function Layout({ children }) {
    return (
        <div>
            <header>
                <nav>
                    <ul>
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/AboutUs">About Us</Link></li>
                        <li><Link to="/ContactUs">Contact Us</Link></li>
                    </ul>
                </nav>
            </header>
            <main>{children}</main>
        </div>
    );
}

export default Layout;
