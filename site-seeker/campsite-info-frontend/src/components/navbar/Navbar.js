import "./navbar.css";
import {Link} from "react-router-dom";

const Navbar = () => {
    return (
        <div className="navbar">
            <div className="navContainer">
                <Link to="/" className="logo">Home </Link>
                <Link to="campsites" className="list">Campsites </Link>
                <Link to="information" className="information">Booking Information </Link>
            </div>
        </div>
    )
}

export default Navbar
