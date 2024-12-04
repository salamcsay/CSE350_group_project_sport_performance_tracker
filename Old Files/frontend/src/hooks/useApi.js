import { useState, useEffect } from 'react';
import { fetchApi } from '@/services/api';
import { apiService } from '../services/api';
import { api } from '../services/api';


export const useApi = (endpoint, options = {}) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [params, setParams] = useState(options.params || {});

  const fetchData = async () => {
    try {
      setLoading(true);
      const response = await api.get(endpoint, { ...options, params });
      setData(response.data);
      setError(null);
    } catch (err) {
      setError(err.message);
      setData(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, [endpoint, JSON.stringify(params)]);

  const refetch = () => fetchData();
  
  return { 
    data, 
    loading, 
    error, 
    setParams,
    refetch,
    isLoading: loading,
    isError: !!error,
    isSuccess: !loading && !error && data !== null
  };
};