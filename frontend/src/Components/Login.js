import { React, useState } from "react";
import Nav from "./Nav";
import styled from "styled-components";
import { Link } from "react-router-dom";
import { Box, Grid, Typography, Button, TextField, Paper } from "@mui/material";
import { motion } from "framer-motion";


  const AuthContainer = styled.div`
    background: var(--primary-color);
    overflow: hidden;
  `;
  const Wrapper = styled.div`
    display: flex;
    justify-content: space-around;
    align-items: center;
    min-height: 100vh;
  `;


const LinkWrap = styled.span`
  color: "#3F3D56";
  cursor: pointer;
  &:hover {
    color: var(--black);
  }
`;
const Img = styled.img``;


  
const Login = () => {


  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  return (
    <AuthContainer>
      <Nav />
      <Wrapper>
        <Box
          sx={{
            mt: 16,
          }}
        >
          <Img src="assets/ThinkIdea.png" alt="think" />
        </Box>
        <Paper variant="elevation" elevation={2} className="login-background">
          <Box
            padding={2}
            
            sx={{
              backgroundColor: "custom.light",
              width: "30vw",
              p: 8,
              borderRadius: "30px",
            }}
          >
            <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{opacity: 0}}
            >

           
            <Grid container direction="column" spacing={1}>
              <Grid item>
                <Typography component="h1" variant="h4" align="center">
                  Get Started
                </Typography>
              </Grid>
              <Grid item align="center">
                <Typography variant="body2">
                  Don't have a account?
                  <Link to="/signup">
                    <LinkWrap> Sign Up</LinkWrap>
                  </Link>
                </Typography>
              </Grid>
              <Grid item>
                <TextField
                  label="Email"
                  variant="standard"
                  type="email"
                  required
                  value={email}
                  fullWidth
                  onChange={(e) => setEmail(e.target.value)}
                />
              </Grid>
              <Grid item>
                <TextField
                  label="Password"
                  variant="standard"
                  placeholder="Enter password"
                  type="password"
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  fullWidth
                />
              </Grid>
              <Grid item sx={{ mt: 3 }}>
                <Button
                  type="submit"
                  variant="contained"
                  sx={{
                    backgroundColor: "secondary.main",
                    color: "custom.light",
                    width: "100%",
                  }}
                >
                  Login
                </Button>
              </Grid>
              <Grid item align="center" sx={{ margin: "20px" }}>
                <Typography variant="body2">
                  ---------------------- or login with ----------------------
                </Typography>
              </Grid>
              <Grid item>
                <Paper variant="elevation" elevation={2}>
                  <Button
                    type="submit"
                    variant="contained"
                    disableElevation
                  disableRipple
                  size="small"
                    sx={{
                      backgroundColor: "custom.light",
                      color: "secondary.main",
                      width: "100%",
                      ml: 1,
                    "&.MuiButtonBase-root:hover": {
                      bgcolor: "custom.light",
                    },
                    }}
                  >
                    <Img
                      src="assets/Google.png"
                      alt="Google"
                      style={{ width: "20px", margin: "10px" }}
                    ></Img>
                    Continue with Google
                  </Button>
                </Paper>
              </Grid>
            </Grid>
            </motion.div>
          </Box>
        </Paper>
        <Box
          sx={{
            mt: 16,
          }}
        >
          <Img src="assets/meetPeople.png" alt="meet" />
         
        </Box>
      </Wrapper>
    </AuthContainer>
  );
};

export default Login;
