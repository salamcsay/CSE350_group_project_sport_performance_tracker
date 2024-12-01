import React, { useState } from 'react';
import { search } from '../services/api';
import '../styles/SearchFilter.css';

// Component that fetches and displays search results
const SearchFilter = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState({ players: [], clubs: [] });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = () => {
    setLoading(true);
    search(query)
      .then(data => setResults(data))
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  };

  return (
    <div>
      <h1>Search</h1>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search for players or clubs"
      />
      <button onClick={handleSearch}>Search</button>
      {loading && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}
      <div>
        <h2>Players</h2>
        <ul>
          {results.players.map(player => (
            <li key={player.id}>
              {player.name} ({player.club?.name})
            </li>
          ))}
        </ul>
        <h2>Clubs</h2>
        <ul>
          {results.clubs.map(club => (
            <li key={club.id}>
              {club.name} ({club.location})
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default SearchFilter;
