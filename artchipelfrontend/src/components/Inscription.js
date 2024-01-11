import React, {useState, useEffect} from "react";
import "../style/styleAccueil.css";
import ImageConnexion from "../components/images/connexion.png"


const Connexion = () => {

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [password2, setPassword2] = useState('');
  const [email, setEmail] = useState('');
  const [first_name, setFirstname] = useState('');
  const [last_name, setLastname] = useState('');
  const [ddnUtilisateur, setDdn] = useState('');
  const [error, setError] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);


  const handleRegister = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/register/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password, password2, email, first_name, last_name, ddnUtilisateur }),
      });

      console.log(JSON.stringify({ username, password, password2, email, first_name, last_name, ddnUtilisateur }));


      

      if (response.ok) {
        const data = await response.json();
        console.log("ajout de l'utilisateur");

        
        window.location.replace('http://localhost:3000/Connexion');
      } else {
        setError('Nom d\'utilisateur ou mot de passe incorrect');
      }
    } catch (error) {
      console.error('Une erreur est survenue lors de la connexion :', error);
      setError('Une erreur est survenue lors de la connexion');
    }
  };

  return (
    <div className="index">
      {isLoggedIn ? (
        <div class="text-center bg-danger">
          Vous êtes déjà connecté. Redirection vers la page d'accueil...
        </div>
      ) : (
        <div class="container-fluid m-5">
          <div class="row justify-content-center">
            <div class="col-5">
              <div class="col-8 container p-5">
                <div class="text-center border">
                  <h1 class="p-3">Inscription</h1>
                  <div>
                    <div class="container">

                      {error && <p style={{ color: 'red' }}>{error}</p>}

                      <div class="row justify-content-center m-4">
                        <p class="m-1 text-center">Nom d'utilisateur:</p>
                        <input type="text" name="username" placeholder="Entrez votre nom d'utilisateur" onChange={(e) => setUsername(e.target.value)}  style={{width:'300px'}} ></input>
                      </div>
                      <div class="row justify-content-center m-4">
                        <p class="m-1 text-center">Mot de passe:</p>
                        <input type="password" name="password" placeholder="Entrez votre mot de passe" onChange={(e) => setPassword(e.target.value)} style={{width:'300px'}}></input>
                      </div>
                      <div class="row justify-content-center m-4">
                        <p class="m-1 text-center">Confirmation mot de passe:</p>
                        <input type="password" name="password2" placeholder="Confirmation mot de passe" onChange={(e) => setPassword2(e.target.value)} style={{width:'300px'}}></input>
                      </div>
                      <div class="row justify-content-center m-4">
                        <p class="m-1 text-center">Email:</p>
                        <input type="text" name="email" placeholder="Entrez votre email" onChange={(e) => setEmail(e.target.value)} style={{width:'300px'}}></input>
                      </div>
                      <div class="row justify-content-center m-4">
                        <p class="m-1 text-center">Prénom:</p>
                        <input type="text" name="first_name" placeholder="Entrez votre Prénom" onChange={(e) => setFirstname(e.target.value)} style={{width:'300px'}}></input>
                      </div>
                      <div class="row justify-content-center m-4">
                        <p class="m-1 text-center">Nom:</p>
                        <input type="text" name="last_name" placeholder="Entrez votre Nom" onChange={(e) => setLastname(e.target.value)} style={{width:'300px'}}></input>
                      </div>
                      <div class="row justify-content-center m-4">
                        <p class="m-1 text-center">Date de Naissance:</p>
                        <input type="date" name="ddnUtilisateur" onChange={(e) => setDdn(e.target.value)} style={{width:'300px'}}></input>
                      </div>

                      <div class="row justify-content-center m-4">
                        <div class="container">
                        <button class="btn btn-primary" onClick={handleRegister}>Valider</button>
                        </div>                     
                      </div>
                    </div>
                  </div>
                </div>
                
              </div>
            </div>
            <div class="col-5">
              <div class="d-flex justify-content-center">
              <img src={ImageConnexion} style={{width:'700px'}}></img>
              </div>
            </div>
          </div>
          
        </div>
        )}
  </div>     
  
  
  );
};

export default Connexion;
