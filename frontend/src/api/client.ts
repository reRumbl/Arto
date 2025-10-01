import axios from 'axios';

const api = axios.create({
	baseURL: `${window.location.protocol}//${window.location.hostname}:8000/api`
});

export default api;
