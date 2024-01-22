// accueil_spec.js
describe('Page d\'accueil', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000/');
  });

  it('devrait afficher l\'image de la bannière', () => {
    cy.get('.banniereFestival').should('be.visible');
  });

  it('devrait lire la vidéo', () => {
    cy.get('.Youtube').should('be.visible');
    cy.get('.Youtube').find('iframe').should('exist');
    
  });

  it('devrait naviguer vers la page Parcours', () => {
    cy.get('.e2eTestParcours').click();
    cy.url().should('include', 'Parcours');
    cy.get('.titreMosaiquee2e').should('be.visible');
  });

  it('devrait naviguer vers la page Lieux', () => {
    cy.get('.e2eTestLieux').click();
    cy.url().should('include', 'lieux');
    cy.get('.titreLieuxe2e').should('be.visible');
  });

  it('devrait naviguer vers la page Carte', () => {
    cy.get('.e2eTestCarte').click();
    cy.url().should('include', 'carte');
    cy.get('.titreCartee2e').should('be.visible');
  });

  it('devrait afficher le message de bienvenue pour le Centre-Val de Loire', () => {
    cy.contains('“Partez à la découverte du Centre Val de Loire”').should('be.visible');
    cy.contains('Bienvenue dans la magie du Centre-Val de Loire !').should('be.visible');
  });
});
