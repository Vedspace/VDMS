import React from 'react';
import {Form, Formik} from 'formik';
import * as yup from 'yup';
import AppTextField from '@crema/core/AppFormComponents/AppTextField';
import IntlMessages from '@crema/utility/IntlMessages';
import {useAuthMethod} from '@crema/utility/AuthHooks';
import Box from '@mui/material/Box';

import Button from '@mui/material/Button';
// import IconButton from '@mui/material/IconButton';
import AppInfoView from '@crema/core/AppInfoView';
import {Fonts} from 'shared/constants/AppEnums';
// import {Link} from 'react-router-dom';
// import {AiOutlineGoogle} from 'react-icons/ai';
// import InputAdornment from '@mui/material/InputAdornment';
// import PhoneIcon from '@mui/icons-material/Phone';


const validationSchema = yup.object({
  name: yup.string().required(<IntlMessages id='validation.nameRequired' />),
  email: yup
    .string()
    .email(<IntlMessages id='validation.emailFormat' />)
    .required(<IntlMessages id='validation.emailRequired' />),
  password: yup
    .string()
    .required(<IntlMessages id='validation.passwordRequired' />),
});

const OtpFirebase = () => {
  const {registerUserWithEmailAndPassword} = useAuthMethod();

  return (
    <Box sx={{flex: 1, display: 'flex', flexDirection: 'column'}}>
      <Box sx={{flex: 1, display: 'flex', flexDirection: 'column', mb: 5}}>
        <Formik
          validateOnChange={true}
          initialValues={{
            number: '',
          }}
          validationSchema={validationSchema}
          onSubmit={(data, {setSubmitting}) => {
            setSubmitting(true);
            console.log('data', data);
            registerUserWithEmailAndPassword(data);
            console.log(
              'registerUserWithEmailAndPassword',
              registerUserWithEmailAndPassword,
            );
            setSubmitting(false);
          }}
        >
          {({isSubmitting}) => (
            <Form style={{textAlign: 'left'}} noValidate autoComplete='off'>
              {/* <Box sx={{mb: {xs: 4, xl: 5}}}>
                <AppTextField
                  label={<IntlMessages id='Phone Number' />}
                  name='phone number'
                  type='text'
                  variant='outlined'
                  InputProps={{
                    startAdornment: (
                      <InputAdornment position='start'>
                        <PhoneIcon fontSize='small' color='secondary' />
                      </InputAdornment>
                    ),
                  }}
                  sx={{
                    width: '100%',
                    '& .MuiInputBase-input': {
                      fontSize: 14,
                    },
                  }}
                />
              </Box>

              <div>
                <Button
                  variant='contained'
                  color='primary'
                  disabled={isSubmitting}
                  sx={{
                    minWidth: 160,
                    fontWeight: Fonts.REGULAR,
                    fontSize: 16,
                    textTransform: 'capitalize',
                    padding: '4px 16px 8px',
                  }}
                  type='submit'
                >
                  <IntlMessages id='send otp' />
                </Button>
              </div> */}

              <Box sx={{mb: {xs: 4, xl: 5}, paddingTop: 6}}>
                <AppTextField
                  label={<IntlMessages id=' Otp' />}
                  name='phone number'
                  type='text'
                  variant='outlined'
                  sx={{
                    width: '100%',
                    '& .MuiInputBase-input': {
                      fontSize: 14,
                    },
                  }}
                />
              </Box>

              <div>
                <Button
                  variant='contained'
                  color='primary'
                  disabled={isSubmitting}
                  sx={{
                    minWidth: 160,
                    fontWeight: Fonts.REGULAR,
                    fontSize: 16,
                    marginLeft:'25%',
                    textTransform: 'capitalize',
                    padding: '4px 16px 8px',
                  }}
                  type='submit'
                >
                  <IntlMessages id='Confirm Otp' />
                </Button>
              </div>
            </Form>
          )}
        </Formik>
      </Box>
{/* 
      <Box
        sx={{
          color: 'grey.500',
          mb: {xs: 5, md: 7},
        }}
      >
        <span style={{marginRight: 4}}>
          <IntlMessages id='common.alreadyHaveAccount' />
        </span>
        <Box
          component='span'
          sx={{
            fontWeight: Fonts.MEDIUM,
            '& a': {
              color: (theme) => theme.palette.primary.main,
              textDecoration: 'none',
            },
          }}
        >
          <Link to='/signIn'>
            <IntlMessages id='common.signIn' />
          </Link>
        </Box>
      </Box> */}

       {/* </Box> */}

      <AppInfoView />
    </Box>
  );
};

export default OtpFirebase;
