package controleur;

import java.util.List;
import com.modeliosoft.modelio.javadesigner.annotations.objid;
import entite.BDProduit;
import entite.BDVente;
import entite.Produit;
import entite.Vente;

@objid ("5b7b5c18-a16c-45f0-b3ee-1fef4da62b8f")
public class ControlProposerVente {
    @objid ("43e78829-e171-458c-8fb8-4f9fae171312")
    private BDProduit bdProduit = new BDProduit();

    @objid ("6931fe0a-5561-429a-bf34-5b42f197d24f")
    private BDVente bdVente = new BDVente();

    @objid ("c9fcb895-6385-43ce-913a-4325d34b38ba")
    public BDProduit bDProduit;

    @objid ("c6ff13c8-df8e-40c8-a8b3-13678d268f6c")
    public BDVente bDVente;

    @objid ("ab27881e-235f-4b76-ba3d-b35f95fc9474")
    public void creerVente(String nomVente, String dateDebut, String dateFin, List<String> activites, String descriptif, int idVente) {
        List<Produit> listProduit = bdProduit.recupererListeProduit(idVente);
        Vente vente = new Vente(nomVente, dateDebut, dateFin, activites, descriptif, idVente, listProduit);
        bdVente.ajouterVente(vente);
    }

    @objid ("94f0240e-2aa4-4323-914b-a3dce5383f32")
    public Produit creerProduit(String nomProduit, String description, String photo, String prixDeBase, String prixDeVente, String nomTaille, String quantite, int idVente) {
        Produit produit = new Produit(nomProduit, description, photo, prixDeBase, prixDeVente, nomTaille, quantite, idVente);
        return produit;
    }

    @objid ("0fc5e4c0-c00a-43ab-924c-a3a6b776d53a")
    public int getIdProchaineVente() {
        return bdVente.getSize();
    }

    @objid ("be9d2ee6-0488-4130-ab36-36d505590e8c")
    public void detruireListeProduit(int idVente) {
        bdProduit.supprimerListeProduit(idVente);
    }

}
