// src/components/HomePage.js

import React from 'react';
import TaskForm from './TaskForm';

function HomePage() {

    return (
        <div className="home-page">
            <div className="header text-center"> {/* Add 'text-center' class to center the header */}
                <h1>Log New Task</h1>
            </div>
            
            <TaskForm />

        </div>
    );
}

export default HomePage;
