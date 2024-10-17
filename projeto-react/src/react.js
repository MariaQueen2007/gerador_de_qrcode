import React from 'react';
import logo from './logo.svg';
import './App.css';

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

  const itensLista = [];
  listadeAlunos.forEach((item) => {
    itensLista.push(<li key={item.nome}>{item.nome}</li>);
  });

  return (
    <ul>
      {itensLista}
    </ul>
  );     
}

export default App;