import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

const PrivateRoute = ({ children, adminOnly = false }) => {
    const { isAuthenticated, user } = useAuth(); // Get user from context

    if (!isAuthenticated) { // No parentheses - it's a boolean
        return <Navigate to="/login" />;
    }

    if (adminOnly && user?.role !== 'admin') {
        return <Navigate to="/dashboard" />;
    }

    return children;
};

export default PrivateRoute;