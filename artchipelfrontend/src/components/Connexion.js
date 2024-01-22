import React, {useState, useEffect} from "react";
import "../style/styleAccueil.css";
import ImageConnexion from "../components/images/connexion.png"
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';


const Connexion = () => {

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const navigate = useNavigate();

  // useEffect(() => {
  //   // Vérifier si l'utilisateur est déjà connecté en vérifiant la présence du token dans le localStorage
  //   const storedToken = localStorage.getItem('token');

  //   if (storedToken) {
  //     // Utilisateur déjà connecté, rediriger vers la page d'accueil
  //     navigate('/');
  //   }
  // }, [navigate]);

  useEffect(() => {
    // Vérifier si l'utilisateur est déjà connecté en vérifiant la présence du token dans le localStorage
    const storedToken = localStorage.getItem('token');

    if (storedToken) {
      // Utilisateur déjà connecté
      setIsLoggedIn(true);

      // Afficher un message pendant quelques secondes avant la redirection
      const delayRedirect = setTimeout(() => {
        // Redirection vers la page d'accueil
        navigate('/');
      }, 2000); // Délai de 3 secondes (3000 millisecondes)

      // Nettoyer le délai si le composant est démonté avant la fin du délai
      return () => clearTimeout(delayRedirect);
    }
  }, [navigate]);

  const handleLogin = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        const data = await response.json();
        const token = data.access;

        // Stockez le token dans le localStorage ou dans les cookies, selon votre préférence.
        localStorage.setItem('token', token);
        localStorage.setItem('tokenrefresh', data.refresh);

        // Redirection vers la page d'accueil ou une autre page après une connexion réussie.
        // Vous pouvez utiliser React Router ou d'autres moyens de navigation.
        // Exemple avec React Router :
        //navigate('/');
        window.location.replace('http://localhost:3000/');
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
                  <h1 class="p-3">Connexion</h1>
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
                        <div class="container">
                        <button class="btn btn-primary" onClick={handleLogin}>Connexion</button>
                        </div>                     
                      </div>
                    </div>
                  </div>
                </div>
                <div class="d-flex justify-content-center">
                  <p>Vous n'avez pas encore de compte ? </p>
                  <Link to={`/Inscription/`}>
                    <a href="" class="ml-2">Inscrivez-vous</a>
                  </Link>
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
