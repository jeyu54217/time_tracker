import React, { useState } from 'react';
import RoundClock from './RoundClock';
import  {Btn30Min, BtnContinue, GoogleLoginButton}  from './Button';
import '../styles/TaskForm.css'; 




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
            setTaskOptions([
                'CS', 
                'English', 
                'Other',
            ]);
        } else if (selectedTaskType === 'Break') {
            setTaskOptions([
                'Chores', 
                'Traveling', 
                'Shopping', 
                'Socializing', 
                'Photography', 
                'Music', 
                'Reading', 
                'Media', 
                'Gaming', 
                'Other',
            ]);
        } else if (selectedTaskType === 'Sport') {
            setTaskOptions([
                'GYM', 
                'Cycling', 
                'Break 3'
            ]);
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
        <div>
            <div className="container-sm custom-bg-color rounded-5" >
                <br />
                <form className="form-body" onSubmit={handleSubmit}>
                    <div className="row ">
                        <div className="col-md-5 mx-auto">
                            <br />
                            <div className="row justify-content-md-center">
                                {/* Date Input */}
                                <div className="col-md-4 custom-column">
                                    <label className="form-label rounded-3">Date</label>
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
                                <div className="col-md-4 custom-column">
                                    <label className="form-label rounded-3" >Start Time</label>
                                    <input
                                        type="time"
                                        className="form-control"
                                        placeholder="Start Time"
                                        name="startTime"
                                        value={formValues.startTime}
                                        onChange={(event) => {
                                            const { value } = event.target;
                                            setFormValues((prevFormValues) => ({
                                                ...prevFormValues,
                                                startTime: value,
                                                endTime: '' // Reset the end time when start time changes
                                            }));
                                        }}
                                    />
                                </div>
                                {/* End Time Inputs */}
                                <div className="col-md-4 custom-column">
                                    <label className="form-label rounded-3">End Time</label>
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

                            <div className="row justify-content-end">
                                {/* Continue Button */}
                                <div className="col-md-4">
                                    <button
                                        className="btnBox"
                                        onClick={() => {
                                            if (formValues.endTime) {
                                                setFormValues((prevFormValues) => ({
                                                    ...prevFormValues,
                                                    startTime: formValues.endTime
                                                }));
                                            }
                                        }}>
                                        <BtnContinue />
                                    </button>
                                </div>

                                {/* Add 30 Minutes Button */}
                                <div className="col-md-3 custom-column">
                                    <button
                                        className="btnBox"
                                        onClick={() => {
                                            const startTime = new Date(`2000-01-01T${formValues.startTime}`);
                                            let newEndTime;

                                            if (!formValues.endTime) {
                                                newEndTime = new Date(startTime.getTime() + 30 * 60000);
                                            } else {
                                                const currentEndTime = new Date(`2000-01-01T${formValues.endTime}`);
                                                newEndTime = new Date(currentEndTime.getTime() + 30 * 60000);
                                            }
                                            const formattedEndTime = newEndTime.toTimeString().slice(0, 5);
                                            const hours = Math.floor(newEndTime.getTime() / (60 * 60 * 1000));
                                            const minutes = newEndTime.getMinutes();
                                            setFormValues((prevFormValues) => ({
                                                ...prevFormValues,
                                                endTime: formattedEndTime,
                                                hours: hours,
                                                minutes: minutes
                                            }));
                                        }}
                                    > 
                                        <Btn30Min />
                                    </button>
                                </div>
                            </div>

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
                                        <option value="Sport">Sport</option>
                                        {/* Add more task types here */}
                                    </select>
                                </div>
                                {/* Task Name Inputs */}
                                <div className="col-md-6">
                                    <select
                                        className="form-control"
                                        name="task"
                                        value={formValues.task}
                                        onChange={handleInputChange}>
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
                        <div className="col-md-2 custom-column justify-content-md-center">
                            <br />
                            <button className="btnBox" type="submit" onClick={handleSubmit}>
                                <RoundClock />
                            </button>
                        </div>
                        {/* Notes Input */}
                        <div className="col-md-5 justify-content-md-center">
                            <br />
                            <br />
                            <textarea
                                className="form-control rounded-4" 
                                placeholder="Notes..."
                                rows="6"
                                name="notes"
                                value={formValues.notes}
                                onChange={handleInputChange}
                            ></textarea>
                        </div>
                    </div>
                    <br />
                </form>
            </div>
            <GoogleLoginButton />
        </div>
    
    );
    }

    export default TaskForm;
