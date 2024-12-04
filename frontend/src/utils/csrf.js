// src/utils/csrf.js
export const getCsrfToken = async () => {
    const response = await fetch('/api/auth/csrf/', {
      method: 'GET',
      credentials: 'include',
    });
    const data = await response.json();
    return data.csrfToken;
  };