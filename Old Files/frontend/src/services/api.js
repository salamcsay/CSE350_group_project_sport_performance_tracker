import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api';

export const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true, // Required to send cookies with requests
});

// Request interceptor for API calls
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for API calls
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        const refreshToken = localStorage.getItem('refreshToken');
        const response = await api.post('/auth/refresh/', { refresh: refreshToken });
        const { access } = response.data;
        
        localStorage.setItem('token', access);
        originalRequest.headers.Authorization = `Bearer ${access}`;
        
        return api(originalRequest);
      } catch (err) {
        // Handle refresh token error (e.g., logout user)
        localStorage.removeItem('token');
        localStorage.removeItem('refreshToken');
        window.location.href = '/login';
      }
    }
    return Promise.reject(error);
  }
);

export const endpoints = {
  players: '/players/',
  clubs: '/clubs/',
  dashboard: '/dashboard/',
  playerStats: (id) => `/players/${id}/stats/`,
  clubStats: (id) => `/clubs/${id}/stats/`,
  search: '/search/',
};

// Add this new function to match the import in useApi.js
export const fetchApi = async (url, options = {}) => {
  const response = await api.get(url, options);
  return response.data;
};

export const apiService = {
  async getDashboard() {
    try {
      const response = await api.get(endpoints.dashboard);
      console.log('Dashboard:', response.data);
      return response.data;
    } catch (error) {
      console.error('Error fetching dashboard:', error);
      throw error;
    }
  },

  async getPlayers(params) {
    const response = await api.get(endpoints.players, { params });
    return response.data;
  },

  async getClubs(params) {
    const response = await api.get(endpoints.clubs, { params });
    return response.data;
  },

  async getPlayerStats(id) {
    const response = await api.get(endpoints.playerStats(id));
    return response.data;
  },

  async getClubStats(id) {
    const response = await api.get(endpoints.clubStats(id));
    return response.data;
  },

  async searchAll(query) {
    const response = await api.get(endpoints.search, { params: { q: query } });
    return response.data;
  }
};