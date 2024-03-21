import React, { useState } from 'react';
import '../styles/ButtonImg.css'; 
import btnBlue from '../img/btnBlue.png';
import btnBlue2 from '../img/btnBlue2.png';
import btnGray from '../img/btnGray.png';
import btnGray2 from '../img/btnGray2.png';
import btnRed from '../img/btnRed.png';
import btnDarkBlue from '../img/btnDarkBlue.png';
import btnDarkBlue2 from '../img/btnDarkBlue2.png';
// import btnGray from '../img/btnGray.png';


export function Btn30Min() {
    const [isHovered, setIsHovered] = useState(false);

    return (
        <div className='btnImgFrame' onMouseEnter={() => setIsHovered(true)} onMouseLeave={() => setIsHovered(false)}>
            <img className='btnImg' src={isHovered ? btnDarkBlue2 : btnDarkBlue} alt=""/>
            <span className='btnImgText'>+30min</span>
        </div>
    );
}

export function BtnContinue() {
    const [isHovered, setIsHovered] = useState(false);

    return (
        <div className='btnImgFrame' onMouseEnter={() => setIsHovered(true)} onMouseLeave={() => setIsHovered(false)}>
            <img className='btnImg' src={isHovered ? btnDarkBlue2 : btnDarkBlue} alt=""/>
            <span className='btnImgText'>Continue</span>
        </div>
    );
}

export function BtnFilter() {
    const [isHovered, setIsHovered] = useState(false);

    return (
        <div className='btnImgFrame' onMouseEnter={() => setIsHovered(true)} onMouseLeave={() => setIsHovered(false)}>
            <img className='btnImg' src={isHovered ? btnBlue2 : btnBlue} alt=""/>
            <span className='btnImgText'>Filter</span>
        </div>
    );
}

export function BtnDel() {
    const [isHovered, setIsHovered] = useState(false);

    return (
        <div className='btnImgFrame' onMouseEnter={() => setIsHovered(true)} onMouseLeave={() => setIsHovered(false)}>
            <img className='btnImg' src={isHovered ? btnDarkBlue2 : btnDarkBlue} alt=""/>
            <span className='btnImgText'>Delete</span>
        </div>
    );
}


export function GoogleLoginButton() {
    const handleLogin = () => {
        const clientId = '1021279696244-76eiutmeco59hp8mcj9cl4rvqlaa69e0.apps.googleusercontent.com';
        const redirectUri = 'http://127.0.0.1:8100/auth/google/callback';
        const scope = 'email profile'; // application is requesting permission to access the user's email and profile information.
        const authUrl = `https://accounts.google.com/o/oauth2/v2/auth?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=code&scope=${scope}&access_type=online`;
    
        window.location.href = authUrl;
    };

    return <button onClick={handleLogin}>Login with Google</button>;
}
