import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, Alert, Button, Table } from 'react-bootstrap';

const StudentList = () => {
    const [students, setStudents] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        const token = localStorage.getItem('token');
        
        if (!token) {
            navigate('/login');
            return;
        }

        // Fetch students from API
        fetch('http://127.0.0.1:8000/api/students/', {
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.status === 401) {
                localStorage.removeItem('token');
                localStorage.removeItem('user');
                navigate('/login');
                return;
            }
            return response.json();
        })
        .then(data => {
            setStudents(data);
            setLoading(false);
        })
        .catch(err => {
            setError('Failed to load students');
            setLoading(false);
        });
    }, [navigate]);

    const handleLogout = () => {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        navigate('/login');
    };

    if (loading) {
        return (
            <Container className="text-center mt-5">
                <div className="spinner-border" role="status">
                    <span className="visually-hidden">Loading...</span>
                </div>
                <p className="mt-2">Loading students...</p>
            </Container>
        );
    }

    return (
        <Container className="mt-4">
            <div className="d-flex justify-content-between align-items-center mb-4">
                <h1>Students Management</h1>
                <div>
                    <Button variant="primary" className="me-2" onClick={() => navigate('/students/new')}>
                        Add New Student
                    </Button>
                    <Button variant="outline-danger" onClick={handleLogout}>
                        Logout
                    </Button>
                </div>
            </div>

            {error && <Alert variant="danger">{error}</Alert>}

            {students.length === 0 ? (
                <Alert variant="info">
                    No students found. Add your first student!
                </Alert>
            ) : (
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>Student ID</th>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Phone</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {students.map((student) => (
                            <tr key={student.id}>
                                <td>{student.student_id}</td>
                                <td>{student.first_name} {student.last_name}</td>
                                <td>{student.email}</td>
                                <td>{student.phone}</td>
                                <td>
                                    <Button variant="info" size="sm" className="me-2">View</Button>
                                    <Button variant="warning" size="sm" className="me-2">Edit</Button>
                                    <Button variant="danger" size="sm">Delete</Button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </Table>
            )}
        </Container>
    );
};

export default StudentList;