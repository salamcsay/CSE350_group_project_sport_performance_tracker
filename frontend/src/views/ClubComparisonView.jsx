// frontend/src/views/ClubComparisonView.jsx
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

const COLORS = ['#22c55e', '#ef4444']; // green, red

const ClubComparisonView = () => {
  const [clubs, setClubs] = useState([null, null]);
  const [availableClubs, setAvailableClubs] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchClubs = async () => {
      try {
        setIsLoading(true);
        setError(null);
        const response = await api.get('/clubs/');
        console.log('Available clubs:', response.data.results);
        setAvailableClubs(response.data.results || []);
      } catch (err) {
        console.error("Error fetching clubs:", err);
        setError("Failed to fetch clubs");
      } finally {
        setIsLoading(false);
      }
    };

    fetchClubs();
  }, []);

  const handleClubSelect = (value, index) => {
    const selectedClub = availableClubs.find(c => c.id.toString() === value);
    const updatedClubs = [...clubs];
    updatedClubs[index] = selectedClub;
    setClubs(updatedClubs);
  };

  const getStatsToCompare = (club1, club2) => {
    if (!club1 || !club2) return [];
    
    return [
      { label: "Wins", key: "wins" },
      { label: "Losses", key: "losses" },
      { label: "Goals", key: "goals" },
      { label: "Clean Sheets", key: "clean_sheets" },
      { label: "Tackles", key: "tackles" },
    ];
  };

  const renderClubChart = (club) => {
    if (!club) return null;
  
    const stats = [
      { name: 'Wins', value: club.stats.wins },
      { name: 'Losses', value: club.stats.losses }
    ];
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
              labelLine={false}
            >
              {dataWithPercentages.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
        <div className="text-center mt-4">
          <h2 className="text-xl font-bold">{club.name}</h2>
        </div>
      </div>
    );
  };

  const renderComparison = () => {
    const [club1, club2] = clubs;
    if (!club1 || !club2) return null;

    const statsToCompare = getStatsToCompare(club1, club2);

    return (
      <Card className="mt-6">
        <CardContent className="pt-6">
          <div className="grid grid-cols-3 gap-8">
            {/* Left club chart */}
            <div>
              {renderClubChart(club1)}
            </div>

            {/* Center stats comparison */}
            <div className="space-y-4">
              {statsToCompare.map(({ label, key }) => (
                <div key={key} className="grid grid-cols-3 gap-4 items-center">
                  <div className="text-right font-medium">{club1.stats?.[key] || "N/A"}</div>
                  <div className="text-center text-sm text-gray-500">{label}</div>
                  <div className="text-left font-medium">{club2.stats?.[key] || "N/A"}</div>
                </div>
              ))}
            </div>

            {/* Right club chart */}
            <div>
              {renderClubChart(club2)}
            </div>
          </div>
        </CardContent>
      </Card>
    );
  };

  const ClubSelectContent = () => (
    <SelectContent>
      <ScrollArea className="h-[200px] w-full">
        <div className="p-1">
          {availableClubs.map((club) => (
            <SelectItem 
              key={club.id} 
              value={club.id.toString()}
              className="cursor-pointer"
            >
              <div className="flex flex-col py-1">
                <span className="font-medium">{club.name}</span>
                <span className="text-sm text-muted-foreground">
                  {club.location}
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
        Error loading clubs: {error}
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Club Comparison</h1>

      <div className="grid grid-cols-2 gap-6">
        {[0, 1].map((index) => (
          <Card key={index} className="relative min-h-[200px]">
            {!clubs[index] ? (
              <Select onValueChange={(value) => handleClubSelect(value, index)}>
                <SelectTrigger className="absolute inset-0 h-full justify-center border-2 border-dashed">
                  <div className="flex items-center">
                    <Plus className="mr-2 h-4 w-4" />
                    Add Club
                  </div>
                </SelectTrigger>
                <ClubSelectContent />
              </Select>
            ) : (
              <CardContent className="pt-6">
                <div className="text-center">
                  <h2 className="text-xl font-bold">{clubs[index].name}</h2>
                  <p className="text-gray-500">
                    {clubs[index].location}
                  </p>
                </div>
                <Select 
                  onValueChange={(value) => handleClubSelect(value, index)}
                  defaultValue={clubs[index].id.toString()}
                >
                  <SelectTrigger className="absolute top-2 right-2 w-24">
                    Change
                  </SelectTrigger>
                  <ClubSelectContent />
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

export default ClubComparisonView;