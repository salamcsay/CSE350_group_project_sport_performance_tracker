import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import AppLayout from './components/AppLayout';
import DashboardView from './views/DashboardView';
import PlayersView from './views/PlayersView';
import ClubsView from './views/ClubsView';

const App = () => {
  return (
    <AppLayout>
      <Routes>
        <Route path="/" element={<DashboardView />} />
        <Route path="/players" element={<PlayersView />} />
        <Route path="/clubs" element={<ClubsView />} />
      </Routes>
    </AppLayout> 
  );
};

export default App;