import React, { useState } from 'react';
import RoundClock from './RoundClock';
import '../styles/TaskForm.css'; // Make sure this points to your CSS file

function TaskForm() {
    const [taskType, setTaskType] = useState('');
    const [taskOptions, setTaskOptions] = useState([]);
    const [formValues, setFormValues] = useState({
        date: new Date().toISOString().split('T')[0],
        startTime: '',
        endTime: '',
        task: '',
        notes: ''
    });

    const handleTaskTypeChange = (event) => {
        const selectedTaskType = event.target.value;
        setTaskType(selectedTaskType);

        // Update the task options based on the selected task type
        if (selectedTaskType === 'Work') {
            setTaskOptions(['CS', 'English', 'Other']);
        } else if (selectedTaskType === 'Break') {
            setTaskOptions(['Photography', 'Break 2', 'Break 3']);
        } else if (selectedTaskType === 'Sport') {
            setTaskOptions(['Break 1', 'Break 2', 'Break 3']);
        } else {
            setTaskOptions([]);
        }
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        // Handle form submission logic here
        console.log(formValues); // Access the form values from the state variable
    };

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setFormValues((prevFormValues) => ({
            ...prevFormValues,
            [name]: value
        }));
    };

    return (
        <div className="container-fluid custom-bg-color container-lg">
            <br />
            <form onSubmit={handleSubmit}>
                <div className="row ">
                    <div className="col-md-5">
                        <br />
                        <div className="row justify-content-md-center">
                            {/* Date Input */}
                            <div className="col-md-4">
                                <label className="form-label">Date</label>
                                <input
                                    type="date"
                                    className="form-control"
                                    placeholder="Date"
                                    name="date"
                                    value={formValues.date}
                                    onChange={handleInputChange}
                                />
                            </div>
                            {/* Start Time Inputs */}
                            <div className="col-md-4">
                                <label className="form-label">Start Time</label>
                                <input
                                    type="time"
                                    className="form-control"
                                    placeholder="Start Time"
                                    name="startTime"
                                    value={formValues.startTime}
                                    onChange={handleInputChange}
                                />
                            </div>
                            {/* End Time Inputs */}
                            <div className="col-md-4">
                                <label className="form-label">End Time</label>
                                <input
                                    type="time"
                                    className="form-control"
                                    placeholder="End Time"
                                    name="endTime"
                                    value={formValues.endTime}
                                    onChange={handleInputChange}
                                />
                            </div>
                        </div>
                        <br />
                        <div className="row justify-content-md-center">
                            {/* Task Type Inputs */}
                            <div className="col-md-6">
                                <select
                                    className="form-control"
                                    value={taskType}
                                    onChange={handleTaskTypeChange}
                                    name="taskType"
                                >
                                    <option value="">Select Task Type...</option>
                                    <option value="Work">Work</option>
                                    <option value="Break">Break</option>
                                    {/* Add more task types here */}
                                </select>
                            </div>
                            {/* Task Name Inputs */}
                            <div className="col-md-6">
                                <select
                                    className="form-control"
                                    name="task"
                                    value={formValues.task}
                                    onChange={handleInputChange}
                                >
                                    <option value="">Select Task...</option>
                                    {taskOptions.map((option) => (
                                        <option key={option} value={option}>
                                            {option}
                                        </option>
                                    ))}
                                </select>
                            </div>
                        </div>
                        <br />
                    </div>
                    {/* RoundClock */}
                    <div className="col-md-2 justify-content-md-center">
                        <button type="submit" onClick={handleSubmit} className="RoundClockButton">
                            <RoundClock />
                        </button>
                    </div>
                    {/* Notes Input */}
                    <div className="col-md-5 justify-content-md-center">
                        <br />
                        <br />
                        <textarea
                            className="form-control"
                            placeholder="Notes..."
                            rows="5"
                            name="notes"
                            value={formValues.notes}
                            onChange={handleInputChange}
                        ></textarea>
                    </div>
                </div>
            </form>
        </div>
    );
}

export default TaskForm;
