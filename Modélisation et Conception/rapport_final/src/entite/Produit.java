package entite;

import com.modeliosoft.modelio.javadesigner.annotations.objid;

@objid ("2c42c169-cbc3-4526-993e-1754453065b1")
public class Produit {
    @objid ("8153907e-63c6-4267-875f-22f111dc494f")
    private String nom;

    @objid ("b58c69af-dcd2-428c-982d-efe4c12db4df")
    private String descriptif;

    @objid ("9701c39a-78f7-49e2-80aa-04ef3574a936")
    private String photo;

    @objid ("f8c997e0-6791-470c-a44b-f5b5e6b1b347")
    private String prixDeBase;

    @objid ("3aca582f-0e0b-44a2-b926-bdb6858465bd")
    private String prixDeVente;

    @objid ("b7ecb142-c283-4ac6-8ad3-6f1081b3dda0")
    private String taille;

    @objid ("3bf71a5a-8038-47b9-b4e2-ade953b6335e")
    private String quantite;

    @objid ("fd444914-5794-4716-b2d5-e6594a9d906b")
    private int idVente;

    @objid ("8701a17c-eb02-4f95-b8b7-a140e58769f9")
    private String nomTaille;

    @objid ("f7fe9227-4d7c-4636-b021-f5d96e925e31")
    public Produit(String nom, String descriptif, String photo, String prixDeBase, String prixDeVente, String nomTaille, String quantite, int idVente) {
        super();
        this.nom = nom;
        this.descriptif = descriptif;
        this.photo = photo;
        this.prixDeBase = prixDeBase;
        this.prixDeVente = prixDeVente;
        this.nomTaille = nomTaille;
        this.idVente = idVente;
    }

    @objid ("aaff681a-b0e9-4028-9cab-0fd495072ac4")
    public int getIdVente() {
        // Automatically generated method. Please delete this comment before entering specific code.
        return this.idVente;
    }

    @objid ("d009d8de-0d70-4799-8b6e-96b3acce81b5")
    public String getNom() {
        return nom;
    }

    @objid ("91033963-6872-4482-a397-441a981a44fb")
    public String getDescriptif() {
        return descriptif;
    }

    @objid ("02a33e39-d8bc-480b-adab-6890168b6c82")
    public String getPhoto() {
        return photo;
    }

    @objid ("9523965f-87a6-401b-a906-2429810d5b3d")
    public String getPrixDeBase() {
        return prixDeBase;
    }

    @objid ("b2aa08ed-5624-4fd4-b5a3-b13a369c1689")
    public String getPrixDeVente() {
        return prixDeVente;
    }

    @objid ("8a754a66-54b7-4fde-b376-12a15ccc3dc9")
    public String getTaille() {
        return taille;
    }

    @objid ("484ac322-fed6-4feb-a6ed-81de754f7e93")
    public String getQuantite() {
        return quantite;
    }

    @objid ("66ea0f1c-e0d0-48dd-ba90-e4071287842d")
    public String getNomTaille() {
        return nomTaille;
    }

}
