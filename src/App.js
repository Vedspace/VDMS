import { useState } from "react";
import "./App.css";
import login from "./images/press-play.svg";
import register from "./images/rocket.svg";

function App() {
  const [signupMode, setSignupMode] = useState("");

  const signupBtn = () => {
    setSignupMode("sign-up-mode");
  };

  const signinBtn = () => {
    setSignupMode("");
  };

  return (
    <div className={"app" + " " + signupMode}>
      <div className="forms-container">
        <div className="signin-signup">
          <form action="" className="sign-in-form">
            <h2 className="title">Sign in</h2>
            <div className="input-field">
          
              <input type="text" placeholder="Username" />
            </div>
            <div className="input-field">
              

              <input type="password" placeholder="Password" />
            </div>
            <input type="submit" value="Login" className="btn solid" />
          </form>

          <form action="" className="sign-up-form">
            <h2 className="title">Sign up</h2>
            <div className="input-field">
             
              <input type="text" placeholder="Username" />
            </div>
            <div className="input-field">
            
              <input type="Number" placeholder="Contact Number" />
            </div>
            <div className="input-field">
            
              <input type="email" placeholder="Email" />
            </div>
            <div className="input-field">
               
              <input type="password" placeholder="Password" />
            </div>
            <input type="submit" value="Sign up" className="btn solid" />
          </form>
        </div>
      </div>

      <div className="panels-container">
        <div className="panel left-panel">
          <div className="content">
            <h3>New here?</h3>
            <p>Sign up now and Welcome to Vedspace Venture</p>
            <button
              className="btn transparent"
              id="sign-up-btn"
              onClick={signupBtn}
            >
              Sign up
            </button>
          </div>
          <img src={register} className="image" alt="vedspace" />
        </div>

        <div className="panel right-panel">
          <div className="content">
            <h3>Already Signed in ?</h3>
            <p>Welcom back Login from here</p>
            <button
              className="btn transparent"
              id="sign-in-btn"
              onClick={signinBtn}
            >
              Sign in
            </button>
          </div>
          <img src={login} className="image" alt="vedspace" />
        </div>
      </div>
    </div>
  );
}

export default App;
