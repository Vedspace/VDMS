import {React,useState,useEffect} from 'react';
import {Form, Formik} from 'formik';
import * as yup from 'yup';
import AppTextField from '@crema/core/AppFormComponents/AppTextField';
import { Select, MenuItem, FormHelperText, FormControl, InputLabel } from '@mui/material';
import IntlMessages from '@crema/utility/IntlMessages';
import {useAuthMethod} from '@crema/utility/AuthHooks';
import Box from '@mui/material/Box';
import Checkbox from '@mui/material/Checkbox';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import AppInfoView from '@crema/core/AppInfoView';
import {Fonts} from 'shared/constants/AppEnums';
import {Link} from 'react-router-dom';
import {AiOutlineGoogle} from 'react-icons/ai';
import InputAdornment from '@mui/material/InputAdornment';
import AlternateEmailIcon from '@mui/icons-material/AlternateEmail';
import PersonIcon from '@mui/icons-material/Person';
import WorkIcon from '@mui/icons-material/Work';

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

const SignupFirebase = () => {
  const {registerUserWithEmailAndPassword, logInWithPopup} = useAuthMethod();
  const [selected,setSelected] =  useState("");
  const [specify,setSpecify] = useState(false);

const Designation = [
    'Student', 'Entrepreneur', 'Freelancer', 'Office Goer', 'Techie', 'Self Employed Businessmen', 
    'Affiliate Marketer', 'Digital Marketer', 'Other'
];  

const specifyBox = () =>{
  console.log(selected);
  if(selected === 'Other')
  {
    setSpecify(true);
  }
  else{
    setSpecify(false);
  }
};

useEffect(()=>{
  specifyBox();
} , [selected] );


  return (
    <Box sx={{flex: 1, display: 'flex', flexDirection: 'column'}}>
      <Box sx={{flex: 1, display: 'flex', flexDirection: 'column', mb: 5}}>
        <Formik
          validateOnChange={true}
          initialValues={{
            name: '',
            email: '',
            password: '',
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
              <Box sx={{mb: {xs: 4, xl: 5}}}>
                <AppTextField
                  label={<IntlMessages id='common.name' />}
                  name='name'
                  variant='outlined'
                  InputProps={{
                    startAdornment: (
                      <InputAdornment position='start'>
                        <PersonIcon fontSize='small' color='secondary' />
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

              <Box sx={{mb: {xs: 4, xl: 5}}}>
                <AppTextField
                  label={<IntlMessages id='common.email' />}
                  name='email'
                  variant='outlined'
                  InputProps={{
                    startAdornment: (
                      <InputAdornment position='start'>
                        <AlternateEmailIcon
                          fontSize='small'
                          color='secondary'
                        />
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

       <Box sx={{mb: {xs: 4, xl: 5}}}>
                <AppTextField
                  label="Please Specify"
                  name='Please specify'
                  variant='outlined'
                   InputProps={{
                    startAdornment: (
                      <InputAdornment position='start'>
                        <WorkIcon
                          fontSize='small'
                          color='secondary'
                        />
                      </InputAdornment>
                    ),
                  }}
                  sx={{
                    width: '100%',
                    display: specify ? '' : 'none',
                    '& .MuiInputBase-input': {
                       fontSize: 14,
                    },
                  }}
                />
              </Box>        

    <FormControl variant = "outlined" sx={{mb: {xs: 4, xl: 5}, width:'100%'}}>
      <InputLabel>Designation</InputLabel>
            <Select 
            label = "Designation" value = {selected} 
            onChange = {(e)=>{setSelected(e.target.value);}}
            >
            {Designation.map((item,idx) => (
                 <MenuItem key = {idx} value={item}>{item}</MenuItem>
            ))};
           </Select>
             <FormHelperText>Select your designation</FormHelperText>
    </FormControl>
       
       

              <Box
                sx={{
                  mb: {xs: 3, xl: 4},
                  display: 'flex',
                  alignItems: 'center',
                  flexWrap: 'wrap',
                }}
              >
                <Box
                  sx={{
                    display: 'flex',
                    alignItems: 'center',
                  }}
                >
                  <Checkbox
                    sx={{
                      ml: -3,
                    }}
                  />
                  <Box
                    component='span'
                    sx={{
                      mr: 2,
                      color: 'grey.500',
                    }}
                  >
                    <IntlMessages id='common.iAgreeTo' />
                  </Box>
                </Box>
                <Box
                  component='span'
                  sx={{
                    color: (theme) => theme.palette.primary.main,
                    cursor: 'pointer',
                  }}
                >
                  <IntlMessages id='common.termConditions' />
                </Box>
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
                  <IntlMessages id='common.signup' />
                </Button>
              </div>
            </Form>
          )}
        </Formik>
      </Box>

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
      </Box>

      <Box
        sx={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          backgroundColor: (theme) => theme.palette.background.default,
          mx: {xs: -5, lg: -10},
          mb: {xs: -6, lg: -11},
          mt: 'auto',
          py: 2,
          px: {xs: 5, lg: 10},
        }}
      >
        <Box
          sx={{
            color: (theme) => theme.palette.text.secondary,
          }}
        >
          <IntlMessages id='common.orLoginWith' />
        </Box>
        <Box
          sx={{
            display: 'flex',
            alignItems: 'center',
          }}
        >
          <IconButton
            sx={{p: 2, '& svg': {fontSize: 18}}}
            onClick={() => logInWithPopup('google')}
          >
            <AiOutlineGoogle />
          </IconButton>
        </Box>
      </Box>

      <AppInfoView />
    </Box>
  );
};

export default SignupFirebase;
