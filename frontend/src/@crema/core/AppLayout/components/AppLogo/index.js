import React from 'react';
// import {useThemeContext} from '../../../../utility/AppContextProvider/ThemeContextProvider';
import {Box} from '@mui/material';
import {ReactComponent as Logo} from '../../../../../assets/icon/logo.svg';
import {ReactComponent as LogoText} from '../../../../../assets/icon/logo_text.svg';

const AppLogo = () => {
  // const {theme} = useThemeContext();

  return (
    <Box
      sx={{
        height: {xs: 50, sm: 40},
        display: 'flex',
        flexDirection: 'row',
        cursor: 'pointer',
        alignItems: 'center',
        justifyContent: 'center',
        '& svg': {
          height: {xs: 50, sm: 50 },paddingRight:23, 
        },
      }}
    >
      <Logo />
      {/* <Box
        sx={{
          mt: 1,
          display: {xs: 'none', md: 'block'},
          '& svg': {
            height: {xs: 25, sm: 30},
          },
        }}
      > */}
        <LogoText  />
      {/* </Box> */}
    </Box>
  );
};

export default AppLogo;
