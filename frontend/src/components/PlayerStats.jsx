import React, { useState, useEffect } from 'react';
import { fetchPlayers } from '../services/api';

// Component that fetches and displays player stats
const PlayerStats = () => {
  const [players, setPlayers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchPlayers()
      .then(data => setPlayers(data))
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>Player Stats</h1>
      <ul>
        {players.map(player => (
          <li key={player.id}>
            <strong>{player.name}</strong> ({player.position}) - Club: {player.club?.name}
            <ul>
              <li>Goals: {player.stats?.goals}</li>
              <li>Assists: {player.stats?.assists}</li>
              <li>Appearances: {player.stats?.appearances}</li>
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PlayerStats;
