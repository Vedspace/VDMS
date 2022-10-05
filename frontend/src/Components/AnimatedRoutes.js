import React from 'react'
import Login from './Login';
import SignUp from './SignUp';
import Otp from './Otp';

import {
    Routes,
    Route,
    useLocation,
  } from "react-router-dom"
import { AnimatePresence } from "framer-motion";
  

function AnimatedRoutes() {
    const location = useLocation();
  return (
    
   <AnimatePresence>
    <Routes location={location} key={location.pathname}>
            <Route path="/login" element={<Login/>} />
            <Route path="/signup" element={<SignUp/>} />
            <Route path="/Otp" element={<Otp/>} />
            
    </Routes>
    </AnimatePresence>
  )
}

export default AnimatedRoutes