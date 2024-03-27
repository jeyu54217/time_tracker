import React from 'react';
import '../styles/HomePage.css';
import TaskForm from './TaskForm';
import RecordsPage from './RecordsPage';
import Navbar  from './Navbar';

function HomePage() {

    return (
        <div className="home-page">
            <Navbar />
            <div className="header text-center"> 
                <h1>Log New Task</h1>
            </div>
            <TaskForm />

            <div className="header text-center"> 
                <h1>Records</h1>
            </div>
            <RecordsPage />

        </div>
    );
}

export default HomePage;
