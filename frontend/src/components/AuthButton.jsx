// src/components/AuthButton.jsx
import React, { useContext } from 'react';
import { Button } from "@/components/ui/button";
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '@/context/AuthContext';

const AuthButton = () => {
  const navigate = useNavigate();
  const { isAuthenticated } = useContext(AuthContext);

  if (isAuthenticated) {
    return null; // Don't render anything if the user is logged in
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