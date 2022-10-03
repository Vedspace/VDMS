import Login from "./Components/Login";
import SignUp from "./Components/SignUp";

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
} from "react-router-dom"
import React from "react";

function App() {
  return (
    <React.Fragment>
      <Router>
        <Routes>
                <Route path="/login" element={<Login/>} />
                <Route path="/signup" element={<SignUp/>} />
        </Routes>
      </Router>
    </React.Fragment>
  );
}

export default App;
