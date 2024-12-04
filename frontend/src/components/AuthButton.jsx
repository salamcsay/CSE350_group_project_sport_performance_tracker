// src/components/AuthButton.jsx
import React, { useContext } from 'react';
import { Button } from "@/components/ui/button";
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '@/context/AuthContext';

const AuthButton = () => {
  const navigate = useNavigate();
  const { isAuthenticated, logout } = useContext(AuthContext);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  if (isAuthenticated) {
    return (
      <Button onClick={handleLogout} variant="destructive">
        Logout
      </Button>
    );
  }

  return (
    <div className="flex gap-2">
      <Button variant="outline" onClick={() => navigate('/login')}>
        Sign In
      </Button>
      <Button onClick={() => navigate('/signup')}>
        Create Account
      </Button>
    </div>
  );
};

export default AuthButton;