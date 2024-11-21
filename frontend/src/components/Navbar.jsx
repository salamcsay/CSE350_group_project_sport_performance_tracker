import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/players">Player Stats</Link></li>
        <li><Link to="/clubs">Club Stats</Link></li>
        <li><Link to="/search">Search</Link></li>
        <li><Link to="/dashboard">Dashboard</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
