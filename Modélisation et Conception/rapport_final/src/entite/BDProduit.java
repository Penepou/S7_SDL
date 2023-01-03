package entite;

import java.util.ArrayList;
import java.util.List;
import com.modeliosoft.modelio.javadesigner.annotations.objid;

@objid ("d5431c2e-135d-45a0-b064-c5d2987062dd")
public class BDProduit {
    @objid ("99c191d8-8c1c-471e-8161-6da15fd78d32")
    private List<Produit> listProduit = new ArrayList<Produit>();

    @objid ("4bfc4ea2-cdee-4a36-9388-0976b0266edd")
    public Produit produit;

    @objid ("a03a5fb2-756e-42f8-8895-b9bda184b2ec")
    public List<Produit> recupererListeProduit(int idVente) {
        List<Produit> listProduitVente = new ArrayList<Produit>();
        for(Produit produit: listProduit) {
            if (produit.getIdVente() == idVente) {
                listProduitVente.add(produit);
            }
        }
        return listProduitVente;
    }

    @objid ("58887ca7-ebc8-4b44-84ed-8fff9e196da7")
    public void ajouterProduit(Produit produit) {
        listProduit.add(produit);
    }

    @objid ("539cef50-7ca9-4195-bd27-7557f4e77da5")
    public void supprimerListeProduit(int idVente) {
        for(Produit produit: listProduit) {
            if (produit.getIdVente() == idVente) {
                listProduit.remove(produit);
            }
        }
    }

}
