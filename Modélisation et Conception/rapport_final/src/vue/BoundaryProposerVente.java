package vue;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import com.modeliosoft.modelio.javadesigner.annotations.objid;
import controleur.ControlProposerVente;
import controleur.ControlVerifierIdentification;

@objid ("ac0d9ee4-cb47-483e-bb48-56ee18a68b93")
public class BoundaryProposerVente {
    @objid ("3732681b-d2d3-4934-8392-b8b943dfc00a")
     Scanner s = new Scanner(System.in);

    @objid ("9b581da2-c085-488e-8a80-62c52a6f8f1e")
    public ControlVerifierIdentification controlVerifierIdentification;

    @objid ("7ab253f7-a510-4eba-a02b-e63b2f13b5a2")
    public ControlProposerVente controlProposerVente;

    @objid ("dd160d7a-ecc4-40fe-9641-1aca82a85c5b")
    public void proposerVente(int id) {
        ControlVerifierIdentification controlVerifierIdentification = new ControlVerifierIdentification();
        ControlProposerVente controlProposerVente = new ControlProposerVente();
        
        boolean fournisseurIdentifie = controlVerifierIdentification.verifierIdentification(id);
        
        if (fournisseurIdentifie) {
            System.out.println("Entrer le nom de la vente");
            String nomVente = entrerClavier();
            
            System.out.println("Entrer la date de debut de la vente");
            String dateDebut = entrerClavier();
            
            System.out.println("Entrer la date de fin de la vente");
            String dateFin = entrerClavier();
            
            System.out.println("Entrer au moins une activite");
            List<String> activites = new ArrayList<String>();
            int nbActivite = 0;
            String activite = "";
            
            while(activite != "" || nbActivite < 1) {
                activite = entrerClavier();
                activites.add(activite);
                nbActivite++;
            }
            
            System.out.println("Entrer un descriptif");
            String descriptif = entrerClavier();
            
            int idVente = controlProposerVente.getIdProchaineVente();
            String reponseProduit;
            
            do{
                System.out.println("Entrer le nom du produit");
                String nomProduit = entrerClavier();
                
                System.out.println("Entrer la description du produit");
                String description = entrerClavier();
                
                System.out.println("Entrer la photo du produit");
                String photo = entrerClavier();
                
                System.out.println("Entrer le prix de base");
                String prixDeBase = entrerClavier();
                
                System.out.println("Entrer le prix de vente");
                String prixDeVente = entrerClavier();
                
                String reponseTaille;
                do {
                    System.out.println("Entrer le nom de la taille");
                    String nomTaille = entrerClavier();
                    
                    System.out.println("Entrer quantite pour la taille");
                    String quantite = entrerClavier();
                    
                    controlProposerVente.creerProduit(nomProduit, description, photo, prixDeBase, prixDeVente, nomTaille, quantite, idVente);
                    
                    System.out.println("Voulez-vous rentrer une autre taille O/N?");
                    reponseTaille = entrerClavier();
                } while(reponseTaille.equals("O"));
                
                System.out.println("Voulez-vous rentrer un autre produit O/N?");
                reponseProduit = entrerClavier();
            } while(reponseProduit.equals("O"));
            
            String confirmation;
            
            System.out.println("Voulez-vous confirmer la vente O/N?");
            confirmation = entrerClavier();
            
            if (confirmation.equals("O")) {
                controlProposerVente.creerVente(nomVente, dateDebut, dateFin, activites, descriptif, idVente);
                System.out.println("La vente a ete creee");
            }
            else {
                controlProposerVente.detruireListeProduit(idVente);
                System.out.println("La vente a bien ete annulee");
            }
        }
        else {
            System.out.println("Vous devez être identifié pour accéder à ce service.");
        }
    }

    @objid ("02768b19-2536-40a8-8740-eb2537e6bbae")
    public static void main(String[] args) {
        BoundaryProposerVente boundaryProposerVente = new BoundaryProposerVente();
        boundaryProposerVente.proposerVente(1001); // On admet que 1001 est un identifiant fournisseur valide
    }

    @objid ("3753c990-2b66-41d1-817b-c2b0fe24e9a1")
    public String entrerClavier() {
        String entree = s.nextLine();
        return entree;
    }

}
