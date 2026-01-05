import API from './api';

export const studentService = {
    getAll: () => API.get('students/'),
    getById: (id) => API.get(`students/${id}/`),
    create: (data) => API.post('students/', data),
    update: (id, data) => API.put(`students/${id}/`, data),
    delete: (id) => API.delete(`students/${id}/`),
};
