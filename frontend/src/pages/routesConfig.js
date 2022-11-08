import HomeIcon from '@mui/icons-material/Home';
import CallIcon from '@mui/icons-material/Call';
import InfoIcon from '@mui/icons-material/Info';
import FormatAlignJustifyIcon from '@mui/icons-material/FormatAlignJustify'; 


const routesConfig = [
  {
    id: 'app',
title: 'sample',
messageId: 'Application',
type: 'group',
children: [
  {
    id: 'page-1',
    title: 'Home',
    messageId: 'Home',
    type: 'item',
    icon: <HomeIcon/> ,
    url: '/sample/page-1',
  },
  {
    id: 'page-2',
    title: 'Page 2',
    messageId: 'Blog',
    type: 'item',
    icon: <InfoIcon />,
    url: '/sample/page-2',
  },
  {
    id: 'page-2',
    title: 'Page 2',
    messageId: 'Contact',
    type: 'item',
    icon: <CallIcon />,
    url: '/sample/page-2',
  },
  {
    id: 'page-2',
    title: 'Page 2',
    messageId: 'About',
    type: 'item',
    icon: <FormatAlignJustifyIcon/>,
    url: '/sample/page-2',
  },
],
  }
      
  
];
export default routesConfig;
