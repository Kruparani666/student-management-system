import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Login from './components/auth/Login';
import Register from './components/auth/Register';
import StudentList from './components/students/StudentList';

// Simple Navbar
const Navbar = () => (
    <nav className="navbar navbar-dark bg-dark">
        <div className="container">
            <span className="navbar-brand">📚 Student Management System</span>
            <div>
                <a href="/login" className="text-white me-3" style={{ textDecoration: 'none' }}>Login</a>
                <a href="/register" className="text-white" style={{ textDecoration: 'none' }}>Register</a>
            </div>
        </div>
    </nav>
);

function App() {
    return (
        <Router>
            <div className="App">
                <Navbar />
                <Routes>
                    <Route path="/login" element={<Login />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/students" element={<StudentList />} />
                    <Route path="/" element={<Navigate to="/login" />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;