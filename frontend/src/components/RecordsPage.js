// src/components/RecordsPage.js

import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BtnFilter, BtnDel } from './ButtonImg';
import '../styles/RecordsPage.css';

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

function RecordsPage() {
    return (
        <div className="container-sm">

                <div className="filters">
                    <div className="row">
                        <div className="col-md-2">
                            <label className="form-label-record rounded-4">Start Date</label>
                            <input type="date" name="filterDate" className="form-control" />
                        </div>
                        <div className="col-md-2">
                            <label className="form-label-record rounded-4">End Date</label>
                            <input type="date" name="filterDate" className="form-control" />
                        </div>
                        <div className="col-md-2">
                            <label className="form-label-record rounded-4">Task Type</label>
                            <select name="filterTaskType" className="form-control">
                                <option value="">All Types</option>
                                {/* Add options here */}
                            </select>
                        </div>
                        <div className="col-md-2">
                            <label className="form-label-record rounded-4">Task Name</label>
                            <select name="filterTaskType" className="form-control">
                                <option value="">All Types</option>
                                {/* Add options here */}
                            </select>
                        </div>
                        <div className="col-md-4">
                            <div className="row justify-content-between">
                                <div className="col-md-3">
                                    <button className="btnAll" type="submit">
                                        <BtnFilter />
                                    </button>
                                </div>
                                <div className="col-md-3">
                                    <button className="btnAll" type="submit">
                                        <BtnDel />
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <br />
                <table className="table table-striped rounded-3 overflow-hidden">
                    <thead className="thead-dark">
                        <tr>
                            <th></th> {/* Add an empty header for the checkbox */}
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
                                <td>
                                    <input type="checkbox" name={`record-${index}`} />
                                </td> 
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

    );
}

export default RecordsPage;
