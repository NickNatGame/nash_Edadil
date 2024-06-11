import React from "react";
import { Link } from "react-router-dom";

function Header() {
    return(
        <header className="header">
            <button className="button button_type_main">
                <Link to="/" className="link">Все товары</Link>
            </button>
            <button className="button button_type_main">
                <Link to="/fav" className="link">Избранное</Link>
            </button>
            <button className="button button_type_main">
                <Link to="/cart" className="link">Корзина</Link>
            </button>
        </header>
    );
}

export default Header;