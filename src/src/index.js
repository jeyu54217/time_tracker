import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/index.css';
import App from './routes';
import 'bootstrap/dist/css/bootstrap.min.css';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);


// ReactDOM.createRoot() is part of the new concurrent mode in React. 
// Concurrent mode allows React to interrupt a long-running render to handle a high-priority event. 
// If you're not using concurrent mode, you would use ReactDOM.render() instead.