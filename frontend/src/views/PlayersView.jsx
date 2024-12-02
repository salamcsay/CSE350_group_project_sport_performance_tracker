import React, { useState, useEffect } from 'react';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Input } from "@/components/ui/input"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Alert, AlertDescription } from "@/components/ui/alert"
import { Loader2 } from "lucide-react"
import { api } from '@/services/api';

const PlayersView = () => {
  const [players, setPlayers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState('');
  const [position, setPosition] = useState('all');
  const [sortColumn, setSortColumn] = useState('name');
  const [sortDirection, setSortDirection] = useState('asc');

  useEffect(() => {
    const fetchPlayers = async () => {
      try {
        const params = new URLSearchParams({
          search: search || '',
          ...(position !== 'all' && { position }),
          ordering: `${sortDirection === 'desc' ? '-' : ''}${sortColumn}`
        });
        
        const response = await api.get(`/players/?${params}`);
        setPlayers(response.data.results);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchPlayers();
  }, [search, position, sortColumn, sortDirection]);

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
        <CardTitle>Players</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="flex gap-4 mb-6">
          <Input
            placeholder="Search players..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="max-w-sm"
          />
          <Select value={position} onValueChange={setPosition}>
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Position" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All Positions</SelectItem>
              <SelectItem value="GK">Goalkeeper</SelectItem>
              <SelectItem value="DF">Defender</SelectItem>
              <SelectItem value="MF">Midfielder</SelectItem>
              <SelectItem value="FW">Forward</SelectItem>
            </SelectContent>
          </Select>
        </div>

        <div className="rounded-md border">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead className="cursor-pointer" onClick={() => handleSort('name')}>
                  Name
                </TableHead>
                <TableHead className="cursor-pointer" onClick={() => handleSort('club')}>
                  Club
                </TableHead>
                <TableHead>Position</TableHead>
                <TableHead className="cursor-pointer" onClick={() => handleSort('stats__goals')}>
                  Goals
                </TableHead>
                <TableHead className="cursor-pointer" onClick={() => handleSort('stats__assists')}>
                  Assists
                </TableHead>
                <TableHead className="cursor-pointer" onClick={() => handleSort('stats__appearances')}>
                  Appearances
                </TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {players.map((player) => (
                <TableRow key={player.id}>
                  <TableCell>{player.name}</TableCell>
                  <TableCell>{player.club.name}</TableCell>
                  <TableCell>{player.position}</TableCell>
                  <TableCell>{player.stats.goals}</TableCell>
                  <TableCell>{player.stats.assists}</TableCell>
                  <TableCell>{player.stats.appearances}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      </CardContent>
    </Card>
  );
};

export default PlayersView;