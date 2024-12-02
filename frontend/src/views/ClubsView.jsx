import React, { useState, useEffect } from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Alert, AlertDescription } from "@/components/ui/alert"
import { Loader2 } from "lucide-react"

const ClubsView = () => {
  const [clubs, setClubs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState('');
  const [sortColumn, setSortColumn] = useState('name');
  const [sortDirection, setSortDirection] = useState('asc');

  useEffect(() => {
    const fetchClubs = async () => {
      try {
        const url = `/api/clubs/?search=${search}&ordering=${sortDirection === 'desc' ? '-' : ''}${sortColumn}`;
        const response = await fetch(url);
        if (!response.ok) throw new Error('Failed to fetch clubs');
        const data = await response.json();
        setClubs(data.results);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchClubs();
  }, [search, sortColumn, sortDirection]);

  const handleSort = (column) => {
    setSortDirection(sortColumn === column && sortDirection === 'asc' ? 'desc' : 'asc');
    setSortColumn(column);
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <Loader2 className="h-8 w-8 animate-spin" />
      </div>
    );
  }

  if (error) {
    return (
      <Alert variant="destructive">
        <AlertDescription>{error}</AlertDescription>
      </Alert>
    );
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle>Clubs</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="mb-6">
          <Input
            placeholder="Search clubs..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="max-w-sm"
          />
        </div>

        <div className="rounded-md border">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead className="cursor-pointer" onClick={() => handleSort('name')}>
                  Name
                </TableHead>
                <TableHead className="cursor-pointer" onClick={() => handleSort('location')}>
                  Location
                </TableHead>
                <TableHead className="cursor-pointer" onClick={() => handleSort('stats__wins')}>
                  Wins
                </TableHead>
                <TableHead className="cursor-pointer" onClick={() => handleSort('stats__goals')}>
                  Goals
                </TableHead>
                <TableHead className="cursor-pointer" onClick={() => handleSort('win_percentage')}>
                  Win Rate
                </TableHead>
                <TableHead className="cursor-pointer" onClick={() => handleSort('goals_per_game')}>
                  Goals/Game
                </TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {clubs.map((club) => (
                <TableRow key={club.id}>
                  <TableCell>{club.name}</TableCell>
                  <TableCell>{club.location}</TableCell>
                  <TableCell>{club.stats.wins}</TableCell>
                  <TableCell>{club.stats.goals}</TableCell>
                  <TableCell>{club.win_percentage}%</TableCell>
                  <TableCell>{club.goals_per_game}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      </CardContent>
    </Card>
  );
};

export default ClubsView;