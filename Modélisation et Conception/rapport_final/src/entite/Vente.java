package entite;

import java.util.List;
import com.modeliosoft.modelio.javadesigner.annotations.objid;

@objid ("b5a504bf-3d32-45c2-8b54-cd5c286f81a7")
public class Vente {
    @objid ("87210fee-b39c-49a0-aed8-2abf3307f2ea")
    private String nomVente;

    @objid ("d3886d01-15ad-4822-827d-e06b937913f1")
    private String dateDebut;

    @objid ("a4509795-6f28-4e96-a400-05e10c018912")
    private String dateFin;

    @objid ("c58897f5-8ccb-4565-a309-41cb3a16ff56")
    private List<String> activites;

    @objid ("5577ca1d-d905-4d54-bd9b-b9a289635e1c")
    private String descriptif;

    @objid ("75b565df-1050-4768-9c86-3543d2240f5e")
    private int idVente;

    @objid ("e6b61f9e-0bc9-4586-8eef-681998df2a93")
    private List<Produit> produitsMisEnVente;

    @objid ("abdd10b3-8d1e-4586-9b7a-53bf5b73af57")
    public Vente(String nomVente, String dateDebut, String dateFin, List<String> activites, String descriptif, int idVente, List<Produit> listeProduit) {
        super();
        this.nomVente = nomVente;
        this.dateDebut = dateDebut;
        this.dateFin = dateFin;
        this.activites = activites;
        this.descriptif = descriptif;
        this.produitsMisEnVente = listeProduit;
    }

    @objid ("0935344a-3ff1-47f8-97d2-0578908a7c6c")
    public String getNom() {
        return nomVente;
    }

    @objid ("56cd10b1-ae71-488b-ba14-8add43e14224")
    public String getDateDebut() {
        return dateDebut;
    }

    @objid ("cb777c5d-eaa5-4b45-af4a-ed33a8d146a2")
    public String getDateFin() {
        return dateFin;
    }

    @objid ("6628ddad-dede-4915-b039-5d3226d0fa36")
    public List<String> getActivites() {
        return activites;
    }

    @objid ("6d507243-3c4e-4e25-88a3-2cf0d78371d4")
    public String getDescriptif() {
        return descriptif;
    }

    @objid ("ce9dab55-71a6-4b5a-9c2d-0c4aa8f603ab")
    public int getIdVente() {
        // Automatically generated method. Please delete this comment before entering specific code.
        return this.idVente;
    }

    @objid ("61d2caa8-d072-4085-a455-eba2160bcee4")
    public String getNomVente() {
        return nomVente;
    }

    @objid ("08249f90-39df-4648-8278-3a5669532340")
    public List<Produit> getProduitsMisEnVente() {
        return produitsMisEnVente;
    }

}
