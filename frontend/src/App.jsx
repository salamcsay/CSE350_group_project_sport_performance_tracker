import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import AppLayout from './components/AppLayout';
import DashboardView from './views/DashboardView';
import PlayersView from './views/PlayersView';
import ClubsView from './views/ClubsView';
import DashboardPage from './pages/DashboardPage';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import { AuthProvider } from './context/AuthContext';

const App = () => {
  return (
<AuthProvider>
    <AppLayout>
      <Routes>
        <Route path="/" element={<DashboardPage />} />
        <Route path="/players" element={<PlayersView />} />
        <Route path="/clubs" element={<ClubsView />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} />
      </Routes>
    </AppLayout>
</AuthProvider>
  );
};

export default App;