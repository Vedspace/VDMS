import React from 'react';
import {TextInput} from 'react-native';
import {darkGreen} from './Constants';

const Field = props => {
  return (
    <TextInput
      {...props}
      style={{borderRadius: 100, color: darkGreen, paddingHorizontal: 50, width: 300, backgroundColor: 'rgb(220,220, 220)', marginVertical: 10,marginRight:20}}
      placeholderTextColor={darkGreen}></TextInput>
  );
};

export default Field;