import React from 'react';
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { Loader2 } from "lucide-react";
import { useApi } from '../hooks/useApi';
import { endpoints } from '../services/api';

const StatsGrid = ({ title, data = [], valueKey, showPlayer = false }) => (
  <Card>
    <CardHeader>
      <CardTitle>{title}</CardTitle>
    </CardHeader>
    <CardContent>
      <div className="space-y-4">
        {data.map((item, index) => (
          <div key={index} className="flex items-center justify-between p-2 bg-gray-50 rounded-lg">
            <div className="flex items-center gap-3">
              <div className="flex-shrink-0 text-sm font-medium text-gray-500">{index + 1}</div>
              <div>
                {showPlayer ? (
                  <>
                    <div className="font-medium">{item.name}</div>
                    <div className="text-sm text-gray-500">{item.club || ''}</div>
                  </>
                ) : (
                  <>
                    <div className="font-medium">{item.name}</div>
                    <div className="text-sm text-gray-500">{item.location || ''}</div>
                  </>
                )}
              </div>
            </div>
            <div className="text-2xl font-bold">{item[valueKey] || 0}</div>
          </div>
        ))}
        <button className="w-full text-sm text-gray-500 hover:text-gray-700">View Full List →</button>
      </div>
    </CardContent>
  </Card>
);

const DashboardView = () => {
  const { data: dashboardData, loading, error } = useApi(endpoints.dashboard);

  if (loading) return (
    <div className="flex items-center justify-center h-64">
      <Loader2 className="h-8 w-8 animate-spin" />
    </div>
  );

  if (error) return (
    <Alert variant="destructive">
      <AlertDescription>{error}</AlertDescription>
    </Alert>
  );

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Season 2024/25 Stats</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <StatsGrid 
          title="Top Scorers" 
          data={dashboardData?.player_stats?.top_scorers || []}
          valueKey="goals"
          showPlayer={true}
        />
        
        <StatsGrid 
          title="Most Assists" 
          data={dashboardData?.player_stats?.top_assisters || []}
          valueKey="assists"
          showPlayer={true}
        />
        
        <StatsGrid 
          title="Most Wins" 
          data={dashboardData?.club_stats?.most_wins || []}
          valueKey="wins"
          showPlayer={false}
        />
        
        <StatsGrid 
          title="Most Clean Sheets" 
          data={dashboardData?.player_stats?.most_clean_sheets || []}
          valueKey="clean_sheets"
          showPlayer={true}
        />
      </div>
    </div>
  );
};

export default DashboardView;
