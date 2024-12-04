import React from 'react';
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { ResponsiveContainer, PieChart, Pie, Cell, Legend, Tooltip } from 'recharts';

const COLORS = ['#22c55e', '#f97316', '#3b82f6', '#eab308', '#ef4444',]; // green, blue, yellow, red, orange

const PlayerDetailView = ({ player }) => {
  if (!player) return null;

  const getStatsForPosition = () => {
    const stats = player.stats;
    switch (player.position) {
      case 'GK':
        return [
          { name: 'Clean Sheets', value: stats.clean_sheets },
          { name: 'Goals Conceded', value: stats.goals_conceded },
          { name: 'Saves', value: stats.saves },
          { name: 'Goal Kicks', value: stats.goal_kicks },
          { name: 'High Claims', value: stats.high_claims }
        ];
      case 'DF':
        return [
          { name: 'Tackles', value: stats.tackles },
          { name: 'Passes', value: stats.passes },
          { name: 'Clean Sheets', value: stats.clean_sheets },
          { name: 'Goals', value: stats.goals },
          { name: 'Appearances', value: stats.appearances }
        ];
      case 'MF':
        return [
          { name: 'Passes', value: stats.passes },
          { name: 'Assists', value: stats.assists },
          { name: 'Shots', value: stats.shots },
          { name: 'Tackles', value: stats.tackles },
          { name: 'Goals', value: stats.goals }
        ];
      case 'FW':
        return [
          { name: 'Goals', value: stats.goals },
          { name: 'Shots', value: stats.shots },
          { name: 'Assists', value: stats.assists },
          { name: 'Passes', value: stats.passes },
          { name: 'Shots on Target', value: stats.shots_on_target }
        ];
      default:
        return [];
    }
  };

  const stats = getStatsForPosition();
  const total = stats.reduce((sum, item) => sum + item.value, 0);
  const dataWithPercentages = stats.map(item => ({
    ...item,
    percentage: ((item.value / total) * 100).toFixed(1)
  }));

  return (
    <Card className="mt-6">
      <CardHeader>
        <CardTitle className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold">{player.name}</h2>
            <p className="text-gray-500">{player.position} · {player.club?.name}</p>
          </div>
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="h-[400px]">
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={dataWithPercentages}
                dataKey="value"
                nameKey="name"
                cx="50%"
                cy="50%"
                outerRadius={150}
                label={({ name, percentage }) => `${name}: ${percentage}%`}
              >
                {dataWithPercentages.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </CardContent>
    </Card>
  );
};

export default PlayerDetailView;