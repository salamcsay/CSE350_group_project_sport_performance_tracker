// src/pages/DashboardPage.jsx
import React, { useState, useEffect, useContext } from 'react';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Alert, AlertDescription } from "@/components/ui/alert";
import DashboardView from '../views/DashboardView';
import { AuthContext } from '@/context/AuthContext';

const DashboardPage = () => {
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null);
  const { logout } = useContext(AuthContext);

  useEffect(() => {
    const fetchUser = async () => {
      const token = localStorage.getItem('token');
      if (!token) {
        return;
      }
      try {
        const response = await fetch('/api/auth/user/', {
          method: 'GET',
          headers: {
            'Authorization': `Token ${token}`,
          },
        });
        const data = await response.json();
        if (!response.ok) {
          throw new Error(data.detail || 'Failed to fetch user');
        }
        setUser(data);
        setError(null); // Reset error state after successful fetch
      } catch (err) {
        setError(err.message);
      }
    };
    fetchUser();
  }, []);

  const handleLogout = () => {
    logout();
    setUser(null);
  };

  return (
    <div className="flex flex-col items-center min-h-[80vh] w-full">
      {error && <Alert variant="destructive"><AlertDescription>{error}</AlertDescription></Alert>}
      {user ? (
        <div className="w-full">
          <div className="flex justify-between items-center p-4">
            <p>Welcome, {user.username}!</p>
          </div>
          <DashboardView />
        </div>
      ) : (
        <Card className="w-[350px]">
          <CardHeader>
            <CardTitle>Dashboard</CardTitle>
          </CardHeader>
          <CardContent>
            <p>Please log in to see your dashboard.</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default DashboardPage;