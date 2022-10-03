import {React,useState} from "react";
import Nav from './Nav'
import styled  from 'styled-components';
import {Link} from 'react-router-dom'
import { Box, 
  Grid , 
  Typography, 
  Stack,
  Button,
  TextField,
  Paper
} from '@mui/material'

const AuthContainer = styled.div`
  background:var(--primary-color);
  margin-top:0px;
`      
const Wrapper = styled.div`
              display:flex;
              justify-content:space-around;
              align-items: center;
              min-height: 90vh;
          `

const LinkWrap = styled.span`
                color:'#3F3D56';
                cursor:pointer;
                &:hover {
                    color: var(--black);
                 }
                `
const Img = styled.img``

const Login = () => {
      const [email, setEmail] = useState('');
      const [password, setPassword] = useState('');

  return (
    <AuthContainer>
    <Nav/>
    <Wrapper>
      <Box sx = {{
         mt:16
      }}>
        <Img src = "assets/ThinkIdea.png" alt = "think"/>
      </Box>
      <Paper variant="elevation"
          elevation={2}
          className="login-background">
        <Box padding = {2} 
        sx = {
          {
            backgroundColor : 'custom.light',
            width:'30vw',
            p : 8,
            borderRadius: '30px'
          }          
          }> 
        <Grid container direction="column" spacing={1} >
          <Grid item>
            <Typography component="h1" variant="h4" align = "center">
                 Get Started
            </Typography>
          </Grid>
          <Grid item align = "center">
             <Typography variant="body2"  >
                 Don't have a account?<Link to = "/signup"><LinkWrap> Sign Up</LinkWrap></Link>
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
               onChange={e => setEmail(e.target.value)}
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
                onChange={e => setPassword(e.target.value)}
                 fullWidth
              />
              </Grid>
              <Grid item sx = {{mt : 3}}>
              <Button type="submit" variant="contained" 
              sx = {{
                backgroundColor: 'secondary.main',
               color : 'custom.light', 
                width:'100%',
                }}>
                Login
              </Button>
              </Grid>
               <Grid item align = "center" sx = {{ margin : '20px' }}>
           <Typography variant = "body2">
            ---------------------- or login with ----------------------
            </Typography>
        </Grid>
               <Grid item>
           <Paper variant="elevation"
          elevation={2}>
            <Button type="submit" variant="contained" 
              sx = {{
                backgroundColor: 'custom.light',
                color : 'secondary.main',
                width:'100%'
                }}>
                <Img src = "assets/Google.png" alt = "Google" style ={{width:'20px', margin:'10px'}}></Img>
                          Continue with Google
              </Button>
              </Paper>
         </Grid>
        </Grid>
        </Box>
        </Paper>
        <Box sx = {{
         mt:16
      }}>
        <Img src = "assets/meetPeople.png" alt = "meet"/>
      </Box>
    </Wrapper>
    </AuthContainer>
    );
};

export default Login;
