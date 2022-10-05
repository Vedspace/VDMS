import React from "react";

  
import {
  BrowserRouter as Router,
} from "react-router-dom"

import AnimatedRoutes from "./Components/AnimatedRoutes";

function App() {
 
    return (
      <React.Fragment>
        <Router>
       
    <AnimatedRoutes/>
        
    </Router>
    </React.Fragment>
  );
}

export default App;