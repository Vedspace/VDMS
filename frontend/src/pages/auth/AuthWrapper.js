import React from 'react';
import Card from '@mui/material/Card';
import Box from '@mui/material/Box';
import PropTypes from 'prop-types';
import {Typography} from '@mui/material';
import {Fonts} from 'shared/constants/AppEnums';
//import styled from '@emotion/styled';

const AuthWrapper = ({children}) => {

  return (
    <Box
      sx={{
        flex: 1,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
       <Card
        sx={{
          maxWidth: 900,
          minHeight: {xs: 320, sm: 450},
          width: '100%',
          overflow: 'hidden',
          position: 'relative',
          display: 'flex',
        }}
      >
    <Box
          sx={{
            width: {xs: '100%', sm: '50%', lg: '50%'},
            position: 'relative',
            padding: {xs: 5, lg: 10},
            display: {xs: 'none', sm: 'flex'},
            alignItems: {sm: 'center'},
            justifyContent: {sm: 'center'},
            flexDirection: {sm: 'column'},
            backgroundColor: (theme) => theme.palette.secondary.bg_sec,
            color: (theme) => theme.palette.common.white,
            fontSize: 14,
          }}
        >

      <Box
            sx={{
              maxWidth: 320,
            }}
          >
            <img style  = 
            {{transition:'2s all'}} 
            src = "assets/images/Rocket.gif" alt = "illustration"></img>
            <Typography
              component='h2'
              sx={{
                fontWeight: Fonts.BOLD,
                fontSize: 24,
                mb: 4,
              }}
            >
              Welcome to VedSpace!
            </Typography>
            <Typography>Professionals at Your Service</Typography>
          </Box>
        </Box>

        {/* content */}
        <Box
          sx={{
            width: {xs: '100%', sm: '50%', lg: '50%'},
            padding: {xs: 5, lg: 10},
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
          }}
        >
           {children}
        </Box> 
      </Card> 
    </Box>
  );
};

export default AuthWrapper;

AuthWrapper.propTypes = {
  children: PropTypes.node,
};
