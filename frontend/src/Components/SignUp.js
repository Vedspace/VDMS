import {React,useState} from 'react'
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
const SignUp = () => {
      const [firstName, setFirstName] = useState("");
      const [lastName, setLastName] = useState("");
      const [email, setEmail] = useState("");
      const [password, setPassword] = useState("");

const Wrapper = styled.div`
              background:var(--primary-color);
              display:flex;
              justify-content:center;
              align-items: center;
              min-height: 100vh;
          `

const LinkWrap = styled.span`
                color:'#3F3D56';
                cursor:pointer;
                &:hover {
                    color: var(--black);
                 }
                `
                
                

  return (
    <Wrapper>
      <Paper variant="elevation"
          elevation={2}
          className="login-background">
        <Box  padding = {2} 
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
             <Typography variant = "body2">
                 Already have a account?<Link to = "/login"><LinkWrap> Login</LinkWrap></Link>
             </Typography>
          </Grid>
          <Grid item>

             <TextField
                label="firstName"
                variant="standard"
                placeholder="Enter your FirstName"
                value={firstName}
                onChange={e => setFirstName(e.target.value)}
                fullWidth
                required
              />
        </Grid>
        <Grid item>
              <TextField
                label="lastName"
                variant="standard"
                placeholder="Enter your lastName"
                required
                value={lastName}
                onChange={e => setLastName(e.target.value)}
                fullWidth
              />
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
                SignUp
              </Button>
              </Grid>
        </Grid>
        </Box>
        </Paper>
    </Wrapper>
  )
}

export default SignUp
