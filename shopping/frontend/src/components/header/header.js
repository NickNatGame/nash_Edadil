import React from 'react';
import { NavLink } from 'react-router-dom';

const navItems = [
  { to: '/', label: 'Все товары', end: true },
  { to: '/fav', label: 'Избранное' },
  { to: '/cart', label: 'Корзина' }
];

function Header() {
  return (
    <header className="header">
      <div className="header__brand">
        <p className="header__eyebrow">Smart Shopping</p>
        <h1 className="header__title">Сравнение и оптимизация корзины</h1>
      </div>
      <nav className="header__nav" aria-label="Основная навигация">
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            end={item.end}
            className={({ isActive }) => `link nav-link${isActive ? ' nav-link_active' : ''}`}
          >
            {item.label}
          </NavLink>
        ))}
      </nav>
    </header>
  );
}

export default Header;
