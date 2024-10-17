import React from 'react';
import logo from './logo.svg';
import './App.css';
import Button from '@mui/material/Button';

function App() {
  const listadeAlunos = [
    {nome: 'João K'},
    {nome: 'Bruno'},
    {nome: 'Chris'},
    {nome: 'Izac'},
    {nome: 'Felipe'},
    {nome: 'Anderson'},
    {nome: 'Anadir'},
    {nome: 'Gabii'},
    {nome: 'Lorii'},
    {nome: 'PL'},
    {nome: 'Jãozin'},
    {nome: 'Tpelink'},
  ];
  return (
  <>
    <ul>

      {listadeAlunos.map((item) => {return (<li>{item.nome}</li>)})}
      <Button variant="contained">Hello world</Button>
      
    </ul>
  </>
  );     
}
export default App;
