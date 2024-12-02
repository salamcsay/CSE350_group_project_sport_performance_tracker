import React from 'react';
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Card } from "@/components/ui/card"
import { useNavigate, useLocation } from 'react-router-dom';

const AppLayout = ({ children }) => {
  const navigate = useNavigate();
  const location = useLocation();
  
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <h1 className="text-3xl font-bold text-gray-900">StatTrackr</h1>
        </div>
      </header>
      
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <Card className="p-6">
          <Tabs value={location.pathname} onValueChange={(value) => navigate(value)}>
            <TabsList className="mb-6">
              <TabsTrigger value="/">Dashboard</TabsTrigger>
              <TabsTrigger value="/players">Players</TabsTrigger>
              <TabsTrigger value="/clubs">Clubs</TabsTrigger>
            </TabsList>
          </Tabs>
          {children}
        </Card>
      </main>
    </div>
  );
};

export default AppLayout;