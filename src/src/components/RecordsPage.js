// src/components/RecordsPage.js

import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function RecordsPage() {
    // Assume records is fetched from state or props
    const records = [
        {
            date: '2022-01-01',
            startTime: '09:00 AM',
            endTime: '10:30 AM',
            taskType: 'Meeting',
            taskName: 'Project Kickoff',
            taskNote: 'Discuss project goals and deliverables',
        },
        {
            date: '2022-01-02',
            startTime: '02:00 PM',
            endTime: '03:30 PM',
            taskType: 'Development',
            taskName: 'Implement Login Page',
            taskNote: 'Work on UI and functionality',
        },
        // Add more test records here
    ];

    return (
        <div className="container d-flex justify-content-center">
            <div className="records-page">
                <h1>Task Records</h1>
                <div className="filters">
                    <input type="date" name="filterDate" className="form-control" />
                    <select name="filterTaskType" className="form-control">
                        <option value="">All Types</option>
                        {/* Add options here */}
                    </select>
                    <input type="text" name="filterTaskName" placeholder="Task Name" className="form-control" />
                    <button className="btn btn-primary">Filter</button>
                </div>
                <table className="table">
                    <thead className="thead-dark">
                        <tr>
                            <th>Date</th>
                            <th>Start Time</th>
                            <th>End Time</th>
                            <th>Task Type</th>
                            <th>Task Name</th>
                            <th>Notes</th>
                        </tr>
                    </thead>
                    <tbody>
                        {records.map((record, index) => (
                            <tr key={index}>
                                <td>{record.date}</td>
                                <td>{record.startTime}</td>
                                <td>{record.endTime}</td>
                                <td>{record.taskType}</td>
                                <td>{record.taskName}</td>
                                <td>{record.taskNote}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default RecordsPage;
