import React, { useEffect, useState } from 'react';
import '../styles/RoundClock.css'

function DigitalClock() {
  const [date, setDate] = useState(new Date());

  useEffect(() => {
    const timerId = setInterval(() => setDate(new Date()), 1000);
    return () => clearInterval(timerId);
  }, []);

  const secondsRatio = date.getSeconds() / 60;
  const minutesRatio = (secondsRatio + date.getMinutes()) / 60;
  const hoursRatio = (minutesRatio + date.getHours()) / 12;

  const secondsDegrees = secondsRatio * 360;
  const minutesDegrees = minutesRatio * 360;
  const hoursDegrees = hoursRatio * 360;

  // Generate clock numbers for SVG
  const clockNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map((number, index) => {
    const angle = Math.PI / 6 * (index - 2); // Calculate the angle for the number position
    const x = 100 + 80 * Math.cos(angle); // Calculate the x position
    const y = 100 + 80 * Math.sin(angle); // Calculate the y position
    return (
      <text x={x} y={y} textAnchor="middle" alignmentBaseline="central" fill="black" fontSize="18" fontFamily="sans-serif">
        {number}
      </text>
    );
  });

  return (
    <svg width="200" height="200" viewBox="0 0 200 200" >
        <circle className="clock-face" cx="100" cy="100" r="95" />
        {clockNumbers}
        <line className="hour-hand" x1="100" y1="100" x2="100" y2="50" transform={`rotate(${hoursDegrees} 100 100)`} />
        <line className="minute-hand" x1="100" y1="100" x2="100" y2="30" transform={`rotate(${minutesDegrees} 100 100)`} />
        <line className="second-hand" x1="100" y1="100" x2="100" y2="20" transform={`rotate(${secondsDegrees} 100 100)`} />
        <circle cx="100" cy="100" r="3" fill="#000000" />
        <text x="100" y="105" textAnchor="middle" fill="rgba(0, 0, 139, 0.5)" fontSize="30" fontFamily="Arial" fontWeight="bold" pointerEvents="none">
          SUBMIT
        </text>
      </svg>
    );
}

export default DigitalClock;


