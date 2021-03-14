# Projet  : Déploiement Ansible :computer:
**Cadre :** Dans le but d'un apprentissage concret des technologies actuelles, j'ai développé un module qui permet de mettre en place une base de donnée locale sur une machine virtuelle distante. En complément, on peut accéder aux donnée de base de donnée via une api Flask qui utilise un port de la machine virtuelle.  

# Technologies :wrench:
**Python**
**Flask**
**Postgresql**

# Outils

 1. Une machine virtuelle don vous possedez, la clé privée

# Dépendances
```~ sudo  apt update```

```~ sudo  apt  install ansible```


# Fonctionnement :

copier ce repo github: 

```~ git clone https://github.com/jozuah/simplon_devcloud_ansible_vm_flask_postgres```

Se placer dans le dossier  /simplon_devcloud_ansible_vm_flask_postgres

 ```~ ansible-playbook -i hosts  playbook.yml --key-file votre-clé.pem```

ATTENTION : IL FAUT AU PREALABLE AVOIR OUVERT LE PORT 3000 DE VOTRE VM

# Accès à l'app flask :
Depuis votre navigateur :  adress_ip_de_la_vm:3000/
