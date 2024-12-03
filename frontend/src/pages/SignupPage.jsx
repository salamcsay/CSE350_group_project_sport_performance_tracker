// src/pages/SignupPage.jsx
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { getCsrfToken } from '@/utils/csrf';

const SignupPage = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password1: '',
    password2: ''
  });
  const [error, setError] = useState(null);
  const navigate = useNavigate();
  const [csrfToken, setCsrfToken] = useState('');

  useEffect(() => {
    const fetchCsrfToken = async () => {
      const token = await getCsrfToken();
      console.log('CSRF token:', token);  // Add logging
      setCsrfToken(token);
    };
    fetchCsrfToken();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (formData.password1 !== formData.password2) {
      setError('Passwords do not match');
      return;
    }
    try {
      console.log('Submitting form data:', formData);  // Add logging
      const response = await fetch('/api/auth/registration/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(formData),
        credentials: 'include',
      });
      console.log('Response status:', response.status);  // Add logging
      const data = await response.json();
      console.log('Response data:', data);  // Add logging
      if (!response.ok) {
        throw new Error(data.detail || 'Registration failed');
      }
      navigate('/login');
    } catch (err) {
      console.error('Error:', err.message);  // Add logging
      setError(err.message);
    }
  };

  return (
    <div className="flex justify-center items-center min-h-[80vh]">
      <Card className="w-[350px]">
        <CardHeader>
          <CardTitle>Create Account</CardTitle>
        </CardHeader>
        <CardContent>
          {error && <Alert variant="destructive"><AlertDescription>{error}</AlertDescription></Alert>}
          <form onSubmit={handleSubmit} className="space-y-4">
            <Input
              type="text"
              placeholder="Username"
              value={formData.username}
              onChange={(e) => setFormData({...formData, username: e.target.value})}
              required
            />
            <Input
              type="email"
              placeholder="Email"
              value={formData.email}
              onChange={(e) => setFormData({...formData, email: e.target.value})}
              required
            />
            <Input
              type="password"
              placeholder="Password"
              value={formData.password1}
              onChange={(e) => setFormData({...formData, password1: e.target.value})}
              required
            />
            <Input
              type="password"
              placeholder="Confirm Password"
              value={formData.password2}
              onChange={(e) => setFormData({...formData, password2: e.target.value})}
              required
            />
            <Button type="submit" className="w-full">Create Account</Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
};

export default SignupPage;