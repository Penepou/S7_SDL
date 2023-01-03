package entite;

import java.util.ArrayList;
import java.util.List;
import com.modeliosoft.modelio.javadesigner.annotations.objid;

@objid ("f4bdea6b-042d-453a-a43b-0ee53e9a82ca")
public class BDVente {
    @objid ("15862795-bf81-4a15-83ff-6052acde76c3")
    private List<Vente> listVente = new ArrayList<Vente>();

    @objid ("0835b469-5637-47ba-b4ec-0fa8a2728cb2")
    public Vente vente;

    @objid ("14884dd1-80b1-49a5-8d44-46c4622b40e3")
    public void ajouterVente(Vente vente) {
        listVente.add(vente);
    }

    @objid ("0151336d-b776-4005-8869-de20ca5c1b38")
    public int getSize() {
        return listVente.size();
    }

}
