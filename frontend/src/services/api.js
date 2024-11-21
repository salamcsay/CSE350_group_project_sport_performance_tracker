import axios from 'axios';

const BASE_URL = 'http://localhost:8000'; 

export const fetchPlayers = async (filters = {}) => {
  const params = new URLSearchParams(filters).toString();
  const response = await axios.get(`${BASE_URL}/api/players/?${params}`);
  return response.data;
};

export const fetchPlayerStats = async (id) => {
  const response = await axios.get(`${BASE_URL}/api/players/${id}/stats/`);
  return response.data;
};

export const fetchClubs = async (filters = {}) => {
  const params = new URLSearchParams(filters).toString();
  const response = await axios.get(`${BASE_URL}/api/clubs/?${params}`);
  return response.data;
};

export const fetchClubStats = async (id) => {
  const response = await axios.get(`${BASE_URL}/api/clubs/${id}/stats/`);
  return response.data;
};

export const fetchDashboardData = async () => {
  const response = await axios.get(`${BASE_URL}/api/dashboard/`);
  return response.data;
};

export const search = async (query) => {
  const response = await axios.get(`${BASE_URL}/api/search/?q=${query}`);
  return response.data;
};
