import React, { useState } from "react";
import styled from "styled-components";
import {
  Box,
  Grid,
  Typography,
  Paper,
  TextField,
  Input,
  Button,
} from "@mui/material";


const Wrapper = styled.div`
  display: flex;
  justify-content: space-around;
  align-items: center;
  min-height: 100vh;
`;

const Otp = () => {
  const [ number , setNumber] = useState("");
  const [ otp , setOtp] = useState("");

  return (
    <Wrapper>
      <Box
        sx={{
          mt: 1,
        }}
      >
        <Paper
          variant="elevation"
          elevation={2}
          className="login-background"
          qq
        >
          <Box
            padding={2}
            sx={{
              backgroundColor: "custom.light",
              width: "30vw",
              p: 2,
              borderRadius: "30px",
            }}
          ></Box>
         
          <Grid container direction="column" spacing={3}>
            <Grid item>
              <Typography component="h1" variant="h4" align="center">
                Otp Verification
              </Typography>
            </Grid>
            <Grid item align="center"></Grid>
          </Grid>
              {/* ----------------------ENter Number and send Otp----------------------------- */}
          <Grid  item align="center">
            <Grid item paddingBottom={1}>
              <TextField
                label="Enter Your Number"
                variant="standard"
                type="text"
                required
                value={number}
                onChange={(e) => setNumber(e.target.value)}
              />
               {/* ----------------------Send Otp button code----------------------------- */}
              <Grid item sx={{ mt: 1 }}>
                <Button
                  type="submit"
                  variant="contained"
                  sx={{
                    backgroundColor: "secondary.main",
                    color: "custom.light",
                    width: "40%",
                  }}
                >
                  Send Otp
                </Button>
              </Grid>
            </Grid>
          </Grid>
          {/* ----------------------ENter otp and confirm Otp----------------------------- */}
          <Grid  item align="center">
            <Grid item paddingBottom={3}>
              <TextField
                label="Enter The Otp"
                variant="standard"
                type="text"
                required
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
               />
           {/* ----------------------Confirm Otp button----------------------------- */}
              <Grid item sx={{ mt: 1
               }}>
                <Button
                  type="submit"
                  variant="contained"
                  sx={{
                    backgroundColor: "secondary.main",
                    color: "custom.light",
                    width: "40%",
                  }}
                >
                  Confirm Otp
                </Button>
              </Grid>
            </Grid>
            </Grid>
           
        </Paper>
      </Box>
    </Wrapper>
  );
};

export default Otp;
