import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import PlayerStats from './components/PlayerStats';
import ClubStats from './components/ClubStats';
import SearchFilter from './components/SearchFilter';
import Dashboard from './components/Dashboard';


const App = () => (
  <Router>
    <Navbar />
    <Routes>
      <Route path="/players" element={<PlayerStats />} />
      <Route path="/clubs" element={<ClubStats />} />
      <Route path="/search" element={<SearchFilter />} />
      <Route path="/dashboard" element={<Dashboard />} />
    </Routes>
  </Router>
);

export default App;
