import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { ThemeProvider,createTheme } from '@mui/material'
import App from './App';

const theme = createTheme({
  palette: {
  primary:{
    main: "#D7FAE7",
  },
  secondary :{
    main: "#3F3D56"
  },
  custom:{
    light:'#ffffff',
    dark:"#000000"
  }
}
});

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
    <App />
    </ThemeProvider>
  </React.StrictMode>
);

