import React, { useState, useEffect } from 'react';
import { fetchClubs } from '../services/api';

const ClubStats = () => {
  const [clubs, setClubs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchClubs()
      .then(setClubs)
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>Club Stats</h1>
      <ul>
        {clubs.map(club => (
          <li key={club.id}>
            <strong>{club.name}</strong> - Location: {club.location}
            <ul>
              <li>Wins: {club.stats?.wins}</li>
              <li>Losses: {club.stats?.losses}</li>
              <li>Goals: {club.stats?.goals}</li>
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ClubStats;
