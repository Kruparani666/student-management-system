import API from './api';

export const authService = {
    login: async (username, password) => {
        const response = await API.post('auth/login/', { username, password });
        if (response.data.token) {
            localStorage.setItem('token', response.data.token);
            localStorage.setItem('user', JSON.stringify(response.data.user));
        }
        return response.data;
    },

    register: async (userData) => {
        const response = await API.post('auth/register/', userData);
        if (response.data.token) {
            localStorage.setItem('token', response.data.token);
            localStorage.setItem('user', JSON.stringify(response.data.user));
        }
        return response.data;
    },

    logout: () => {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        API.post('auth/logout/');
    },

    getCurrentUser: () => {
        const user = localStorage.getItem('user');
        return user ? JSON.parse(user) : null;
    },

    // This should return a boolean directly
    isAuthenticated: () => {
        return localStorage.getItem('token') !== null;
    },

    isAdmin: () => {
        const user = JSON.parse(localStorage.getItem('user'));
        return user && user.role === 'admin';
    }
};