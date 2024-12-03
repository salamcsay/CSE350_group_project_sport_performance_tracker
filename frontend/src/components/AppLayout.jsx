// src/components/AppLayout.jsx
import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Card } from "@/components/ui/card";
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Button } from "@/components/ui/button";
import AuthButton from './AuthButton';

const AppLayout = ({ children }) => {
  const location = useLocation();

  return (
    <div className="min-h-screen flex">
      {/* Sidebar */}
      <aside className="w-64 bg-background border-r p-4">
        <div className="space-y-4">
          <h2 className="text-2xl font-bold">StatsTrackr</h2>
          <nav className="space-y-2">
            <Link to="/" className="block hover:bg-accent p-2 rounded-lg">
              Dashboard
            </Link>
            <Link to="/players" className="block hover:bg-accent p-2 rounded-lg">
              Players
            </Link>
            <Link to="/clubs" className="block hover:bg-accent p-2 rounded-lg">
              Clubs
            </Link>
          </nav>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-8">
        <div className="flex justify-between items-center mb-4">
          <Tabs value={location.pathname}>
            <TabsList>
              <TabsTrigger value="/" asChild>
                <Link to="/">Dashboard</Link>
              </TabsTrigger>
              <TabsTrigger value="/players" asChild>
                <Link to="/players">Players</Link>
              </TabsTrigger>
              <TabsTrigger value="/clubs" asChild>
                <Link to="/clubs">Clubs</Link>
              </TabsTrigger>
            </TabsList>
          </Tabs>
          <AuthButton />
        </div>
        <Card className="p-6">
          {children}
        </Card>
      </main>
    </div>
  );
};

export default AppLayout;