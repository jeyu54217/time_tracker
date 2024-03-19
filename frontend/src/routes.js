
import './styles/routes.css';
import React from 'react';

import HomePage from './components/HomePage';
import RecordsPage from './components/RecordsPage';
import SignIn from './components/auth/SignIn';
import SignUp from './components/auth/SignUp';
import SignOut from './components/auth/SignOut';


import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';


// ... other imports ...


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage/>} />
        <Route path="/record" element={<RecordsPage/>} />

        <Route path="/sign-in" element={<SignIn />} />
        <Route path="/sign-up" element={<SignUp />} />
        <Route path="/sign-out" element={<SignOut />} />
      </Routes>
    </Router>
  );
}

export default App;
