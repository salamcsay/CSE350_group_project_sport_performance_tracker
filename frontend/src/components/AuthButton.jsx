// src/components/AuthButton.jsx
import React from 'react';
import { Button } from "@/components/ui/button";
import { useNavigate } from 'react-router-dom';

const AuthButton = () => {
  const navigate = useNavigate();
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