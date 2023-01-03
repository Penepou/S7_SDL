package controleur;

import com.modeliosoft.modelio.javadesigner.annotations.objid;

@objid ("e99db5f9-235b-4610-b371-0022fa0880db")
public class ControlVerifierIdentification {
    @objid ("c974d4f2-cedd-4f2f-88a6-fcbd9ec16722")
    public boolean verifierIdentification(int id) {
        return id == 1001;
    }

}
