import React from 'react'
import styled from 'styled-components'

const Img = styled.img`
`

const Nav = () => {
  return (
       <div style = {{background : 'var(--primary-color)', width:'10vw' , margin : '0px'}}>
       <Img src = "assets/Logo-bg.png" alt = "Logo"></Img>
       </div>  
  )
}

export default Nav
