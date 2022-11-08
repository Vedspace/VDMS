import React from 'react';
import {Box, Typography, Divider, Link} from '@mui/material';
import {Fonts} from 'shared/constants/AppEnums';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Container from '@mui/material/Container';
//import Grid from '@mui/material/Grid';
// import Stack from '@mui/material/Stack';
// import Paper from '@mui/material/Paper';
//import GitHubIcon from '@mui/icons-material/GitHub';
//import FacebookIcon from '@mui/icons-material/Facebook';
// import TwitterIcon from '@mui/icons-material/Twitter';

const Page2 = () => {
  return (
    <>
      {/*---------------------------------- main container begins --------------------------------*/}
      <Container maxWidth='200'>
        <Box>
          {/*---------------------------------- main box at top with blog name  --------------------------------*/}
          <Box
            sx={{
              maxWidth: 350,
            }}
          >
            <Typography
              sx={{
                minWidth: 260,
                fontWeight: Fonts.REGULAR,
                fontSize: 46,
                textTransform: 'capitalize',
                padding: '1px 16px 1px',
              }}
            >
              Blog NAme
            </Typography>
            <Divider />
          </Box>
          {/*---------------------------------- main box at top with date  --------------------------------*/}
          <Box>
          <Typography
            sx={{
              minWidth: 160,
              fontWeight: Fonts.REGULAR,
              fontSize: 16,
              textTransform: 'capitalize',
              padding: '2px 2px 20px',
            }}
          >
            17 November 2022
          </Typography>
          </Box>
          {/*----------------------------------box with card content (About)  --------------------------------*/}

          <Box>
            <Card sx={{minWidth: 70, height: 180, mx: 100, my: -30}}>
              <CardContent>
                <Typography variant='h2' component='div'>
                  About
                </Typography>
                <Typography sx={{pt: 4, fontSize: 20 , pb:15}} variant='body2'>
                  About the blog page
                  <br />
                </Typography>
              </CardContent>
            </Card>
          </Box>
     {/*---------------------------------- box with short para on blog  --------------------------------*/}
          <Box>
            <Typography
              sx={{
                minWidth: 260,
                fontWeight: Fonts.REGULAR,
                fontSize: 20,
                textTransform: 'capitalize',
                pt:20
              }}
            >
              Short para on blog
              <br />
              Short para on blog
              <br /> Short para on blog
            </Typography>
            <Divider />
            {/*---------------------------------- box with subheading of blog  --------------------------------*/}
            <Box>
              <Typography sx={{mt: 5, maxWidth: 300}}>
                <h2>Subheading of the blog</h2>
              </Typography>
              <Typography sx={{mt: 5, maxWidth: 800}}>
                Lorem vdvlmsdg <br />
                Cum sociis natoque penatibus et magnis dis parturient montes,
                nascetur ridiculus mus. Example code block Aenean lacinia
                bibendum nulla sed consectetur. Etiam porta sem malesuada magna
                mollis euismod. Fusce dapibus, tellus ac cursus commodo, tortor
                mauris condimentum nibh, ut fermentum massa.
              </Typography>
              <Typography sx={{mt: 5, maxWidth: 300}}>
                <h2>Sub-heading</h2>
              </Typography>
              <Typography sx={{mt: 5, maxWidth: 800}}>
                Lorem vdvlmsdg <br />
                Cum sociis natoque penatibus et magnis dis parturient montes,
                nascetur ridiculus mus. Example code block Aenean lacinia
                bibendum nulla sed consectetur. Etiam porta sem malesuada magna
                mollis euismod. Fusce dapibus, tellus ac cursus commodo, tortor
                mauris condimentum nibh, ut fermentum massa.
              </Typography>
{/*---------------------------------- box with leftsidebar --------------------------------*/}
              <Box
                sx={{
                  ml: 200,
                  mt: 1,
                }}
              >
                <Typography variant='h4'>Archives</Typography>
                <Typography>
                  <Link display='block' variant='body1' href=''>
                    March 2020
                  </Link>
                </Typography>
                <Typography>
                  <Link display='block' variant='body1' href=''>
                    February 2020
                  </Link>
                </Typography>
                <Typography>
                  <Link display='block' variant='body1' href=''>
                    January 2020
                  </Link>
                </Typography>
                <Typography>
                  <Link display='block' variant='body1' href=''>
                    November 1999
                  </Link>
                </Typography>
                <Typography>
                  <Link display='block' variant='body1' href=''>
                    October 1999
                  </Link>
                </Typography>
                <Typography>
                  <Link display='block' variant='body1' href=''>
                    September 1999
                  </Link>
                </Typography>
                <Typography>
                  <Link display='block' variant='body1' href=''>
                    August 1999
                  </Link>
                </Typography>
                <Typography>
                  <Link display='block' variant='body1' href=''>
                    July 1999
                  </Link>
                </Typography>
                <Typography>
                  <Link display='block' variant='body1' href=''>
                    July 1999
                  </Link>
                </Typography>
                <Typography>ElseWhere</Typography>
                <Typography>
                  <Link display='block' variant='body1' href=''>
                    Github
                  </Link>
                </Typography>
                <Typography>
                  <Link display='block' variant='body1' href=''>
                    Twitter
                  </Link>
                </Typography>
                <Typography>
                  <Link display='block' variant='body1' href=''>
                    Facebook
                  </Link>
                </Typography>
              </Box>
            </Box>
          </Box>
        </Box>
      </Container>
    </>
  );
};

export default Page2;
