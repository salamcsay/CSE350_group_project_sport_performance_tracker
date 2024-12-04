import React, { useState, useEffect } from "react";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Plus } from "lucide-react";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { ScrollArea } from "@/components/ui/scroll-area";
import { ResponsiveContainer, PieChart, Pie, Cell, Legend, Tooltip } from 'recharts';
import { api } from "@/services/api";

const COLORS = ['#22c55e', '#f97316', '#3b82f6', '#eab308', '#ef4444']; // green, orange, blue, yellow, red

const PlayerComparisonView = () => {
  const [players, setPlayers] = useState([null, null]);
  const [availablePlayers, setAvailablePlayers] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPlayers = async () => {
      try {
        setIsLoading(true);
        setError(null);
        const response = await api.get('/players/');
        console.log('Available players:', response.data.results);
        setAvailablePlayers(response.data.results || []);
      } catch (err) {
        console.error("Error fetching players:", err);
        setError("Failed to fetch players");
      } finally {
        setIsLoading(false);
      }
    };

    fetchPlayers();
  }, []);

  const handlePlayerSelect = (value, index) => {
    const selectedPlayer = availablePlayers.find(p => p.id.toString() === value);
    const updatedPlayers = [...players];
    updatedPlayers[index] = selectedPlayer;
    setPlayers(updatedPlayers);
  };

  const getStatsForPosition = (player) => {
    if (!player?.stats) return [];
    
    switch (player.position) {
      case 'GK':
        return [
          { name: 'Clean Sheets', value: player.stats.clean_sheets },
          { name: 'Goals Conceded', value: player.stats.goals_conceded },
          { name: 'Saves', value: player.stats.saves },
          { name: 'Goal Kicks', value: player.stats.goal_kicks },
          { name: 'High Claims', value: player.stats.high_claims }
        ];
      case 'DF':
        return [
          { name: 'Tackles', value: player.stats.tackles },
          { name: 'Passes', value: player.stats.passes },
          { name: 'Clean Sheets', value: player.stats.clean_sheets },
          { name: 'Goals', value: player.stats.goals },
          { name: 'Appearances', value: player.stats.appearances }
        ];
      case 'MF':
        return [
          { name: 'Passes', value: player.stats.passes },
          { name: 'Assists', value: player.stats.assists },
          { name: 'Shots', value: player.stats.shots },
          { name: 'Tackles', value: player.stats.tackles },
          { name: 'Goals', value: player.stats.goals }
        ];
      case 'FW':
        return [
          { name: 'Goals', value: player.stats.goals },
          { name: 'Shots', value: player.stats.shots },
          { name: 'Assists', value: player.stats.assists },
          { name: 'Passes', value: player.stats.passes },
          { name: 'Shots on Target', value: player.stats.shots_on_target }
        ];
      default:
        return [];
    }
  };

  const getStatsToCompare = (player1, player2) => {
    if (!player1 || !player2 || player1.position !== player2.position) return [];
    
    switch (player1.position) {
      case "GK":
        return [
          { label: "Clean Sheets", key: "clean_sheets" },
          { label: "Goals Conceded", key: "goals_conceded" },
          { label: "Saves", key: "saves" },
          { label: "Goal Kicks", key: "goal_kicks" },
          { label: "High Claims", key: "high_claims" },
        ];
      case "DF":
        return [
          { label: "Tackles", key: "tackles" },
          { label: "Passes", key: "passes" },
          { label: "Clean Sheets", key: "clean_sheets" },
          { label: "Goals", key: "goals" },
          { label: "Appearances", key: "appearances" },
        ];
      case "MF":
        return [
          { label: "Passes", key: "passes" },
          { label: "Assists", key: "assists" },
          { label: "Shots", key: "shots" },
          { label: "Tackles", key: "tackles" },
          { label: "Goals", key: "goals" },
        ];
      case "FW":
        return [
          { label: "Goals", key: "goals" },
          { label: "Shots", key: "shots" },
          { label: "Assists", key: "assists" },
          { label: "Passes", key: "passes" },
          { label: "Shots on Target", key: "shots_on_target" },
        ];
      default:
        return [];
    }
  };

  const renderPlayerChart = (player) => {
    if (!player) return null;

    const stats = getStatsForPosition(player);
    const total = stats.reduce((sum, item) => sum + (item.value || 0), 0);
    const dataWithPercentages = stats.map(item => ({
      ...item,
      percentage: ((item.value / total) * 100).toFixed(1)
    }));

    return (
      <div className="h-[300px]">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={dataWithPercentages}
              dataKey="value"
              nameKey="name"
              cx="50%"
              cy="50%"
              outerRadius={100}
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
    );
  };

  const renderComparison = () => {
    const [player1, player2] = players;
    if (!player1 || !player2) return null;

    if (player1.position !== player2.position) {
      return (
        <Card className="mt-6">
          <CardContent className="pt-6">
            <div className="text-center text-red-500">
              Cannot compare players of different positions
            </div>
          </CardContent>
        </Card>
      );
    }

    const statsToCompare = getStatsToCompare(player1, player2);

    return (
      <Card className="mt-6">
        <CardContent className="pt-6">
          <div className="grid grid-cols-3 gap-8">
            {/* Left player chart */}
            <div>
              {renderPlayerChart(player1)}
            </div>

            {/* Center stats comparison */}
            <div className="space-y-4">
              {statsToCompare.map(({ label, key }) => (
                <div key={key} className="grid grid-cols-3 gap-4 items-center">
                  <div className="text-right font-medium">{player1.stats?.[key] || "N/A"}</div>
                  <div className="text-center text-sm text-gray-500">{label}</div>
                  <div className="text-left font-medium">{player2.stats?.[key] || "N/A"}</div>
                </div>
              ))}
            </div>

            {/* Right player chart */}
            <div>
              {renderPlayerChart(player2)}
            </div>
          </div>
        </CardContent>
      </Card>
    );
  };

  const PlayerSelectContent = () => (
    <SelectContent>
      <ScrollArea className="h-[200px] w-full">
        <div className="p-1">
          {availablePlayers.map((player) => (
            <SelectItem 
              key={player.id} 
              value={player.id.toString()}
              className="cursor-pointer"
            >
              <div className="flex flex-col py-1">
                <span className="font-medium">{player.name}</span>
                <span className="text-sm text-muted-foreground">
                  {player.position} · {player.club?.name || "No Club"}
                </span>
              </div>
            </SelectItem>
          ))}
        </div>
      </ScrollArea>
    </SelectContent>
  );

  if (error) {
    return (
      <div className="text-center text-red-500">
        Error loading players: {error}
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Player Comparison</h1>

      <div className="grid grid-cols-2 gap-6">
        {[0, 1].map((index) => (
          <Card key={index} className="relative min-h-[200px]">
            {!players[index] ? (
              <Select onValueChange={(value) => handlePlayerSelect(value, index)}>
                <SelectTrigger className="absolute inset-0 h-full justify-center border-2 border-dashed">
                  <div className="flex items-center">
                    <Plus className="mr-2 h-4 w-4" />
                    Add Player
                  </div>
                </SelectTrigger>
                <PlayerSelectContent />
              </Select>
            ) : (
              <CardContent className="pt-6">
                <div className="text-center">
                  <h2 className="text-xl font-bold">{players[index].name}</h2>
                  <p className="text-gray-500">
                    {players[index].position} · {players[index].club?.name || "No Club"}
                  </p>
                </div>
                <Select 
                  onValueChange={(value) => handlePlayerSelect(value, index)}
                  defaultValue={players[index].id.toString()}
                >
                  <SelectTrigger className="absolute top-2 right-2 w-24">
                    Change
                  </SelectTrigger>
                  <PlayerSelectContent />
                </Select>
              </CardContent>
            )}
          </Card>
        ))}
      </div>

      {renderComparison()}
    </div>
  );
};

export default PlayerComparisonView;