import React, { useState, useEffect } from 'react';
import { fetchDashboardData } from '../services/api';

// Component that fetches and displays dashboard stats
const DashboardStats = () => {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchDashboardData()
      .then(setData)
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>Dashboard Overview</h1>
      <h2>Top Players</h2>
      <ul>
        {data.top_players?.map(player => (
          <li key={player.id}>
            {player.name} - {player.stats?.goals} goals
          </li>
        ))}
      </ul>
      <h2>Top Clubs</h2>
      <ul>
        {data.top_clubs?.map(club => (
          <li key={club.id}>
            {club.name} - {club.stats?.wins} wins
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DashboardStats;
