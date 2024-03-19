import React, { useEffect, useState } from 'react';
import '../styles/RoundClock.css'
import clockFace from '../img/clockFace.png';
import clockFace2 from '../img/clockFace2.png'; // Add the second clock face image



function DigitalClock() {
  const [date, setDate] = useState(new Date());
  const [clockFaceImage, setClockFaceImage] = useState(clockFace); 

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

  // Clock numbers for SVG
  const num = ['・','・','・','・','・','・','・','・','・','・','・','・']
  const clockNumbers = ['・','・','・','・','・','・','・','・','・','・','・','・'].map((number, index) => {
    const angle = Math.PI / 6 * (index - 2); // Calculate the angle for the number position
    const x = 100 + 90 * Math.cos(angle); // Calculate the x position
    const y = 100 + 90 * Math.sin(angle); // Calculate the y position
    return (
      <text x={x} y={y} textAnchor="middle" alignmentBaseline="central" fill="black" fontSize="30" fontFamily="sans-serif">
        {number}
      </text>
    );
  });

  // Event handler for mouse move
  const handleMouseMove = () => {
    setClockFaceImage(clockFace2); // Update the clockFaceImage state with the second clock face image
  };

  // Event handler for mouse leave
  const handleMouseLeave = () => {
    setClockFaceImage(clockFace); // Reset the clockFaceImage state to the original clock face image
  };

  return (
    <svg
      width="200"
      height="200"
      viewBox="0 0 200 200"
      onMouseMove={handleMouseMove} 
      onMouseLeave={handleMouseLeave} 
    >
      {/* Clock Face */}
      <circle className="clock-face" cx="100" cy="100" r="95" />
      <image href={clockFaceImage} x="2" y="2" height="200" width="200" /> {/* Use clockFaceImage state */}
      {/* Clock Numbers */}
      {clockNumbers}
      {/* Clock Button Text */}
      <text
        x="100"
        y="120"
        textAnchor="middle"
        fill="rgba(160,160,160,255)"
        fontSize="60"
        fontFamily="Arial"
        fontWeight="bold"
        pointerEvents="none"
      >
        ADD
      </text>
      {/* Clock Pointer */}
      <line
        className="hour-hand"
        x1="100"
        y1="100"
        x2="100"
        y2="50"
        transform={`rotate(${hoursDegrees} 100 100)`}
      />
      <line
        className="minute-hand"
        x1="100"
        y1="100"
        x2="100"
        y2="30"
        transform={`rotate(${minutesDegrees} 100 100)`}
      />
      <line
        className="second-hand"
        x1="100"
        y1="100"
        x2="100"
        y2="28"
        transform={`rotate(${secondsDegrees} 100 100)`}
      />
      <circle cx="100" cy="100" r="3" fill="#000000" />
    </svg>
  );
}

export default DigitalClock;
