import React, { useState, useEffect } from 'react';
import { fetchPlayers } from '../services/api';

// Component that fetches and displays player stats
const StatsList = () => {
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
            <strong>{player.name}</strong> - {player.stats?.goals} goals, {player.stats?.assists} assists
          </li>
        ))}
      </ul>
    </div>
  );
};

export default StatsList;
